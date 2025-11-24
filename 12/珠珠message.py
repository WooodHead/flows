from betteryeah import BetterYeah
import json

better_yeah = BetterYeah()

async def main():
    """
    从dialogue变量中提取最后一条assistant消息之后的所有user消息
    返回: str，多条消息用空格隔开
    """
    
    # 将字符串解析为列表
    dialogue_list = json.loads(dialogue) if isinstance(dialogue, str) else dialogue

    user_messages = []
    found_last_assistant = False

    # 从后往前遍历，找到最后一条assistant消息
    for i in range(len(dialogue_list) - 1, -1, -1):
        msg = dialogue_list[i]
        role = msg.get("role")
        
        if role == "assistant":
            found_last_assistant = True
            # 从这条assistant消息之后开始收集user消息
            for j in range(i + 1, len(dialogue_list)):
                user_msg = dialogue_list[j]
                if user_msg.get("role") == "user":
                    content = user_msg.get("content", {})
                    text = content.get("text", "") if isinstance(content, dict) else str(content)
                    if text:
                        user_messages.append(text)
            break
    
    # 如果没有找到assistant消息，则收集所有user消息
    if not found_last_assistant:
        for msg in dialogue_list:
            if msg.get("role") == "user":
                content = msg.get("content", {})
                text = content.get("text", "") if isinstance(content, dict) else str(content)
                if text:
                    user_messages.append(text)
    
    return " ".join(user_messages)
