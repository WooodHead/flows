from betteryeah import BetterYeah
import json

better_yeah = BetterYeah()

async def main():
    messages_array = extract_user_messages()
    image_results = await process_image()
    tags_data = await query_tags()
    
    # 获取最后一个元素
    latest_message = messages_array[-1] if messages_array else ""
    
    return {
        "messages": messages_array,
        "latest_message": latest_message,  # 最后一个元素(字符串)
        "images": image_results,
        "tags": tags_data
    }


import re

def extract_user_messages():
    """
    以 assistant 消息为分隔符切割对话
    - 第一个 assistant 之前的 user 消息 -> 第1个元素
    - 第一个和第二个 assistant 之间的 user 消息 -> 第2个元素
    - 第二个和第三个 assistant 之间的 user 消息 -> 第3个元素
    - 最后一个 assistant 之后的 user 消息 -> 最后一个元素
    
    返回格式: ["user1 user2", "user3 user4", "user5"]
    注意: 会过滤掉空字符串,只返回有实际内容的消息
    """
    try:
        dialogue_list = json.loads(dialogue) if isinstance(dialogue, str) else dialogue
        
        # 找到所有 assistant 消息的索引位置
        assistant_indices = []
        for i, msg in enumerate(dialogue_list):
            if msg.get("role") == "assistant":
                assistant_indices.append(i)
        
        # 如果没有 assistant 消息，返回所有 user 消息作为一段
        if not assistant_indices:
            all_user_texts = []
            for msg in dialogue_list:
                if msg.get("role") == "user":
                    text = extract_text_from_message(msg)
                    if text:
                        all_user_texts.append(text)
            return [" ".join(all_user_texts)] if all_user_texts else []
        
        result = []
        
        # 处理每个区间
        # 区间0: 从开头到第一个 assistant
        # 区间1: 第一个 assistant 到第二个 assistant
        # ...
        # 区间n: 最后一个 assistant 到结尾
        
        for idx in range(len(assistant_indices) + 1):
            if idx == 0:
                # 第一个 assistant 之前
                start_idx = 0
                end_idx = assistant_indices[0]
            elif idx == len(assistant_indices):
                # 最后一个 assistant 之后
                start_idx = assistant_indices[-1] + 1
                end_idx = len(dialogue_list)
            else:
                # 两个 assistant 之间
                start_idx = assistant_indices[idx - 1] + 1
                end_idx = assistant_indices[idx]
            
            # 收集该区间内的所有 user 消息
            user_texts = []
            for i in range(start_idx, end_idx):
                if dialogue_list[i].get("role") == "user":
                    text = extract_text_from_message(dialogue_list[i])
                    if text:
                        user_texts.append(text)
            
            # 只有当该区间有 user 消息时才加入结果
            if user_texts:
                result.append(" ".join(user_texts))
        
        return result
    except Exception as e:
        return []


def extract_text_from_message(msg):
    """从消息中提取文本并清理"""
    content = msg.get("content", {})
    text = content.get("text", "") if isinstance(content, dict) else str(content)
    if text:
        # 清理文本：去掉"月销"及之后的内容
        text = re.sub(r'\s*月销.*$', '', text).strip()
        text = re.sub(r'\s*已售.*$', '', text).strip()
        text = re.sub(r'\s*当前用户来自.*$', '', text).strip()

    return text




import asyncio

async def process_image():
    """提取并识别所有用户图片，并行处理减少耗时"""
    try:
        data = dialogue if isinstance(dialogue, list) else json.loads(dialogue) if isinstance(dialogue, str) else [dialogue]
        if isinstance(data, dict):
            data = [data]
        
        # 收集所有图片信息
        image_tasks = []
        
        for message in data:
            if message and message.get("role") == "user":
                content = message.get("content", {})
                if isinstance(content, dict):
                    image = content.get("image", "").strip()
                    if image:
                        if image.startswith("http://"):
                            image = "https://" + image[7:]
                        timestamp = message.get("send_time", message.get("timestamp", ""))
                        image_tasks.append((image, timestamp))
        
        if not image_tasks:
            return []
        
        # 并行识别所有图片
        async def recognize_single(url, timestamp):
            prompt = "识别顾客发送的图片中的内容，包括所有关键特征。简洁描述，重点突出要点。"
            try:
                resp = await better_yeah.plugin.image.vision(url, prompt, model="grok-4-fast-non-reasoning")
                recognition = resp.data if resp.success else ""
            except:
                recognition = ""
            return {
                "image_send_time": timestamp,
                "image_content": recognition
            }
        
        # 并行执行所有识别任务
        results = await asyncio.gather(*[recognize_single(url, ts) for url, ts in image_tasks])
        return list(results)
    except:
        return []


async def query_tags():
    """
    查询标签表，返回一级分类及其二级分类（含描述和场景策略）
    不包含转人工字段
    """
    try:
        database_id = database_config["id"]
        
        # 查询固定标签表
        sql = "SELECT 事件一级, 事件二级, 事件描述 FROM 固定标签表 WHERE 事件一级 IS NOT NULL LIMIT 500;"
        
        res = await better_yeah.database.execute_database(
            base_id=database_id,
            executable_sql=sql
        )
        
        if not res.success:
            raise Exception(res.message)
        
        # 查询场景策略表
        situation_sql = "SELECT 事件一级标签, 事件二级标签, situation FROM 场景策略表 LIMIT 500;"
        
        situation_res = await better_yeah.database.execute_database(
            base_id=database_id,
            executable_sql=situation_sql
        )
        
        # 构建场景策略映射: {(事件一级标签, 事件二级标签): [situation1, situation2, ...]}
        situation_map = {}
        if situation_res.success:
            for row in situation_res.data.data:
                event_one = row.get("事件一级标签", "")
                event_two = row.get("事件二级标签", "")
                situation = row.get("situation", "")
                
                if event_one and event_two and situation:
                    key = (event_one, event_two)
                    if key not in situation_map:
                        situation_map[key] = []
                    if situation not in situation_map[key]:
                        situation_map[key].append(situation)
        
        # 先按事件一级分组收集二级数据
        grouped = {}
        
        for row in res.data.data:
            event_one = row.get("事件一级", "")
            event_two = row.get("事件二级")
            desc = row.get("事件描述")
            
            if not event_one:
                continue
                
            if event_one not in grouped:
                grouped[event_one] = []
            
            if event_two:
                exists = any(item["名称"] == event_two for item in grouped[event_one])
                if not exists:
                    item = {"名称": event_two}
                    if desc:
                        item["描述"] = desc
                    # 添加场景策略 situations
                    situations = situation_map.get((event_one, event_two), [])
                    if situations:
                        item["situations"] = situations
                    grouped[event_one].append(item)
        
        # 转换为最终格式
        result = []
        for event_one, items in grouped.items():
            result.append({
                "事件一级": event_one,
                "包含的事件二级": items
            })
        
        return result
    except Exception as e:
        return []
