from betteryeah import BetterYeah
import json
import re

better_yeah = BetterYeah()

def extract_product_codes_from_dialogue(dialogue_data):
    """
    从对话中提取货号/款号(字母+数字组合)
    支持格式: dw2415, ABC123, 845680, M123-456等
    """
    codes = []
    
    for message in dialogue_data:
        if not message or not isinstance(message, dict):
            continue
        
        if message.get("role") not in ["user", "assistant"]:
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
        
        # 匹配货号模式(支持中文环境)
        matches = re.findall(r'([a-zA-Z0-9][-_a-zA-Z0-9]{2,})', text)
        
        for code in matches:
            # 过滤纯字母(可能是普通单词)
            if not re.search(r'\d', code):
                continue
            # 过滤纯数字且长度<4(可能是数量)
            if code.isdigit() and len(code) < 4:
                continue
            # 去重
            if code not in codes:
                codes.append(code)
    
    return codes

async def fetch_products_by_codes(database_id, product_codes):
    """
    根据货号模糊匹配商品
    """
    if not product_codes:
        return []
    
    # 构建LIKE查询条件
    like_conditions = " OR ".join([f"商品标题 LIKE '%{code}%'" for code in product_codes])
    
    product_sql = f"""
    SELECT 
        商品id, 商品标题, 商品链接, 参数, 商品详情页识别结果, 
        轮播图识别结果, 卖点, 补充知识
    FROM 店铺商品目录
    WHERE {like_conditions}
    LIMIT 20
    """
    
    try:
        product_res = await better_yeah.database.execute_database(
            base_id=database_id,
            executable_sql=product_sql
        )
        
        if product_res.success and hasattr(product_res.data, 'data'):
            products = product_res.data.data
            if products:
                print(f"[数据] 货号匹配:{len(products)}个")
            return products
        
    except Exception as e:
        print(f"[错误] 货号查询失败: {str(e)}")
    
    return []

async def main():
    """
    整合数据库和知识库数据
    支持: 1.货号查询(优先) 2.品类推荐(补充)
    """
    
    # 获取参数
    database_id = database_config["id"]
    category = match.get("category", "")
    
    all_products = []
    
    # ========== 1. 货号查询(优先) ==========
    product_codes = extract_product_codes_from_dialogue(dialogue)
    
    if product_codes:
        print(f"[提取] 货号:{len(product_codes)}个")
        products_by_code = await fetch_products_by_codes(database_id, product_codes)
        all_products.extend(products_by_code)
    
    # ========== 2. 品类推荐(补充) ==========
    if category and len(all_products) < 20:
        limit = 20 - len(all_products)
        
        product_sql = f"""
        SELECT 
            商品id, 商品标题, 商品链接, 参数, 商品详情页识别结果, 
            轮播图识别结果, 卖点, 补充知识
        FROM (
          SELECT
            商品id, 商品标题, 商品链接, 参数, 商品详情页识别结果, 
            轮播图识别结果, 卖点, 补充知识,
            ROW_NUMBER() OVER (PARTITION BY 商品id ORDER BY id) AS rn,
            CASE WHEN 是否主推 = '是' THEN 1 ELSE 2 END AS priority
          FROM 店铺商品目录
          WHERE 商品品类 LIKE '%{category}%'
        ) t
        WHERE rn = 1
        ORDER BY priority ASC, RANDOM()
        LIMIT {limit}
        """
        
        try:
            product_res = await better_yeah.database.execute_database(
                base_id=database_id,
                executable_sql=product_sql
            )
            
            if product_res.success and hasattr(product_res.data, 'data'):
                products = product_res.data.data
                all_products.extend(products)
                print(f"[数据] 品类推荐:{len(products)}个")
        
        except Exception as e:
            print(f"[错误] 品类查询失败: {str(e)}")
    
    if not all_products:
        return []
    
    # ========== 3. 去重(基于商品ID) ==========
    seen_ids = set()
    unique_products = []
    for p in all_products:
        if isinstance(p, dict):
            item_id = p.get("商品id")
            if item_id and item_id not in seen_ids:
                seen_ids.add(item_id)
                unique_products.append(p)
    
    # ========== 4. 批量查询SKU ==========
    product_ids = [p.get("商品id") for p in unique_products]
    
    if product_ids:
        ids_str = "','".join(str(pid) for pid in product_ids)
        sku_sql = f"""
        SELECT 商品id, sku, sku图识别结果
        FROM sku参数表
        WHERE 商品id IN ('{ids_str}')
        """
        
        try:
            sku_res = await better_yeah.database.execute_database(
                base_id=database_id,
                executable_sql=sku_sql
            )
            
            if sku_res.success:
                skus = sku_res.data.data
            else:
                skus = []
        except:
            skus = []
    else:
        skus = []
    
    # ========== 5. 组装数据 ==========
    # 按商品ID分组SKU
    sku_map = {}
    for sku in skus:
        if not isinstance(sku, dict):
            continue
        item_id = sku.get("商品id")
        if item_id:
            if item_id not in sku_map:
                sku_map[item_id] = []
            sku_map[item_id].append({
                "sku": sku.get("sku", ""),
                "sku图识别结果": sku.get("sku图识别结果", "")
            })
    
    # 组装最终结果
    processed_data = []
    for product in unique_products:
        if not isinstance(product, dict):
            continue
            
        item_id = product.get("商品id", "")
        
        processed_item = {
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
        
        # 处理商品详情页识别结果 - 去掉url
        detail_result = product.get("商品详情页识别结果", "")
        if detail_result:
            try:
                detail_list = json.loads(detail_result) if isinstance(detail_result, str) else detail_result
                if isinstance(detail_list, list):
                    for detail_item in detail_list:
                        if isinstance(detail_item, dict):
                            desc_dict = {k: v for k, v in detail_item.items() if k.startswith("image_desc")}
                            if desc_dict:
                                processed_item["商品详情页识别结果"].append(desc_dict)
            except:
                pass
        
        # 处理轮播图识别结果 - 去掉url
        carousel_result = product.get("轮播图识别结果", "")
        if carousel_result:
            try:
                carousel_list = json.loads(carousel_result) if isinstance(carousel_result, str) else carousel_result
                if isinstance(carousel_list, list):
                    for carousel_item in carousel_list:
                        if isinstance(carousel_item, dict):
                            desc_dict = {k: v for k, v in carousel_item.items() if k.startswith("image_desc")}
                            if desc_dict:
                                processed_item["轮播图识别结果"].append(desc_dict)
            except:
                pass
        
        processed_data.append(processed_item)
    
    print(f"[完成] 返回商品:{len(processed_data)}个")
    
    return processed_data
