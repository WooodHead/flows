from betteryeah import BetterYeah
import json
import re
import string
better_yeah = BetterYeah()

def clean_string(text):
    """
    清理字符串:去除空格、换行、标点符号
    """
    print(f"[clean_string] 输入文本: {repr(text)}")

    if not text:
        print("[clean_string] 文本为空,返回空字符串")
        return ""

    # 去除所有空白字符(空格、制表符、换行符等)
    text = re.sub(r'\s+', '', text)
    print(f"[clean_string] 去除空白字符后: {repr(text)}")

    # 去除英文标点符号
    text = text.translate(str.maketrans('', '', string.punctuation))
    print(f"[clean_string] 去除英文标点后: {repr(text)}")

    # 去除中文标点符号
    chinese_punctuation = '。,、;:?!…—·ˉ¨''""々～‖∶"''{}[]()<>《》【】「」『』〔〕／\\'
    text = re.sub(f'[{re.escape(chinese_punctuation)}]', '', text)
    print(f"[clean_string] 清理后的最终文本: {repr(text)}")

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
    print(f"\n[calculate_similarity] 比较字符串:")
    print(f"  str1原文: {repr(str1[:100])}..." if len(str1) > 100 else f"  str1原文: {repr(str1)}")
    print(f"  str2原文: {repr(str2[:100])}..." if len(str2) > 100 else f"  str2原文: {repr(str2)}")

    # 清理字符串
    str1 = clean_string(str1)
    str2 = clean_string(str2)

    if not str1 and not str2:
        print("[calculate_similarity] 两个字符串都为空,相似度: 100.0")
        return 100.0

    if not str1 or not str2:
        print("[calculate_similarity] 其中一个字符串为空,相似度: 0.0")
        return 0.0

    distance = levenshtein_distance(str1, str2)
    max_length = max(len(str1), len(str2))
    print(f"[calculate_similarity] Levenshtein距离: {distance}, 最大长度: {max_length}")

    similarity = (1.0 - distance / max_length) * 100.0
    print(f"[calculate_similarity] 计算相似度: {similarity:.2f}%")
    return similarity


def check_similarity(text1, text2, threshold=70):
    """检查两个文本的相似度"""
    similarity = calculate_similarity(text1, text2)
    return similarity >= threshold

def extract_assistant_replies(dialogue):
    """提取对话中assistant的所有回复内容"""
    print(f"\n[extract_assistant_replies] 开始提取assistant回复")
    print(f"[extract_assistant_replies] 对话消息数量: {len(dialogue) if dialogue else 0}")

    if not dialogue:
        print("[extract_assistant_replies] 对话为空,返回空列表")
        return []

    assistant_replies = []

    for idx, message in enumerate(dialogue):
        if isinstance(message, dict) and message.get("role") == "assistant":
            print(f"[extract_assistant_replies] 找到第{idx}条assistant消息")
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
                print(f"[extract_assistant_replies] 添加回复内容(前50字): {str(text).strip()[:50]}...")

    print(f"[extract_assistant_replies] 共提取到{len(assistant_replies)}条assistant回复")
    return assistant_replies

def parse_dialogue_data(dialogue_data):
    """解析对话数据"""
    print(f"\n[parse_dialogue_data] 数据类型: {type(dialogue_data)}")

    if isinstance(dialogue_data, list):
        print(f"[parse_dialogue_data] 数据已是列表格式,长度: {len(dialogue_data)}")
        return dialogue_data
    if isinstance(dialogue_data, str):
        print(f"[parse_dialogue_data] 字符串数据,长度: {len(dialogue_data)}")
        try:
            parsed = json.loads(dialogue_data.strip())
            print(f"[parse_dialogue_data] JSON解析成功,结果类型: {type(parsed)}")
            return parsed
        except Exception as e:
            print(f"[parse_dialogue_data] JSON解析失败: {e}")
            raise Exception(f"无法解析对话数据: {e}")
    # 如果是其他格式，直接返回
    print(f"[parse_dialogue_data] 其他格式,直接返回")
    return dialogue_data

# 必须保证节点中存在一个main函数
async def main():
    try:
        print("\n" + "="*60)
        print("开始执行促单预处理流程")
        print("="*60)

        # 检查促单功能是否启用
        promotion_enabled = sop_config.get("promotion_enabled", True)
        print(f"\n[main] 促单功能启用状态: {promotion_enabled}")
        if not promotion_enabled:
            print("[main] 促单功能未启用,直接返回")
            return {
                "promotion_scripts": [],
                "promotion_scripts_count": 0,
            }

        # 解析输入的对话数据
        dialogue_list = parse_dialogue_data(dialogue)

        # 提取assistant的所有历史回复（客服消息）
        assistant_replies = extract_assistant_replies(dialogue_list)

        # 获取促销话术列表
        promotion_scripts = sop_config.get("promotion_scripts", [])
        print(f"\n[main] 促销话术总数: {len(promotion_scripts)}")

        # 过滤出没有发送过的促销话术
        unsent_scripts = []

        for idx, script in enumerate(promotion_scripts):
            script_content = script.get("content", "")
            print(f"\n[main] 检查第{idx+1}个促销话术:")
            print(f"  话术内容(前50字): {script_content[:50]}..." if len(script_content) > 50 else f"  话术内容: {script_content}")

            if not script_content:
                print("  话术内容为空,跳过")
                continue

            # 检查该话术是否已经发送过（相似度>=90%）
            is_sent = False
            for reply_idx, reply in enumerate(assistant_replies):
                similarity = calculate_similarity(reply, script_content)
                if similarity >= 90:
                    print(f"  与第{reply_idx+1}条历史回复相似度{similarity:.2f}% >= 90%,判定为已发送")
                    is_sent = True
                    break

            # 如果没有发送过，添加到结果列表
            if not is_sent:
                print("  该话术未发送过,添加到结果列表")
                unsent_scripts.append(script)
            else:
                print("  该话术已发送过,跳过")

        print(f"\n[main] 过滤完成:")
        print(f"  总话术数: {len(promotion_scripts)}")
        print(f"  未发送话术数: {len(unsent_scripts)}")
        print("="*60)

        return {
            "promotion_scripts": unsent_scripts,
            "promotion_scripts_count": len(unsent_scripts),
        }

    except Exception as e:
        print(f"\n[main] 发生异常: {str(e)}")
        import traceback
        print(f"[main] 异常堆栈:\n{traceback.format_exc()}")
        return {
            "error": f"处理失败: {str(e)}",
            "promotion_scripts": [],
            "promotion_scripts_count": 0
        }
