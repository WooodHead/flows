from betteryeah import BetterYeah
import json
import re
import string
better_yeah = BetterYeah()

def clean_string(text):
    """
    清理字符串:去除空格、换行、标点符号
    """
    if not text:
        return ""

    # 去除所有空白字符(空格、制表符、换行符等)
    text = re.sub(r'\s+', '', text)

    # 去除英文标点符号
    text = text.translate(str.maketrans('', '', string.punctuation))

    # 去除中文标点符号
    chinese_punctuation = '。,、;:?!…—·ˉ¨''""々～‖∶"''{}[]()<>《》【】「」『』〔〕／\\'
    text = re.sub(f'[{re.escape(chinese_punctuation)}]', '', text)

    return text


def levenshtein_distance(str1, str2):
    """
    计算 Levenshtein 距离
    """
    m, n = len(str1), len(str2)
    matrix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        matrix[i][0] = i
    for j in range(n + 1):
        matrix[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost
            )

    return matrix[m][n]


def calculate_similarity(str1, str2):
    """
    计算两个字符串的相似度百分比(基于 Levenshtein 距离)
    自动清理空格、换行和标点符号

    Args:
        str1: 第一个字符串
        str2: 第二个字符串

    Returns:
        相似度百分比 (0-100)
    """
    # 清理字符串
    str1 = clean_string(str1)
    str2 = clean_string(str2)

    if not str1 and not str2:
        return 100.0

    if not str1 or not str2:
        return 0.0

    distance = levenshtein_distance(str1, str2)
    max_length = max(len(str1), len(str2))

    similarity = (1.0 - distance / max_length) * 100.0
    return similarity


def check_similarity(text1, text2, threshold=70):
    """检查两个文本的相似度"""
    similarity = calculate_similarity(text1, text2)
    return similarity >= threshold

def extract_assistant_replies(dialogue):
    """提取对话中assistant的所有回复内容"""
    if not dialogue:
        return []
    
    assistant_replies = []
    
    for message in dialogue:
        if isinstance(message, dict) and message.get("role") == "assistant":
            content = message.get("content", {})
            
            # 提取文本内容
            if isinstance(content, dict):
                text = content.get("text", "")
                # 处理text可能是列表的情况
                if isinstance(text, list) and len(text) > 0:
                    text = text[0]  # 取第一个元素
            else:
                text = str(content) if content else ""
            
            # 只记录有文字内容的回复
            if text and str(text).strip():
                assistant_replies.append(str(text).strip())
    
    return assistant_replies

def parse_dialogue_data(dialogue_data):
    """解析对话数据"""
    if isinstance(dialogue_data, list):
        return dialogue_data
    if isinstance(dialogue_data, str):
        try:
            return json.loads(dialogue_data.strip())
        except Exception as e:
            raise Exception(f"无法解析对话数据: {e}")
    # 如果是其他格式，直接返回
    return dialogue_data

# 必须保证节点中存在一个main函数
async def main():
    try:
        # 解析输入的对话数据
        dialogue_list = parse_dialogue_data(dialogue)

        # 提取assistant的所有历史回复（客服消息）
        assistant_replies = extract_assistant_replies(dialogue_list)

        # 获取促销话术列表
        promotion_scripts = sop_config.get("promotion_scripts", [])

        # 过滤出没有发送过的促销话术
        unsent_scripts = []

        for script in promotion_scripts:
            script_content = script.get("content", "")
            if not script_content:
                continue

            # 检查该话术是否已经发送过（相似度>=90%）
            is_sent = False
            for reply in assistant_replies:
                similarity = calculate_similarity(reply, script_content)
                if similarity >= 90:
                    is_sent = True
                    break

            # 如果没有发送过，添加到结果列表
            if not is_sent:
                unsent_scripts.append(script)

        return {
            "promotion_scripts": unsent_scripts,
        }

    except Exception as e:
        return {
            "error": f"处理失败: {str(e)}",
            "promotion_scripts": []
        }
