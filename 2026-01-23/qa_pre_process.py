from betteryeah import BetterYeah
import requests
import json
import uuid
import re
import asyncio
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

better_yeah = BetterYeah()

DEFAULT_ACTION="""
    data_source:
      - "严禁编造信息或使用常识补充"

    决策链:
      第一步_检查商品问题:
        - "问题涉及具体商品 + dialogue无链接且product_data为空 → 询问商品链接并跳过第二步"
        - "问题涉及具体商品 + 有链接但product_data为空 → [TRANSFER]"
        - "其他情况 → 进入第二步"

      第二步_信息检索:
        -  在 product_data、faq_knowledge、common_knowledge 中查找"
	    -  优先使用 product_data，其次使用faq_knowledge，最次使用 common_knowledge的内容回答"

    check_list:
      - "回复中每条信息是否能在数据源中找到原文？→ 必须"
      - "是否编造了数据源中不存在的信息？→ 禁止"
      - “引用 faq_knowledge 中的回答时，不要改变原文 → 必须”

"""

def generate_app_id():
    return re.sub(r'-', '', str(uuid.uuid4()))

def get_current_datetime():
    now = datetime.now()
    weekdays = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    return f"{now.year}年{now.month}月{now.day}日（{weekdays[now.weekday()]}） {now.hour:02d}:{now.minute:02d}:{now.second:02d}"

def resolve_taobao_short_link(url):
    """解析淘宝短链，优先获取 id，其次获取 shareDetailItemId"""
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
    }
    try:
        resp = requests.get(url, headers=headers, timeout=5)
        if resp.status_code != 200:
            return None
        
        html = resp.text
        # 1. 提取 JS 变量中的长链接内容
        url_match = re.search(r"var\s+url\s*=\s*['\"]([^'\"]+)['\"]", html)
        content_to_search = url_match.group(1) if url_match else html

        # 2. 尝试匹配 id (优先级最高)
        id_match = re.search(r'[?&]id=(\d+)', content_to_search)
        if id_match:
            return id_match.group(1)

        # 3. 如果没找到 id，则尝试匹配 shareDetailItemId
        share_id_match = re.search(r'[?&]shareDetailItemId=(\d+)', content_to_search)
        if share_id_match:
            return share_id_match.group(1)

    except Exception as e:
        print(f"[警告] 解析失败: {e}")
    
    return None

def extract_ids_from_dialogue(dialogue_data, platform=None):
    """从对话中提取商品ID"""
    ids = []
    id_map = {}
    for message in dialogue_data:
        if not message or not isinstance(message, dict):
            continue
        if message.get("role") not in ["user", "assistant"]:
            continue
        content = message.get("content")
        if not content:
            continue
        if isinstance(content, str):
            combined_text = content
        elif isinstance(content, dict):
            combined_text = f"{content.get('text', '')} {content.get('url', '')}"
        else:
            continue
        
        if platform == 'jingdong':
            # 提取京东商品链接中的ID，格式: https://item.jd.com/10119818260214.html
            jd_links = re.findall(r'https?://item\.jd\.com/(\d+)\.html', combined_text)
            for item_id in jd_links:
                if item_id and item_id not in ids:
                    ids.append(item_id)
                    if item_id not in id_map:
                        id_map[item_id] = f"https://item.jd.com/{item_id}.html"
        elif platform == 'pinduoduo':
            # 提取拼多多商品链接中的ID，格式: https://mobile.yangkeduo.com/goods.html?goods_id=890314091995
            pdd_links = re.findall(r'https?://(?:mobile\.)?yangkeduo\.com/goods\.html[^\s]*?goods_id=(\d+)', combined_text)
            for item_id in pdd_links:
                if item_id and item_id not in ids:
                    ids.append(item_id)
                    if item_id not in id_map:
                        id_map[item_id] = f"https://mobile.yangkeduo.com/goods.html?goods_id={item_id}"
            # 也支持直接从 URL 参数中提取 goods_id
            for item_id in re.findall(r'goods_id=(\d+)', combined_text):
                if item_id and item_id not in ids:
                    ids.append(item_id)
                    if item_id not in id_map:
                        id_map[item_id] = f"https://mobile.yangkeduo.com/goods.html?goods_id={item_id}"
        else:
            # 提取淘宝短链并解析
            short_links = re.findall(r'https?://e\.tb\.cn/[^\s]+', combined_text)
            print('解析短链', short_links)
            for link in short_links:
                resolved_id = resolve_taobao_short_link(link)
                if resolved_id:
                    if resolved_id not in ids:
                        ids.append(resolved_id)
                    if resolved_id not in id_map:
                        id_map[resolved_id] = link
                    
            for item_id in re.findall(r'id=(\d+)', combined_text):
                if item_id and item_id not in ids:
                    ids.append(item_id)
    return ids, id_map

