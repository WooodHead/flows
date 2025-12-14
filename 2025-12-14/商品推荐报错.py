from betteryeah import BetterYeah
import json

better_yeah = BetterYeah()

async def main():
    """
    整合数据库和知识库数据
    一次查询获取product和sku数据
    """
    
    database_id = database_config["id"]
    
    category = None
    if isinstance(match, dict):
        category = match.get("category")
    elif isinstance(match, list):
        for item in match:
            if isinstance(item, dict) and item.get("category"):
                category = item.get("category")
                break
    if not category:
        return []
    
    # ========== SQL查询 - 一次性获取product和sku ==========
    # 先查商品
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
    LIMIT 20
    """
    
    try:
        product_res = await better_yeah.database.execute_database(
            base_id=database_id,
            executable_sql=product_sql
        )
        
        if not product_res.success:
            return []
        
        products = product_res.data.data
        
    except Exception as e:
        return []
    
    if not products:
        return []
    
    # 获取所有商品ID
    product_ids = [p.get("商品id") for p in products if isinstance(p, dict) and p.get("商品id")]
    
    if not product_ids:
        return []
    
    # 批量查询SKU
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
    except Exception as e:
        skus = []
    
    # ========== 组装数据 ==========
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
    for product in products:
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
    
    return processed_data
