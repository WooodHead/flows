from betteryeah import BetterYeah
import json
import re
import string
import requests
import asyncio


better_yeah = BetterYeah()

def clean_string(text):
    """
    清理字符串:去除空格、换行、标点符号
    """
    print(f"[clean_string] 输入文本: {repr(text)}")

    if not text:
        print("[clean_string] 文本为空,返回空字符串")
        return ""

    # 去除所有空白字符(空格、制表符、换行符等)
    text = re.sub(r'\s+', '', text)
    print(f"[clean_string] 去除空白字符后: {repr(text)}")

    # 去除英文标点符号
    text = text.translate(str.maketrans('', '', string.punctuation))
    print(f"[clean_string] 去除英文标点后: {repr(text)}")

    # 去除中文标点符号
    chinese_punctuation = '。,、;:?!…—·ˉ¨''""々～‖∶"''{}[]()<>《》【】「」『』〔〕／\\'
    text = re.sub(f'[{re.escape(chinese_punctuation)}]', '', text)
    print(f"[clean_string] 清理后的最终文本: {repr(text)}")

    return text


def levenshtein_distance(str1, str2):
    """
    计算 Levenshtein 距离
    """
    m, n = len(str1), len(str2)
    matrix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        matrix[i][0] = i
    for j in range(n + 1):
        matrix[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost
            )

    return matrix[m][n]


def calculate_similarity(str1, str2):
    """
    计算两个字符串的相似度百分比(基于 Levenshtein 距离)
    自动清理空格、换行和标点符号

    Args:
        str1: 第一个字符串
        str2: 第二个字符串

    Returns:
        相似度百分比 (0-100)
    """
    print("\n[calculate_similarity] 比较字符串:")
    print(f"  str1原文: {repr(str1[:100])}..." if len(str1) > 100 else f"  str1原文: {repr(str1)}")
    print(f"  str2原文: {repr(str2[:100])}..." if len(str2) > 100 else f"  str2原文: {repr(str2)}")

    # 清理字符串
    str1 = clean_string(str1)
    str2 = clean_string(str2)

    if not str1 and not str2:
        print("[calculate_similarity] 两个字符串都为空,相似度: 100.0")
        return 100.0

    if not str1 or not str2:
        print("[calculate_similarity] 其中一个字符串为空,相似度: 0.0")
        return 0.0

    distance = levenshtein_distance(str1, str2)
    max_length = max(len(str1), len(str2))
    print(f"[calculate_similarity] Levenshtein距离: {distance}, 最大长度: {max_length}")

    similarity = (1.0 - distance / max_length) * 100.0
    print(f"[calculate_similarity] 计算相似度: {similarity:.2f}%")
    return similarity


def check_similarity(text1, text2, threshold=70):
    """检查两个文本的相似度"""
    similarity = calculate_similarity(text1, text2)
    return similarity >= threshold


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


def extract_assistant_replies(dialogue):
    """提取对话中assistant的所有回复内容"""
    print("\n[extract_assistant_replies] 开始提取assistant回复")
    print(f"[extract_assistant_replies] 对话消息数量: {len(dialogue) if dialogue else 0}")

    if not dialogue:
        print("[extract_assistant_replies] 对话为空,返回空列表")
        return []

    assistant_replies = []

    for idx, message in enumerate(dialogue):
        if isinstance(message, dict) and message.get("role") == "assistant":
            print(f"[extract_assistant_replies] 找到第{idx}条assistant消息")
            content = message.get("content", {})

            # 提取文本内容
            if isinstance(content, dict):
                text = content.get("text", "")
                # 处理text可能是列表的情况
                if isinstance(text, list) and len(text) > 0:
                    text = text[0]  # 取第一个元素
            else:
                text = str(content) if content else ""

            # 只记录有文字内容的回复
            if text and str(text).strip():
                assistant_replies.append(str(text).strip())
                print(f"[extract_assistant_replies] 添加回复内容(前50字): {str(text).strip()[:50]}...")

    print(f"[extract_assistant_replies] 共提取到{len(assistant_replies)}条assistant回复")
    return assistant_replies

def parse_dialogue_data(dialogue_data):
    """解析对话数据"""
    print(f"\n[parse_dialogue_data] 数据类型: {type(dialogue_data)}")

    if isinstance(dialogue_data, list):
        print(f"[parse_dialogue_data] 数据已是列表格式,长度: {len(dialogue_data)}")
        return dialogue_data
    if isinstance(dialogue_data, str):
        print(f"[parse_dialogue_data] 字符串数据,长度: {len(dialogue_data)}")
        try:
            parsed = json.loads(dialogue_data.strip())
            print(f"[parse_dialogue_data] JSON解析成功,结果类型: {type(parsed)}")
            return parsed
        except Exception as e:
            print(f"[parse_dialogue_data] JSON解析失败: {e}")
            raise Exception(f"无法解析对话数据: {e}")
    # 如果是其他格式，直接返回
    print("[parse_dialogue_data] 其他格式,直接返回")
    return dialogue_data