async def fetch_product_and_sku(database_id, item_ids, shop_code=None, platform=None):
    """根据商品ID查询商品和SKU
    
    Args:
        database_id: 数据库ID
        item_ids: 商品ID列表（京东平台为sku_id列表）
        shop_code: 店铺编码，如果提供则通过sub_flow获取SKU
        platform: 平台类型，如果是jingdong则item_ids为sku_id，需要先查询对应的商品id
    """
    if not item_ids:
        return []
    
    # 京东平台：链接中的ID是sku_id，需要先从【sku参数表】查找对应的商品id
    if platform == 'jingdong':
        sku_ids_str = "','".join(str(sku_id) for sku_id in item_ids)
        try:
            sku_res = await better_yeah.database.execute_database(
                base_id=database_id,
                executable_sql=f"SELECT DISTINCT 商品id FROM sku参数表 WHERE sku_id IN ('{sku_ids_str}') LIMIT 100"
            )
            sku_data = sku_res.data.data if sku_res.success and hasattr(sku_res.data, 'data') else []
            if sku_data:
                # 提取商品id列表，替换原来的item_ids
                item_ids = [str(row.get('商品id')) for row in sku_data if row.get('商品id')]
                print(f"[京东] 从sku_id转换得到商品id: {item_ids}")
            else:
                print(f"[京东] 未从sku参数表找到对应商品id，sku_ids: {item_ids}")
                return []
        except Exception as e:
            print(f"[京东sku查询失败] {e}")
            return []
    
    if not item_ids:
        return []
    
    ids_str = "','".join(str(pid) for pid in item_ids)
    
    try:
        # 查询商品基本信息
        product_res = await better_yeah.database.execute_database(
            base_id=database_id,
            executable_sql=f"SELECT * FROM 店铺商品目录 WHERE 商品id IN ('{ids_str}') LIMIT 100"
        )
        products = product_res.data.data if product_res.success and hasattr(product_res.data, 'data') else []
    except Exception as e:
        print(f"[商品查询失败] {e}")
        return []
    
    if not products:
        return []
    
    skus = []
    sku_map = {}
    
    if shop_code:
        # 通过sub_flow获取SKU信息
        print(f"[sub_flow] 使用shop_code: {shop_code} 获取SKU信息")
        
        # 为每个商品ID并发调用sub_flow获取SKU
        sku_tasks = []
        for product in products:
            if not isinstance(product, dict):
                continue
                
            item_id = product.get("商品id", "")
            if not item_id:
                continue
            
            # 创建sub_flow任务
            sku_tasks.append(
                better_yeah.sub_flow.execute(
                    flow_id="9fd77172552649cfafe3aa24540dd61c",
                    parameter={"product_id": str(item_id), "shop_code": shop_code}
                )
            )
        
        if sku_tasks:
            # 并发执行所有sub_flow任务
            sku_results = await asyncio.gather(*sku_tasks, return_exceptions=True)
            
            for idx, (product, sku_result) in enumerate(zip(products, sku_results)):
                if not isinstance(product, dict):
                    continue
                    
                item_id = product.get("商品id", "")
                if not item_id:
                    continue
                
                sku_map[item_id] = []
                
                # 处理sub_flow返回结果
                if isinstance(sku_result, Exception):
                    print(f"[sub_flow] 商品{item_id} SKU查询异常: {sku_result}")
                    continue
                
                # 解析sub_flow返回的SKU数据
                try:
                    # 根据返回结构，我们需要访问: sku_result.data.run_result
                    if hasattr(sku_result, 'data') and hasattr(sku_result.data, 'run_result'):
                        run_result = sku_result.data.run_result
                        
                        # 从调试信息看，run_result是一个字典，包含'skus'键
                        if isinstance(run_result, dict) and 'skus' in run_result:
                            skus_data = run_result['skus']
                            
                            # 进一步获取sku列表
                            if isinstance(skus_data, dict) and 'sku' in skus_data:
                                api_skus = skus_data['sku']
                            else:
                                api_skus = []
                        else:
                            api_skus = []
                    else:
                        print(f"[sub_flow] 商品{item_id} 返回结构不符合预期")
                        api_skus = []
                    
                    print(f"[sub_flow] 商品{item_id} 解析到{len(api_skus)}个SKU")
                    
                    for api_sku in api_skus:
                        if isinstance(api_sku, dict) and 'properties_name' in api_sku:
                            sku_info = {
                                "sku": api_sku.get("properties_name", ""),
                                "quantity": api_sku.get("quantity", 0),
                                "status": api_sku.get("status", ""),
                                "sku图识别结果": ""  # sub_flow返回没有图片信息
                            }
                        else:
                            continue
                            
                        sku_map[item_id].append(sku_info)
                        skus.append({
                            "商品id": item_id,
                            "sku": sku_info["sku"],
                            "quantity": sku_info["quantity"],
                            "status": sku_info["status"],
                            "sku图识别结果": sku_info["sku图识别结果"]
                        })
                    
                    print(f"[sub_flow] 商品{item_id} 获取到{len(sku_map[item_id])}个SKU")
                    
                except Exception as e:
                    print(f"[sub_flow] 商品{item_id} SKU解析失败: {e}")
                    import traceback
                    print(traceback.format_exc())
    else:
        print("[sub_flow] 未提供shop_code，使用数据库查询SKU")
    
    # 如果没有通过sub_flow获取到SKU，或者没有shop_code，则从数据库获取
    if not sku_map:
        try:
            sku_res = await better_yeah.database.execute_database(
                base_id=database_id,
                executable_sql=f"SELECT 商品id, sku, sku图识别结果 FROM sku参数表 WHERE 商品id IN ('{ids_str}') LIMIT 500"
            )
            skus = sku_res.data.data if sku_res.success and hasattr(sku_res.data, 'data') else []
            
            # 重新构建sku_map
            for sku in skus:
                if isinstance(sku, dict) and sku.get("商品id"):
                    sku_map.setdefault(sku["商品id"], []).append({
                        "sku": sku.get("sku", ""),
                        "sku图识别结果": sku.get("sku图识别结果", "")
                    })
                    
            print(f"[数据库] 获取到{len(skus)}个SKU记录")
        except Exception as e:
            print(f"[SKU查询失败] {e}")
    
    # 组装结果
    result = []
    for product in products:
        if not isinstance(product, dict):
            continue
            
        item_id = product.get("商品id", "")
        processed = {
            "商品id": item_id,
            "商品标题": product.get("商品标题", ""),
            "商品链接": product.get("商品链接", ""),
            "参数": product.get("参数", ""),
            "商品详情页识别结果": [],
            "轮播图识别结果": [],
            "卖点": product.get("卖点", ""),
            "补充知识": product.get("补充知识", ""),
            "商品状态": product.get("商品状态", "上架中"),
            "sku": sku_map.get(item_id, [])
        }
        
        # 处理图片识别结果
        for field in ["商品详情页识别结果", "轮播图识别结果"]:
            raw = product.get(field, "")
            if raw:
                try:
                    items = json.loads(raw) if isinstance(raw, str) else raw
                    if isinstance(items, list):
                        for item in items:
                            if isinstance(item, dict):
                                desc = {k: v for k, v in item.items() if k.startswith("image_desc") or k.startswith("image_url")}
                                if desc:
                                    processed[field].append(desc)
                except:
                    pass
        result.append(processed)
    
    sku_total = sum(len(p['sku']) for p in result)
    print(f"[数据] 商品ID查询:{len(result)}个 SKU:{sku_total}个 (来源: {'sub_flow' if shop_code else '数据库'})")
    
    # 如果需要，可以打印一些调试信息
    if shop_code and sku_map:
        for item_id, sku_list in sku_map.items():
            if sku_list:
                print(f"  商品{item_id}: {len(sku_list)}个SKU, 示例: {sku_list[0]['sku'][:50]}...")
    
    return result

