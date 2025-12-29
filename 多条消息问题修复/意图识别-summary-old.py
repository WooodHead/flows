import re
from betteryeah import BetterYeah, Model
better_yeah = BetterYeah()

async def main():

    business_messages = business.get("messages", None) if business else None
    business_debug_message = business.get("debug_message") if business else None
    business_thinking = business.get("thinking", None) if business else None
    business_product_data = business.get("product_data") if business else None
    business_answer = business.get("answer", '') if business else None
    business_forward_group_type = business.get("forward_group_type", '') if business else None

    product_messages = custom_product.get("messages") if custom_product else (product.get("messages") if product else [])
    product_debug_message = custom_product.get("debug_message") if custom_product else (product.get("debug_message") if product else None)
    product_thinking = custom_product.get("thinking") if custom_product else (product.get("thinking") if product else None)
    product_answer = product.get("answer", '') if product else None

    search_messages = search.get("messages", None) if search else None
    search_debug_message = search.get("debug_message") if search else None
    search_thinking = search.get("thinking") if search else None
    search_answer = search.get("answer", '') if search else None

    human_message = ['人工客服'] if human else None
    human_answer = '人工客服' if human else None

    event_one = judge.get("event_one") if judge else None
    event_two = judge.get("event_two") if judge else None
    judge_thinking = judge.get("thinking") if judge else None
    judge_emotion = judge.get("emotion") if judge else None

    debug_message = f"""意图识别:
一级: {event_one or '无'}
二级: {event_two or '无'}

意图识别 Thinking:
{judge_thinking or '无思考过程'}
"""

    debug_message = f"{debug_message}\n{business_debug_message or product_debug_message or search_debug_message or ''}"

    answer = business_answer or product_answer or search_answer or human_answer or ''

    forbidden_words = customer_config.get("forbidden_words", [])

    # 遍历违禁词列表，将answer中的违禁词替换为对应数量的·(忽略大小写)
    for word in forbidden_words:
        if word:
            # 使用正则表达式进行大小写不敏感的替换
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            answer = pattern.sub(lambda m: '·' * len(m.group()), answer)

    # 按换行拆分成列表
    answer_messages = answer.splitlines()
    # 替换转人工标记TRANSFER为“人工客服”
    processed_messages = [
        '人工客服' if 'TRANSFER' in message else message
        for message in answer_messages
    ]

    return {
        "flow_name": "意图识别",
        "flow_type": "INTENT",

        "messages": processed_messages or product_messages,
        "forward_group_type": business_forward_group_type,

        "debug_message": debug_message.strip(),
        "event_one": event_one,
        "event_two": event_two,
        "event_two_transfer_human": True if human else False,
        "intent_thinking": judge_thinking,
        "general_qa_thinking": business_thinking,
        "recommend_thinking": product_thinking,
        "search_thinking": search_thinking,
        "emotion": judge_emotion,
        "product_data": business_product_data,
        "context_infos": [
            *context_infos,
            *preprocess["images"],
        ]
    }
