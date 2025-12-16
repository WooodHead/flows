from betteryeah import BetterYeah, Model
import json

better_yeah = BetterYeah()

async def main():
    # 解析上一个节点输出的JSON字符串
    try:
        solution_data = json.loads(solution) if isinstance(solution, str) else solution
    except json.JSONDecodeError as e:
        print(f"[错误] JSON解析失败: {e}")
        return {
            'flow_name': '一般咨询',
            'flow_type': 'GENERAL_QA',
            'debug_message': f'JSON解析错误: {str(e)}',
            'messages': ['人工客服'],
            'thinking': '',
            'product_data': [],
        }
    
    thinking = solution_data.get('thinking', '')
    answer = solution_data.get('answer', '')
    answer_messages = answer.splitlines()
    processed_messages = [
        '人工客服' if 'TRANSFER' in message else message
        for message in answer_messages
    ]
    
    # 判断是否需要转人工
    if '[TRANSFER]' in answer:
        return {
            'flow_name': '一般咨询',
            'flow_type': 'GENERAL_QA',
            'debug_message': f'一般咨询\nThinking:\n{thinking}\n\n回答:\n人工客服',
            'messages': ['人工客服'],
            'thinking': thinking,
            'product_data': context.get("data", []),
        }
    else:
        return {
            'flow_name': '一般咨询',
            'flow_type': 'GENERAL_QA',
            'debug_message': f'一般咨询\nThinking:\n{thinking}\n\n回答:\n{answer}',
            'messages': processed_messages,
            'thinking': thinking,
            'product_data': context.get("data", []),
        }
