from betteryeah import BetterYeah
better_yeah = BetterYeah()

# 必须保证节点中存在一个main函数
# 你的代码应该在main函数中编写
# main函数的返回值为当前节点的返回值
async def main():
    dialogue = better_yeah.get("dialogue", [])

    # 读取最后一条消息
    if not dialogue:
        return {"should_send_invite": False}

    last_message = dialogue[-1]
    last_role = last_message.get("role", "")

    # 如果最后一条消息是用户发送的，返回 False
    # 如果最后一条消息是客服发送的，返回 True
    should_send_invite = last_role == "assistant"

    return {"should_send_invite": should_send_invite}