async def fetch_behavior_new(database_id, top_situation):
    if not top_situation:
        print("[fetch_behavior] top_situation为空，返回空对象")
        return {}

    try:
        sql = f"SELECT situation, action FROM 场景策略 WHERE situation = '{top_situation}' LIMIT 50"
        res = await better_yeah.database.execute_database(
            base_id=database_id,
            executable_sql=sql
        )
        result = res.data.data if res.success and hasattr(res.data, 'data') else []

        if result[0]:
            return result[0]

        return {}
    except Exception as e:
        print(f"[fetch_behavior] 异常: {type(e).__name__}: {e}")
        return {}
        
async def fetch_behavior(database_id, top_situations):
    """
    根据 top_situations 查询场景策略，结果按 top_situations 顺序排序
    """
    
    if not top_situations:
        print("[fetch_behavior] top_situations为空，返回空列表")
        return []
    
    try:
        # 构建 IN 查询条件
        situations_str = "','".join(s.replace("'", "''") for s in top_situations)
        sql = f"SELECT situation, action FROM 场景策略 WHERE situation IN ('{situations_str}') LIMIT 50"
        
        res = await better_yeah.database.execute_database(
            base_id=database_id,
            executable_sql=sql
        )
        
        
        result = res.data.data if res.success and hasattr(res.data, 'data') else []
        
        # 按照 top_situations 的顺序排序
        situation_order = {s: i for i, s in enumerate(top_situations)}
        
        result.sort(key=lambda x: situation_order.get(x.get("situation", ""), len(top_situations)))
        
        # 如果 action 为空，使用 DEFAULT_ACTION
        for item in result:
            if not item.get("action"):
                item["action"] = DEFAULT_ACTION
        
        return result
    except Exception as e:
        print(f"[fetch_behavior] 异常: {type(e).__name__}: {e}")
        import traceback
        print(f"[fetch_behavior] 堆栈: {traceback.format_exc()}")
        return []


