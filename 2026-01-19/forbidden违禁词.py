import re
from betteryeah import BetterYeah
better_yeah = BetterYeah()

async def main():

    business_messages = business.get("messages", None) if business else None
    business_debug_message = business.get("debug_message") if business else None
    business_thinking = business.get("thinking", None) if business else None
    business_product_data = business.get("product_data") if business else None
    business_forward_group_type = business.get("forward_group_type", '') if business else None

    business_context = business.get("context", None) if business else None

    product_messages = custom_product.get("messages") if custom_product else (product.get("messages") if product else [])
    product_debug_message = custom_product.get("debug_message") if custom_product else (product.get("debug_message") if product else None)
    product_thinking = custom_product.get("thinking") if custom_product else (product.get("thinking") if product else None)

    search_messages = search.get("messages", None) if search else None
    search_debug_message = search.get("debug_message") if search else None
    search_thinking = search.get("thinking") if search else None

    event_two_transfer_human_messages = ['人工客服'] if event_two_transfer_human else None
    situation_transfer_human_messages = ['人工客服'] if situation_transfer_human else None

    event_one = judge.get("event_one") if judge else None
    event_two = judge.get("event_two") if judge else None

    behavior = business.get("behavior", {}) if business else None

    quality_inspection = judge.get("quality_inspection", {}) if judge else None
    judge_thinking = judge.get("thinking") if judge else None
    judge_emotion = judge.get("emotion") if judge else None
    judge_top_situation = judge.get("top_situation") if judge else None

    debug_message = f"""意图识别:
一级: {event_one or '无'}
二级: {event_two or '无'}

意图识别 Thinking:
{judge_thinking or '无思考过程'}
"""

    debug_message = f"{debug_message}\n{business_debug_message or product_debug_message or search_debug_message or ''}"

    forbidden_words = customer_config.get("forbidden_words", [])

    messages = business_messages or product_messages or search_messages or event_two_transfer_human_messages or situation_transfer_human_messages or []

    # 检查消息是否包含违禁词
    def contains_forbidden_word(text, words):
        for word in words:
            if word and re.search(re.escape(word), text, re.IGNORECASE):
                return True
        return False

    # 调用大模型改写去除违禁词
    async def rewrite_without_forbidden_words(text, words):
        forbidden_list = ", ".join([w for w in words if w])
        system_prompt = f"""<role>你是一个文本改写助手</role>

<task>改写用户提供的文本，去除其中的违禁词，但保持原意不变</task>

<forbidden_words>
{forbidden_list}
</forbidden_words>

<requirements>
1. 改写后的文本不能包含上述任何违禁词
2. 把存在的违禁词替换为相似的词语或表达方式
3. 保持原文的语义和语气
4. 只输出改写后的文本，不要有任何解释或说明
</requirements>

<user_input>
{text}
</user_input>
"""
        print("system_prompt", system_prompt)
        print("text", text)
        res = await better_yeah.llm.chat(
            system_prompt=system_prompt,
            model="qwen3-vl-flash"
        )
        if not res.success:
            # 如果大模型调用失败，回退到替换为·的方式
            for word in words:
                if word:
                    pattern = re.compile(re.escape(word), re.IGNORECASE)
                    text = pattern.sub(lambda m: '·' * len(m.group()), text)
            return text
        rewrite_result = res.data.strip()

        print("rewrite_result", rewrite_result)
        return rewrite_result

    # 替换转人工标记TRANSFER为"人工客服"，并去除违禁词
    processed_messages = []
    for message in messages:
        # 先处理TRANSFER标记
        processed_msg = '人工客服' if 'TRANSFER' in message else message

        # 检查是否包含违禁词，如果包含则调用大模型改写
        if forbidden_words and contains_forbidden_word(processed_msg, forbidden_words):
            processed_msg = await rewrite_without_forbidden_words(processed_msg, forbidden_words)

        processed_messages.append(processed_msg)

    return {
        "flow_name": "意图识别",
        "flow_type": "INTENT",

        "messages": processed_messages,
        "forward_group_type": business_forward_group_type,

        "debug_message": debug_message.strip(),
        "event_one": event_one,
        "event_two": event_two,
        "event_two_transfer_human": True if event_two_transfer_human else False,
        "situation_transfer_human": True if situation_transfer_human else False,

        "top_situation":judge_top_situation,

        "behavior": behavior,
        "intent_thinking": judge_thinking,
        "quality_inspection": quality_inspection,
        "general_qa_thinking": business_thinking,
        "recommend_thinking": product_thinking,
        "search_thinking": search_thinking,
        "emotion": judge_emotion,
        "product_data": business_product_data,
        "business_context": business_context,
        "context_infos": [
            *context_infos,
            *preprocess["images"],
        ]
    }
