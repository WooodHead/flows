from betteryeah import BetterYeah
from datetime import datetime

better_yeah = BetterYeah()

async def main():
    # 获取当前轮次（从全局变量或循环索引获取）
    current_round = betterAI.store.get("current_round") or 1
    round_key = str(current_round)
    
    # 测试集问题
    test_question = betterAI.store.get("test_question") or {}

    # 测试时间
    test_question_time = betterAI.store.get("test_question_time") or {}

    # 测试集答案
    test_answer = betterAI.store.get("test_answer") or {}

    # 实际答案
    actual_answer = betterAI.store.get("actual_answer") or {}

    # 实际回复时间
    actual_answer_time = betterAI.store.get("actual_answer_time") or {}

    # 评分
    score = betterAI.store.get("score") or {}

    # 原因
    reason_for_match = betterAI.store.get("reason_for_match") or {}

    # 记录ID
    record_id = betterAI.store.get("record_id") or {}

    # 是否转人工
    transfer_to_human = betterAI.store.get("transfer_to_human") or {}
    
    # 转换时间戳为ISO格式
    def timestamp_to_iso(timestamp):
        return datetime.fromtimestamp(timestamp).isoformat()
    
    # 更新当前轮次的数据
    test_question[round_key] = loop["item"]["客户"]
    test_question_time[round_key] = timestamp_to_iso(time)
    test_answer[round_key] = loop["item"]["客服"]
    actual_answer[round_key] = chat["data"][0]["text"]
    actual_answer_time[round_key] = timestamp_to_iso(chat["now_time"])
    score[round_key] = evaluate_single["score"]
    reason_for_match[round_key] = evaluate_single["reason"]
    record_id[round_key] = chat["data"][0]["record_id"]

    # 保存回全局变量
    betterAI.store.set("test_question", test_question)
    betterAI.store.set("test_question_time", test_question_time)
    betterAI.store.set("test_answer", test_answer)
    betterAI.store.set("actual_answer", actual_answer)
    betterAI.store.set("actual_answer_time", actual_answer_time)
    betterAI.store.set("score", score)
    betterAI.store.set("reason_for_match", reason_for_match)
    betterAI.store.set("record_id", record_id)
    
    # 更新轮次计数
    betterAI.store.set("current_round", current_round + 1)

    # 构建全局分析JSON - 用于对比标准答案和实际回复
    global_analysis = []
    for round_num in sorted(test_question.keys(), key=lambda x: int(x)):
        global_analysis.append({
            "轮次": int(round_num),
            "问题": test_question[round_num],
            "标准答案": test_answer[round_num],
            "实际回复": actual_answer[round_num],
            "得分": score[round_num]
        })
    
    return {
        "round": round_key,
        "test_question": test_question,
        "test_question_time": test_question_time,
        "test_answer": test_answer,
        "actual_answer": actual_answer,
        "actual_answer_time": actual_answer_time,
        "score": score,
        "reason_for_match": reason_for_match,
        "record_id": record_id,
        "global_analysis": global_analysis  # 新增：全局分析JSON
    }