def filter_available_tools(tool_list, behavior_action):
    """
    筛选可用工具：
    1. 如果 tool.get('tool') 在 behavior.action 中存在，则该工具可用
    2. 如果 tool 的 params 中的任意 key 在 behavior.action 中存在，则该工具可用
    """
    print("\n" + "-"*50)
    print("[filter_available_tools] 开始筛选可用工具")
    print(f"[filter_available_tools] 工具列表数量: {len(tool_list) if tool_list else 0}")
    print(f"[filter_available_tools] behavior_action: {behavior_action}")

    if not tool_list or not behavior_action:
        print("[filter_available_tools] 工具列表或behavior_action为空,返回空列表")
        return []

    available_tools = []
    for idx, tool in enumerate(tool_list):
        # 检查 tool 名称是否在 behavior_action 中
        tool_name = tool.get("tool")
        tool_type = tool.get("type")
        is_run = tool.get('run')

        print(f"\n[filter_available_tools] 检查第{idx+1}个工具:")
        print(f"  - tool_name: {tool_name}")
        print(f"  - tool_type: {tool_type}")
        print(f"  - is_run: {is_run}")
        print(f"  - flow_id: {tool.get('flow_id')}")

        # order_query 且 type 为 system 时默认可用
        if tool_name == "order_query" and tool_type == "system":
            print(f"  ✓ 匹配条件: order_query系统工具,默认可用")
            available_tools.append(tool)
            continue

        if is_run:
            print(f"  ✓ 匹配条件: is_run=True,工具可用")
            available_tools.append(tool)
            continue
        if tool_name and tool_name in behavior_action:
            print(f"  ✓ 匹配条件: tool_name '{tool_name}' 在 behavior_action 中")
            available_tools.append(tool)
            continue

        # 检查 params 中的 key 是否在 behavior_action 中
        params = tool.get("params", {})
        print(f"  - params keys: {list(params.keys())}")
        matched_key = None
        for key in params.keys():
            if key in behavior_action:
                matched_key = key
                available_tools.append(tool)
                break

        if matched_key:
            print(f"  ✓ 匹配条件: params中的key '{matched_key}' 在 behavior_action 中")
        else:
            print(f"  ✗ 未匹配任何条件,工具不可用")

    print(f"\n[filter_available_tools] 筛选完成,可用工具数量: {len(available_tools)}")
    print(f"[filter_available_tools] 可用工具列表: {[t.get('tool') for t in available_tools]}")
    print("-"*50)
    return available_tools

def execute_custom_tool(tool, dialogue, auth, product_data=None):
    """
    执行 custom 类型的工具，通过 REST API 调用
    """
    tool_name = tool.get("tool", "unknown")
    flow_id = tool.get("flow_id")

    print(f"\n[execute_custom_tool] 开始执行自定义工具")
    print(f"[execute_custom_tool] 工具名称: {tool_name}")
    print(f"[execute_custom_tool] flow_id: {flow_id}")

    if not flow_id:
        print(f"[execute_custom_tool] ✗ 错误: 缺少flow_id")
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

    print(f"[execute_custom_tool] 请求URL: {url}")
    print(f"[execute_custom_tool] Workspace-Id: {auth.get('user_workspace_id', '')}")
    print(f"[execute_custom_tool] 请求payload keys: {list(payload['inputs'].keys())}")

    try:
        print(f"[execute_custom_tool] 发送POST请求...")
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        print(f"[execute_custom_tool] 响应状态码: {response.status_code}")

        if response.status_code == 200:
            result = response.json()
            status = result.get("data", {}).get("status")
            success = result.get("success")
            print(f"[execute_custom_tool] 响应success: {success}, status: {status}")

            if success and status == "SUCCEEDED":
                run_result = result.get("data", {}).get("run_result", "")
                print(f"[execute_custom_tool] ✓ 执行成功")
                print(f"[execute_custom_tool] 返回结果类型: {type(run_result)}")
                if isinstance(run_result, str):
                    print(f"[execute_custom_tool] 返回结果(前200字): {run_result[:200]}..." if len(run_result) > 200 else f"[execute_custom_tool] 返回结果: {run_result}")
                return run_result
            else:
                error_msg = result.get("message", "执行失败")
                print(f"[execute_custom_tool] ✗ 执行失败: {error_msg}")
                print(f"[execute_custom_tool] 响应data: {result.get('data')}")
                return {"error": error_msg, "data": result.get("data")}
        else:
            print(f"[execute_custom_tool] ✗ HTTP错误: {response.status_code}")
            print(f"[execute_custom_tool] 响应内容: {response.text[:500]}..." if len(response.text) > 500 else f"[execute_custom_tool] 响应内容: {response.text}")
            return {"error": f"HTTP {response.status_code}", "body": response.text}
    except Exception as e:
        print(f"[execute_custom_tool] ✗ 异常: {str(e)}")
        import traceback
        print(f"[execute_custom_tool] 异常堆栈:\n{traceback.format_exc()}")
        return {"error": str(e)}

