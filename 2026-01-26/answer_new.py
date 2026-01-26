from betteryeah import BetterYeah
import json
import requests

better_yeah = BetterYeah()

def update_conversation_state(total_step, cur_step, is_completed):
    try:
        body = {
            "pre_situation": context.get("behavior", {}).get("situation", None),
            "total_step": total_step,
            "cur_step": cur_step,
            "is_completed": is_completed
        }

        requests.post(
            f"https://customer-servhub-api.betteryeah.com/v1/chat/conversation/{conversation_id}/variables",
            json=body
        )
    except Exception:
        print("update_conversation_state报错", 2)
        return


async def main():
    try:

        # 解析上一个节点输出的JSON字符串
        try:
            solution_data = json.loads(solution_new) if isinstance(solution_new, str) else solution_new
        except json.JSONDecodeError as e:
            print(f"[错误] JSON解析失败: {e}")
            return {
                'flow_name': '一般咨询',
                'flow_type': 'GENERAL_QA',
                'debug_message': f'JSON解析错误: {str(e)}',
                'messages': ['人工客服'],
                'answer': '人工客服',
                'thinking': '',
                'product_data': [],
            }

        messages = solution_data.get('messages', [])
        # 展平嵌套列表，确保所有元素都是字符串
        flat_messages = []
        for msg in messages:
            if isinstance(msg, list):
                flat_messages.extend(str(m) for m in msg)
            else:
                flat_messages.append(str(msg))
        messages = flat_messages
        answer = '\n'.join(messages)

        thinking = solution_data.get('thinking', '')

        is_after_sales = solution_data.get('is_after_sales', False)

        total_step = solution_data.get("total_step", None)
        cur_step = solution_data.get("cur_step", None)
        is_completed = solution_data.get("is_completed", None)
        behavior = context.get('behavior', {})

        update_conversation_state(
            total_step=total_step,
            cur_step=cur_step,
            is_completed=is_completed
        )

        return {
            'flow_name': '一般咨询',
            'flow_type': 'GENERAL_QA',
            'debug_message': f'一般咨询\nThinking:\n{thinking}\n\n回答:\n{answer}',
            'messages': messages,
            'behavior': behavior,
            'answer': answer,
            'thinking': thinking,

            'context': context,
            'product_data': context.get("data", []),

            'is_after_sales': is_after_sales,
        }
    except Exception as e:
        print(f"[错误] main执行异常: {e}")
        return {
            'flow_name': '一般咨询',
            'flow_type': 'GENERAL_QA',
            'debug_message': f'执行异常: {str(e)}',
            'messages': ['人工客服'],
            'answer': '人工客服',
            'thinking': '',
            'product_data': [],
        }
