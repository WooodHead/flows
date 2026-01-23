from betteryeah import BetterYeah
better_yeah = BetterYeah()


def normalize_invite_format(invite_data):
    """
    处理invite格式不对的情况
    将嵌套的数组格式 [[{...}]] 转换为正确的对象格式 {...}
    """
    # 如果数据被包裹在多层列表中，递归解包
    while isinstance(invite_data, list):
        if len(invite_data) == 0:
            return {}
        if len(invite_data) == 1:
            invite_data = invite_data[0]
        else:
            # 如果列表有多个元素，返回第一个字典类型的元素
            for item in invite_data:
                if isinstance(item, dict):
                    return item
            return {}

    # 如果最终结果是字典，返回它
    if isinstance(invite_data, dict):
        return invite_data

    return {}


async def main(pre_process, invite, customer_config):
    pre_process_should_send_invite = pre_process.get("should_send_invite", False)

    if not pre_process_should_send_invite:
        return {
            "messages": [],
            "answer": "",

            "flow_name": "满意度邀评",
            "flow_type": "INVITATION_RATING",

            "event_one": "满意度邀评",
            "event_two": "满意度邀评",
            "event_two_transfer_human": False,
        }

    # 规范化invite格式，处理 [[{...}]] 或 [{...}] 格式
    invite = normalize_invite_format(invite)

    should_send_invitation_rating = invite.get("should_send_invitation_rating", False)

    if not should_send_invitation_rating:
        return {
            "messages": [],
            "answer": "",

            "flow_name": "满意度邀评",
            "flow_type": "INVITATION_RATING",

            "event_one": "满意度邀评",
            "event_two": "满意度邀评",
            "event_two_transfer_human": False,
        }

    answer = customer_config.get("invitation_rating", {}).get("invitation_rating_message", "")
    result = {
        "messages":[answer] if answer else [],
        "answer": answer,

        "flow_name": "满意度邀评",
        "flow_type": "INVITATION_RATING",

        "event_one": "满意度邀评",
        "event_two": "满意度邀评",
        "event_two_transfer_human": False,
    }
    return result

