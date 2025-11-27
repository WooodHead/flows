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
    """解析淘宝短链获取商品ID"""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        resp = requests.get(url, headers=headers, timeout=5)
        if resp.status_code == 200:
            html = resp.text
            match = re.search(r"var\s+url\s*=\s*['\"]([^'\"]+)['\"]", html)
            if match:
                long_url = match.group(1)
                id_match = re.search(r'[?&]id=(\d+)', long_url)
                if id_match:
                    return id_match.group(1)
    except Exception as e:
        print(f"[警告] 解析短链失败 {url}: {e}")
    return None

def extract_ids_from_dialogue(dialogue_data):
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
            
        # 提取短链并解析
        short_links = re.findall(r'https?://e\.tb\.cn/[A-Za-z0-9._]+', combined_text)
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

def extract_product_codes_from_dialogue(dialogue_data):
    """
    从对话中提取货号/款号(字母+数字组合)
    支持格式: dw2415, ABC123, 845680, M123-456等
    """
    codes = []
    
    print(f"[调试] dialogue_data类型: {type(dialogue_data)}, 长度: {len(dialogue_data) if dialogue_data else 0}")
    
    for idx, message in enumerate(dialogue_data):
        if not message or not isinstance(message, dict):
            continue
        
        role = message.get("role")
        if role not in ["user", "assistant"]:
            continue
            
        content = message.get("content")
        if not content:
            continue
        
        # 提取文本
        if isinstance(content, str):
            text = content
        elif isinstance(content, dict):
            text = content.get('text', '')
        else:
            continue
        
        print(f"[调试] 消息{idx} role={role}, text={text[:50]}...")
        
        # 匹配货号模式: 
        # - 至少3个字符
        # - 包含字母或数字(可混合)
        # - 可包含中划线/下划线
        # 示例: dw2415, ABC123, 845680, M123-456, style_2024
        # 注意: 不使用\b边界,因为中文环境下可能失效
        matches = re.findall(r'([a-zA-Z0-9][-_a-zA-Z0-9]{2,})', text)
        
        print(f"[调试] 正则匹配到: {matches}")
        
        for code in matches:
            # 过滤纯字母(可能是普通单词)
            if not re.search(r'\d', code):
                print(f"[调试] 过滤{code}: 纯字母")
                continue
            # 过滤纯数字且长度<4(可能是数量)
            if code.isdigit() and len(code) < 4:
                print(f"[调试] 过滤{code}: 数字太短")
                continue
            # 去重
            if code not in codes:
                print(f"[调试] ✅ 保留货号: {code}")
                codes.append(code)
    
    return codes

async def fetch_product_by_codes(database_id, product_codes):
    """
    根据货号模糊匹配商品
    支持: dw2415, ABC123等
    """
    if not product_codes:
        return []
    
    # 构建LIKE查询条件
    like_conditions = " OR ".join([f"商品标题 LIKE '%{code}%'" for code in product_codes])
    
    try:
        product_res = await better_yeah.database.execute_database(
            base_id=database_id,
            executable_sql=f"""
                SELECT 商品id, 商品标题, 商品链接, 参数, 
                       商品详情页识别结果, 轮播图识别结果, 卖点, 补充知识 
                FROM 店铺商品目录 
                WHERE {like_conditions}
                LIMIT 50
            """
        )
        products = product_res.data.data if product_res.success and hasattr(product_res.data, 'data') else []
        
        if products:
            print(f"[数据] 货号匹配到商品:{len(products)}个")
        
        return products
    except Exception as e:
        print(f"[错误] 货号查询失败: {str(e)}")
        return []

async def fetch_product_and_sku(database_id, item_ids):
    """根据商品ID查询商品和SKU"""
    if not item_ids:
        return []
    
    ids_str = "','".join(str(pid) for pid in item_ids)
    
    try:
        product_res = await better_yeah.database.execute_database(
            base_id=database_id,
            executable_sql=f"SELECT 商品id, 商品标题, 商品链接, 参数, 商品详情页识别结果, 轮播图识别结果, 卖点, 补充知识 FROM 店铺商品目录 WHERE 商品id IN ('{ids_str}') LIMIT 100"
        )
        products = product_res.data.data if product_res.success and hasattr(product_res.data, 'data') else []
    except:
        return []
    
    if not products:
        return []
    
    try:
        sku_res = await better_yeah.database.execute_database(
            base_id=database_id,
            executable_sql=f"SELECT 商品id, sku, sku图识别结果 FROM sku参数表 WHERE 商品id IN ('{ids_str}') LIMIT 500"
        )
        skus = sku_res.data.data if sku_res.success and hasattr(sku_res.data, 'data') else []
    except:
        skus = []
    
    sku_map = {}
    for sku in skus:
        if isinstance(sku, dict) and sku.get("商品id"):
            sku_map.setdefault(sku["商品id"], []).append({
                "sku": sku.get("sku", ""),
                "sku图识别结果": sku.get("sku图识别结果", "")
            })
    
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
            "sku": sku_map.get(item_id, [])
        }
        
        for field in ["商品详情页识别结果", "轮播图识别结果"]:
            raw = product.get(field, "")
            if raw:
                try:
                    items = json.loads(raw) if isinstance(raw, str) else raw
                    if isinstance(items, list):
                        for item in items:
                            if isinstance(item, dict):
                                desc = {k: v for k, v in item.items() if k.startswith("image_desc")}
                                if desc:
                                    processed[field].append(desc)
                except:
                    pass
        result.append(processed)
    
    print(f"[数据] 商品ID查询:{len(result)}个 SKU:{len(skus)}")
    return result