def fetch_knowledge_base_single(auth, kb_config, partition_id, query_content, msg_index):
    """单次知识库查询"""
    if not all([auth.get("user_access_key"), auth.get("user_workspace_id"), partition_id, query_content]):
        return []
    
    body = {
        "top_k": kb_config.get("top_k", 5),
        "content": query_content,
        "partition_id": partition_id,
        "threshold": kb_config.get("threshold", 0.5),
        "ranking_strategy": kb_config.get("ranking_strategy", 1),
        "similarity": kb_config.get("similarity", 0.3),
        "hit_strategy": [3],
        "tags": [],
    }

    headers = {
        "accept": "application/json",
        "application-id": generate_app_id(),
        "content-type": "application/json",
        "workspace-id": auth["user_workspace_id"],
        "access-key": auth["user_access_key"],
    }

    try:
        response = requests.post(
            "https://ai-api.betteryeah.com/v1/oapi/dataset/content-match",
            json=body, headers=headers, timeout=15
        )

        if response.status_code == 200:
            result = response.json()
            match_contents = result.get("data", {}).get("match_contents", [])
            return match_contents
    except:
        pass

    return []

def fetch_knowledge_base_batch(auth, kb_config, partition_id, messages, kb_name):
    """并行查询多条消息"""
    start_time = datetime.now()
    
    if not messages or not partition_id:
        return []
    
    # 过滤空消息
    valid_messages = [(idx, msg) for idx, msg in enumerate(messages) if msg and msg.strip()]
    
    if not valid_messages:
        return []
    
    # 使用线程池并行查询所有消息
    all_results = []
    seen_contents = set()
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        # 提交所有查询任务
        futures = []
        for idx, msg in valid_messages:
            future = executor.submit(
                fetch_knowledge_base_single,
                auth, kb_config, partition_id, msg, f"{kb_name}-{idx}"
            )
            futures.append((idx, future))
        
        # 收集结果
        for idx, future in futures:
            try:
                results = future.result(timeout=20)
                for item in results:
                    if isinstance(item, dict):
                        content = item.get("content", "")
                        if content and content not in seen_contents:
                            seen_contents.add(content)
                            all_results.append(item)
            except:
                pass
    
    # 按相似度排序并取前10个
    all_results.sort(key=lambda x: x.get("similarity", 0.0), reverse=True)
    final_results = all_results[:10]
    
    elapsed = (datetime.now() - start_time).total_seconds()
    print(f"[{kb_name}] {len(valid_messages)}条查询 → {len(final_results)}条结果 | {elapsed:.2f}秒")
    
    return final_results

