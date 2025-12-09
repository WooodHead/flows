from betteryeah import BetterYeah
import json
import asyncio

better_yeah = BetterYeah()

async def fetch_products_by_entity(database_id, entity):
    """
    根据单个实体查询商品(模糊匹配商品标题)
    """
    if not entity:
        return []
    
    # 模糊匹配: 商品标题
    product_sql = f"""
    SELECT 
        商品id, 商品标题, 商品链接, 参数, 商品详情页识别结果, 
        轮播图识别结果, 卖点, 补充知识
    FROM 店铺商品目录
    WHERE 商品标题 LIKE '%{entity}%'
    LIMIT 100
    """
    
    try:
        product_res = await better_yeah.database.execute_database(
            base_id=database_id,
            executable_sql=product_sql
        )
        
        if product_res.success and hasattr(product_res.data, 'data'):
            products = product_res.data.data
            return products if products else []
        
    except Exception as e:
        print(f"[错误] 实体'{entity}'查询失败: {str(e)}")
        import traceback
        print(f"[错误详情] {traceback.format_exc()}")
    
    return []

async def main():
    """
    根据entities数组并发查询商品
    模糊匹配: 商品标题
    """
    
    # 获取参数
    database_id = database_config["id"]
    entities_raw = extract.get("entities", [])
    
    # 提取value字段
    entities = []
    for item in entities_raw:
        if isinstance(item, dict):
            value = item.get("value")
            if value:
                entities.append(value)
        elif isinstance(item, str):
            entities.append(item)
    
    if not entities:
        print("[提示] entities为空")
        return []
    
    print(f"[提取] 实体:{entities}")
    
    # ========== 1. 并发查询所有实体 ==========
    tasks = [fetch_products_by_entity(database_id, entity) for entity in entities]
    results = await asyncio.gather(*tasks)
    
    # 合并所有结果
    all_products = []
    for products in results:
        if products:
            all_products.extend(products)
    
    if not all_products:
        print("[提示] 未匹配到商品")
        return []
    
    print(f"[数据] 实体匹配:{len(all_products)}个(去重前)")
    
    # ========== 2. 去重(基于商品ID) ==========
    seen_ids = set()
    unique_products = []
    for p in all_products:
        if isinstance(p, dict):
            item_id = p.get("商品id")
            if item_id and item_id not in seen_ids:
                seen_ids.add(item_id)
                unique_products.append(p)
    
    print(f"[数据] 去重后:{len(unique_products)}个")
    
    # ========== 3. 批量查询SKU ==========
    product_ids = [p.get("商品id") for p in unique_products]
    
    if product_ids:
        ids_str = "','".join(str(pid) for pid in product_ids)
        sku_sql = f"""
        SELECT 商品id, sku, sku图识别结果
        FROM sku参数表
        WHERE 商品id IN ('{ids_str}')
        LIMIT 100
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
            print(f"[错误] 查询SKU失败: {str(e)}")
            import traceback
            print(f"[错误详情] {traceback.format_exc()}")
            skus = []
    else:
        skus = []
    
    # ========== 4. 组装数据 ==========
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
            except Exception as e:
                print(f"[错误] 处理商品详情页识别结果失败(商品ID:{item_id}): {str(e)}")
                import traceback
                print(f"[错误详情] {traceback.format_exc()}")
        
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
            except Exception as e:
                print(f"[错误] 处理轮播图识别结果失败(商品ID:{item_id}): {str(e)}")
                import traceback
                print(f"[错误详情] {traceback.format_exc()}")
        
        processed_data.append(processed_item)
    
    print(f"[完成] 返回商品:{len(processed_data)}个")
    
    return processed_data