async def execute_tool_subflows(available_tools, start_param, auth=None, product_data=None):
    """
    并发执行所有可用工具的子流程
    """
    print("\n" + "="*50)
    print("[execute_tool_subflows] 开始执行工具子流程")
    print(f"[execute_tool_subflows] 可用工具数量: {len(available_tools) if available_tools else 0}")

    if not available_tools:
        print("[execute_tool_subflows] 无可用工具,返回空列表")
        return []

    tasks = []
    custom_tools = []  # 记录 custom 类型工具的索引
    task_tool_mapping = []  # 记录任务与工具的映射关系

    print("\n[execute_tool_subflows] 准备执行任务:")
    for idx, tool in enumerate(available_tools):
        flow_id = tool.get("flow_id")
        tool_name = tool.get("tool", "unknown")
        tool_type = tool.get("type")

        print(f"\n  [{idx+1}] 工具: {tool_name}")
        print(f"      类型: {tool_type}")
        print(f"      flow_id: {flow_id}")

        if not flow_id:
            print(f"      ✗ 跳过: 缺少flow_id")
            continue

        if tool_type == "custom" and auth:
            # custom 类型使用 REST API 调用
            print(f"      → 使用REST API调用(custom类型)")
            task = asyncio.get_event_loop().run_in_executor(
                None,
                execute_custom_tool,
                tool,
                start_param.get("dialogue2"),
                auth,
                product_data
            )
            tasks.append(task)
            custom_tools.append(len(tasks) - 1)
            task_tool_mapping.append({"idx": idx, "tool_name": tool_name, "type": "custom"})
        else:
            # 默认使用 sub_flow.execute
            print(f"      → 使用sub_flow.execute调用")
            tasks.append(better_yeah.sub_flow.execute(flow_id=flow_id, parameter={"tool": tool, "dialogue": start_param.get("dialogue2"), "product_data": product_data, "database_config": database_config}))
            task_tool_mapping.append({"idx": idx, "tool_name": tool_name, "type": "subflow"})

    if not tasks:
        print("\n[execute_tool_subflows] 无有效任务,返回空列表")
        return []

    print(f"\n[execute_tool_subflows] 开始并发执行 {len(tasks)} 个任务...")
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(f"[execute_tool_subflows] 并发执行完成,获得 {len(results)} 个结果")

    # 组装返回结果
    tool_results = []
    print("\n[execute_tool_subflows] 处理执行结果:")

    for idx, (tool, result) in enumerate(zip(available_tools, results)):
        tool_name = tool.get("tool", "unknown")
        print(f"\n  [{idx+1}] 工具: {tool_name}")
        print(f"      原始结果类型: {type(result)}")

        if isinstance(result, Exception):
            result_data = str(result)
            print(f"      ✗ 执行异常: {result_data}")
        elif idx in custom_tools:
            # custom 类型的结果已经是处理过的数据
            result_data = result
            print(f"      ✓ custom类型结果")
            if isinstance(result_data, dict) and "error" in result_data:
                print(f"      ✗ 包含错误: {result_data.get('error')}")
            else:
                result_str = str(result_data)
                print(f"      结果预览: {result_str[:100]}..." if len(result_str) > 100 else f"      结果: {result_str}")
        elif hasattr(result, 'data') and hasattr(result.data, 'run_result'):
            result_data = result.data.run_result
            print(f"      ✓ subflow结果(data.run_result)")
            result_str = str(result_data)
            print(f"      结果预览: {result_str[:100]}..." if len(result_str) > 100 else f"      结果: {result_str}")
        elif hasattr(result, 'data'):
            result_data = result.data
            print(f"      ✓ subflow结果(data)")
            result_str = str(result_data)
            print(f"      结果预览: {result_str[:100]}..." if len(result_str) > 100 else f"      结果: {result_str}")
        else:
            result_data = result
            print(f"      ✓ 直接结果")
            result_str = str(result_data)
            print(f"      结果预览: {result_str[:100]}..." if len(result_str) > 100 else f"      结果: {result_str}")

        tool_results.append({
            "tool": tool.get("tool"),
            "name": tool.get("name"),
            "type": tool.get("type"),
            "flow_id": tool.get("flow_id"),
            "result": result_data
        })

    print(f"\n[execute_tool_subflows] 处理完成,返回 {len(tool_results)} 个工具结果")
    print("="*50)
    return tool_results

