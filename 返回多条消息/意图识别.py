from betteryeah import BetterYeah, Model
better_yeah = BetterYeah()

async def main():

    business_messages = business.get("messages", None) if business else None
    business_debug_message = business.get("debug_message") if business else None
    business_thinking = business.get("thinking", None) if business else None
    business_product_data = business.get("product_data") if business else None

    product_messages = product.get("messages", None) if product else None
    product_debug_message = product.get("debug_message") if product else None
    product_thinking = product.get("thinking") if product else None

    search_messages = search.get("messages", None) if search else None
    search_debug_message = search.get("debug_message") if search else None
    search_thinking = search.get("thinking") if search else None

    human_message = ['人工客服'] if human else None
    
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

    return {
        "flow_name": "意图识别",
        "flow_type": "INTENT",
        "messages": business_messages or product_messages or human_message or search_messages or [],
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
