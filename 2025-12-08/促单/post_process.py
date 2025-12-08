from betteryeah import BetterYeah, Model
import random
better_yeah = BetterYeah()

# 必须保证节点中存在一个main函数
# 你的代码应该在main函数中编写
# main函数的返回值为当前节点的返回值
async def main():
    try:
        if pre_process.get("promotion_scripts_count", 0) == 0:
            return {
                "flow_name": "促单",
                "messages": []
            }

        # 读取判断结果，检查是否需要发送促单话术
        should_send = judge.get("should_send_promotion", False)

        # 如果不需要发送，返回空消息
        if not should_send:
            return {
                "flow_name": "促单",
                "messages": []
            }

        # 从pre_process中获取未发送的促销话术
        promotion_scripts = pre_process.get("promotion_scripts", [])

        # 如果没有可用的话术，返回空消息
        if not promotion_scripts:
            return {"messages": []}

        # 随机选择一条话术
        selected_script = random.choice(promotion_scripts)
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
        # 打印错误信息
        print(f"Error in post_process: {str(e)}")
        print(f"Exception type: {type(e).__name__}")
        import traceback
        traceback.print_exc()

        # 出错时返回空消息
        return {
            "flow_name": "促单",
            "messages": []
        }