# 必须保证节点中存在一个main函数
async def main():
    try:
        print("\n" + "="*60)
        print("开始执行促单预处理流程")
        print("="*60)

        # 检查促单功能是否启用
        promotion_enabled = sop_config.get("promotion_enabled", True)
        print(f"\n[main] 促单功能启用状态: {promotion_enabled}")
        if not promotion_enabled:
            print("[main] 促单功能未启用,直接返回")
            return {
                "promotion_scripts": [],
                "promotion_scripts_count": 0,
            }

        # 解析输入的对话数据
        dialogue_list = parse_dialogue_data(dialogue)

        # 提取assistant的所有历史回复（客服消息）
        assistant_replies = extract_assistant_replies(dialogue_list)

        # 获取促销话术列表
        promotion_scripts = sop_config.get("promotion_scripts", [])
        print(f"\n[main] 促销话术总数: {len(promotion_scripts)}")

        # 过滤出没有发送过的促销话术
        unsent_scripts = []

        for idx, script in enumerate(promotion_scripts):
            script_content = script.get("content", "")
            print(f"\n[main] 检查第{idx+1}个促销话术:")
            print(f"  话术内容(前50字): {script_content[:50]}..." if len(script_content) > 50 else f"  话术内容: {script_content}")

            if not script_content:
                print("  话术内容为空,跳过")
                continue

            # 检查该话术是否已经发送过（相似度>=90%）
            is_sent = False
            for reply_idx, reply in enumerate(assistant_replies):
                similarity = calculate_similarity(reply, script_content)
                if similarity >= 90:
                    print(f"  与第{reply_idx+1}条历史回复相似度{similarity:.2f}% >= 90%,判定为已发送")
                    is_sent = True
                    break

            # 如果没有发送过，添加到结果列表
            if not is_sent:
                print("  该话术未发送过,添加到结果列表")
                unsent_scripts.append(script)
            else:
                print("  该话术已发送过,跳过")

        # 获取工具列表中的shop_code
        tool_list = start.get("tools", [])
        shop_code = None
        
        # 从工具列表中查找第一个有shop_code的工具
        for tool in tool_list:
            if isinstance(tool, dict) and tool.get("shop_code"):
                shop_code = tool["shop_code"]
                print(f"[配置] 使用shop_code: {shop_code}")
                break
        
         item_ids, id_map = extract_ids_from_dialogue(dialogue, platform)

        # 并行执行所有查询任务
        tasks = [
        ]
        # 添加商品查询任务
        if item_ids:
            tasks.append(fetch_product_and_sku(database_id, item_ids, shop_code, platform))
        
        # 筛选并执行可用工具
        print("\n" + "="*60)
        print("[main] 开始工具筛选与执行流程")
        print("="*60)

        tool_list = start.get("tools", [])
        behavior_action = start.get("sop_config", {}).get("promotion_strategy", "")

        print(f"[main] 原始工具列表数量: {len(tool_list) if tool_list else 0}")
        print(f"[main] promotion_strategy: {behavior_action}")

        if tool_list:
            print("[main] 原始工具列表详情:")
            for idx, t in enumerate(tool_list):
                print(f"  [{idx+1}] {t.get('tool')} (type={t.get('type')}, flow_id={t.get('flow_id')})")

        available_tools = filter_available_tools(tool_list, behavior_action)

        print(f"\n[main] 筛选后可用工具数量: {len(available_tools)}")
        print(f"[main] 可用工具名称: {[t.get('name') for t in available_tools]}")

        print(f"\n[main] 开始执行工具子流程...")
        tool_results = await execute_tool_subflows(available_tools, start, auth)

        print(f"\n[main] 工具执行完成,结果数量: {len(tool_results) if tool_results else 0}")
        if tool_results:
            print("[main] 工具执行结果摘要:")
            for idx, tr in enumerate(tool_results):
                result_preview = str(tr.get('result', ''))[:80]
                has_error = isinstance(tr.get('result'), dict) and 'error' in tr.get('result', {})
                status = "✗ 失败" if has_error else "✓ 成功"
                print(f"  [{idx+1}] {tr.get('tool')} - {status}")
                print(f"      结果预览: {result_preview}{'...' if len(str(tr.get('result', ''))) > 80 else ''}")

        return {
            "promotion_scripts": unsent_scripts,
            "promotion_scripts_count": len(unsent_scripts),
            "tool_results": tool_results,
        }

    except Exception as e:
        print(f"\n[main] 发生异常: {str(e)}")
        import traceback
        print(f"[main] 异常堆栈:\n{traceback.format_exc()}")
        return {
            "error": f"处理失败: {str(e)}",
            "promotion_scripts": [],
            "promotion_scripts_count": 0,
            "tool_results": [],
        }
