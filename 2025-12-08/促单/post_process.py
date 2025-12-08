from betteryeah import BetterYeah, Model
import random
better_yeah = BetterYeah()

# 必须保证节点中存在一个main函数
# 你的代码应该在main函数中编写
# main函数的返回值为当前节点的返回值
async def main():
    try:
        # 读取判断结果，检查是否需要发送促单话术
        should_send = judge.get("should_send_promotion", False)

        # 如果不需要发送，返回空消息
        if not should_send:
            return {
                "flow_name": "促单",
                "messages": []
            }

        # 从pre_process中获取未发送的促销话术
        unsent_scripts = pre_process.get("unsent_scripts", [])

        # 如果没有可用的话术，返回空消息
        if not unsent_scripts:
            return {"messages": []}

        # 随机选择一条话术
        selected_script = random.choice(unsent_scripts)
        script_content = selected_script.get("content", "")

        # 返回选中的话术
        if script_content:
            return {
                "flow_name": "促单",
                "messages": [script_content]
            }
        else:
            return {
                "flow_name": "促单",
                "messages": []
            }

    except Exception as e:
        # 出错时返回空消息
        return {
            "flow_name": "促单",
            "messages": []
        }