def merge(a, b):
    if a is None and b is None:
        return None
    if a is None:
        return b
    if b is None:
        return a
    return {**a, **b}

def filter_available_tools(tool_list, behavior_action):
    """
    筛选可用工具：
    1. 如果 tool.get('tool') 在 behavior.action 中存在，则该工具可用
    2. 如果 tool 的 params 中的任意 key 在 behavior.action 中存在，则该工具可用
    """
    if not tool_list or not behavior_action:
        return []
    
    available_tools = []
    for tool in tool_list:
        # 检查 tool 名称是否在 behavior_action 中
        tool_name = tool.get("tool")
        tool_type = tool.get("type")
        is_run = tool.get('run')

        # order_query 且 type 为 system 时默认可用
        if tool_name == "order_query" and tool_type == "system":
            available_tools.append(tool)
            continue

        if is_run:
            available_tools.append(tool)
            continue
        if tool_name and tool_name in behavior_action:
            available_tools.append(tool)
            continue

        # 检查 params 中的 key 是否在 behavior_action 中
        params = tool.get("params", {})
        for key in params.keys():
            if key in behavior_action:
                available_tools.append(tool)
                break
    return available_tools

def execute_custom_tool(tool, dialogue, auth, product_data=None):
    """
    执行 custom 类型的工具，通过 REST API 调用
    """
    flow_id = tool.get("flow_id")
    if not flow_id:
        return {"error": "missing flow_id"}
    
    url = f"https://ai-api.betteryeah.com/v1/public_api/rest_api/{flow_id}/execute_flow"
    headers = {
        "Content-Type": "application/json",
        "Access-Key": auth.get("user_access_key", ""),
        "Workspace-Id": auth.get("user_workspace_id", "")
    }
    payload = {
        "inputs": {
            "dialogue": dialogue,
            "tool": tool,
            "product_data": product_data,
            "database_config": database_config,
            "shop_id": shop_id,
            "agent_id": auth.get("agent_id", "")
        }
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        if response.status_code == 200:
            result = response.json()
            if result.get("success") and result.get("data", {}).get("status") == "SUCCEEDED":
                return result.get("data", {}).get("run_result", "")
            else:
                return {"error": result.get("message", "执行失败"), "data": result.get("data")}
        else:
            return {"error": f"HTTP {response.status_code}", "body": response.text}
    except Exception as e:
        return {"error": str(e)}

async def execute_tool_subflows(available_tools, start_param, auth=None, product_data=None):
    """
    并发执行所有可用工具的子流程
    """
    if not available_tools:
        return []
    
    tasks = []
    custom_tools = []  # 记录 custom 类型工具的索引
    
    for idx, tool in enumerate(available_tools):
        flow_id = tool.get("flow_id")
        if not flow_id:
            continue
            
        tool_type = tool.get("type")
        if tool_type == "custom" and auth:
            # custom 类型使用 REST API 调用
            task = asyncio.get_event_loop().run_in_executor(
                None,
                execute_custom_tool,
                tool,
                start_param.get("dialogue2"),
                auth,
                product_data
            )
            tasks.append(task)
            custom_tools.append(idx)
        else:
            # 默认使用 sub_flow.execute
            tasks.append(better_yeah.sub_flow.execute(flow_id=flow_id, parameter={"tool": tool, "dialogue": start_param.get("dialogue2"), "product_data": product_data, "database_config": database_config}))
    
    if not tasks:
        return []
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # 组装返回结果
    tool_results = []
    for idx, (tool, result) in enumerate(zip(available_tools, results)):
        if isinstance(result, Exception):
            result_data = str(result)
        elif idx in custom_tools:
            # custom 类型的结果已经是处理过的数据
            result_data = result
        elif hasattr(result, 'data') and hasattr(result.data, 'run_result'):
            result_data = result.data.run_result
        elif hasattr(result, 'data'):
            result_data = result.data
        else:
            result_data = result
        tool_results.append({
            "tool": tool.get("tool"),
            "name": tool.get("name"),
            "type": tool.get("type"),
            "flow_id": tool.get("flow_id"),
            "result": result_data
        })
    return tool_results

async def main():
    database_id = database_config["id"]
    auth = start.get("auth", {})
    kb_config = start.get("knowledge_base_config", {})
    messages = start.get("messages", [])

     # 获取工具列表中的shop_code
    tool_list = start.get("tools", [])
    shop_code = None
    
    # 从工具列表中查找第一个有shop_code的工具
    for tool in tool_list:
        if isinstance(tool, dict) and tool.get("shop_code"):
            shop_code = tool["shop_code"]
            print(f"[配置] 使用shop_code: {shop_code}")
            break
    
    # 检查数组长度
    if len(messages) >= 2:
        # 取数组的最后两个元素
        latest_messages = messages[-2:]
    else:
        # 如果元素少于两个，直接返回整个数组
        latest_messages = messages
    
    start_time = datetime.now()
    
    # 提取商品ID
    item_ids, id_map = extract_ids_from_dialogue(dialogue, platform)
    
    print(f"[提取] 商品ID:{item_ids}")
    
    # 并行执行所有查询任务
    tasks = [
        fetch_behavior_new(database_id, ''),
        asyncio.get_event_loop().run_in_executor(
            None, 
            fetch_knowledge_base_batch, 
            auth, kb_config, kb_config.get("common_partition_id", ""), latest_messages, "common"
        ),
        asyncio.get_event_loop().run_in_executor(
            None,
            fetch_knowledge_base_batch,
            auth, kb_config, kb_config.get("faq_partition_id", ""), latest_messages, "faq"
        )
    ]
    
    # 添加商品查询任务
    if item_ids:
        tasks.append(fetch_product_and_sku(database_id, item_ids, shop_code, platform))
    
    # 执行所有任务
    results = await asyncio.gather(*tasks)
    
    # 解析结果
    behavior_result = results[0]
    print("behavior_result", behavior_result)

    common_result = results[1]
    faq_result = results[2]
    
    # 处理商品数据
    product_sku_result = []
    
    if item_ids and len(results) > 3:
        products_from_ids = results[3]
        # 注入 short_link
        print(f"[调试] ID映射: {id_map}")
        for p in products_from_ids:
            p["short_link"] = "" # 初始化短链字段
            pid = p.get("商品id")
            if pid and str(pid) in id_map:
                 p["short_link"] = id_map[str(pid)]
        product_sku_result.extend(products_from_ids)
    
    # 筛选并执行可用工具
    tool_list = start.get("tools", [])
    behavior_action = behavior_result.get("action", "") if behavior_result else ""
    available_tools = filter_available_tools(tool_list, behavior_action)
    print(f"[工具] 可用工具: {[t.get('name') for t in available_tools]}")
    
    print("product_sku_result", product_sku_result)
    tool_results = await execute_tool_subflows(available_tools, start, auth, product_data=product_sku_result)
    
    # 处理知识库结果
    processed_common = [item.get("content", "") for item in common_result if isinstance(item, dict) and item.get("content")]
    processed_faq = [{"question": item.get("content", ""), "answer": item.get("extra_info", {})} for item in faq_result if isinstance(item, dict) and (item.get("content") or item.get("extra_info"))]
    
    elapsed = (datetime.now() - start_time).total_seconds()
    print(f"[完成] 商品{len(product_sku_result)}个 | common{len(processed_common)}条 | faq{len(processed_faq)}条 | 总耗时{elapsed:.2f}秒")

    return {
        "data": product_sku_result,
        "behavior": behavior_result,
        "common": processed_common,
        "faq": processed_faq,
        "current_time": get_current_datetime(),
        "tool_results": tool_results
    }