async def process_product_data(database_id, products_by_code):
    """
    处理货号查询到的商品,补充SKU信息
    """
    if not products_by_code:
        return []
    
    # 提取所有商品ID
    item_ids = [p.get("商品id") for p in products_by_code if p.get("商品id")]
    
    if not item_ids:
        return []
    
    ids_str = "','".join(str(pid) for pid in item_ids)
    
    # 查询SKU
    try:
        sku_res = await better_yeah.database.execute_database(
            base_id=database_id,
            executable_sql=f"SELECT 商品id, sku, sku图识别结果 FROM sku参数表 WHERE 商品id IN ('{ids_str}') LIMIT 500"
        )
        skus = sku_res.data.data if sku_res.success and hasattr(sku_res.data, 'data') else []
    except:
        skus = []
    
    # 构建SKU映射
    sku_map = {}
    for sku in skus:
        if isinstance(sku, dict) and sku.get("商品id"):
            sku_map.setdefault(sku["商品id"], []).append({
                "sku": sku.get("sku", ""),
                "sku图识别结果": sku.get("sku图识别结果", "")
            })
    
    # 处理商品数据
    result = []
    for product in products_by_code:
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
            "sku": sku_map.get(item_id, []),
            "匹配方式": "货号模糊匹配",  # 标记匹配方式
            "short_link": ""  # 初始化短链字段
        }
        
        for field in ["商品详情页识别结果", "轮播图识别结果"]:
            raw = product.get(field, "")
            if raw:
                try:
                    items = json.loads(raw) if isinstance(raw, str) else raw
                    if isinstance(items, list):
                        for item in items:
                            if isinstance(item, dict):
                                desc = {k: v for k, v in item.items() if k.startswith("image_desc")}
                                if desc:
                                    processed[field].append(desc)
                except:
                    pass
        result.append(processed)
    
    return result

async def fetch_behavior(database_id, top_situations):
    """
    根据 top_situations 查询场景策略，结果按 top_situations 顺序排序
    """
    
    if not top_situations:
        print(f"[fetch_behavior] top_situations为空，返回空列表")
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

async def main():
    database_id = database_config["id"]
    auth = start.get("auth", {})
    kb_config = start.get("knowledge_base_config", {})
    messages = start.get("messages", [])
    
    # 检查数组长度
    if len(messages) >= 2:
        # 取数组的最后两个元素
        latest_messages = messages[-2:]
    else:
        # 如果元素少于两个，直接返回整个数组
        latest_messages = messages[:]
    
    start_time = datetime.now()
    
    # 提取商品ID和货号
    item_ids, id_map = extract_ids_from_dialogue(dialogue)
    product_codes = extract_product_codes_from_dialogue(dialogue)
    
    print(f"[提取] 商品ID:{item_ids} | 货号:{product_codes}")
    
    # 并行执行所有查询任务
    tasks = [
        fetch_behavior(database_id, top_situations),
        asyncio.get_event_loop().run_in_executor(
            None, 
            fetch_knowledge_base_batch, 
            auth, kb_config, kb_config.get("common_partition_id", ""), messages, "common"
        ),
        asyncio.get_event_loop().run_in_executor(
            None,
            fetch_knowledge_base_batch,
            auth, kb_config, kb_config.get("faq_partition_id", ""), latest_messages, "faq"
        )
    ]
    
    # 添加商品查询任务
    if item_ids:
        tasks.append(fetch_product_and_sku(database_id, item_ids))
    
    if product_codes:
        tasks.append(fetch_product_by_codes(database_id, product_codes))
    
    # 执行所有任务
    results = await asyncio.gather(*tasks)
    
    # 解析结果
    behavior_result = results[0]
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
    
    if product_codes:
        # 如果有货号查询结果
        code_result_idx = 4 if item_ids else 3
        if len(results) > code_result_idx:
            products_by_code = results[code_result_idx]
            # 处理货号查询到的商品,补充SKU
            processed = await process_product_data(database_id, products_by_code)
            product_sku_result.extend(processed)
    
    # 去重商品(基于商品id)
    seen_product_ids = set()
    unique_products = []
    for product in product_sku_result:
        product_id = product.get("商品id")
        if product_id and product_id not in seen_product_ids:
            seen_product_ids.add(product_id)
            unique_products.append(product)
    
    # 处理知识库结果
    processed_common = [item.get("content", "") for item in common_result if isinstance(item, dict) and item.get("content")]
    processed_faq = [{"question": item.get("content", ""), "answer": item.get("extra_info", {})} for item in faq_result if isinstance(item, dict) and (item.get("content") or item.get("extra_info"))]
    
    elapsed = (datetime.now() - start_time).total_seconds()
    print(f"[完成] 商品{len(unique_products)}个 | 策略{len(behavior_result)}条 | common{len(processed_common)}条 | faq{len(processed_faq)}条 | 总耗时{elapsed:.2f}秒")
    
    return {
        "data": unique_products,
        "behavior": behavior_result,
        "common": processed_common,
        "faq": processed_faq,
        "current_time": get_current_datetime()
    }
