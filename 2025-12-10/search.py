from betteryeah import BetterYeah, Model
better_yeah = BetterYeah()


async def main():
    fallback = {
        'messages': ['人工客服'],
        'thinking': None,
        "flow_name": "查找商品",
        "flow_type": "SEARCH",
        "debug_message": "查找商品:\n\t思考过程: 无\n\t回答: 人工客服",
    }

    try:
        current_solution = solution
    except NameError:
        print("solution is not defined")
        return fallback

    print(f"solution {current_solution}")

    if not isinstance(current_solution, dict) or not current_solution:
        return fallback

    answer = current_solution.get('answer')
    thinking = current_solution.get('thinking')

    return {
        'messages': [answer],
        'thinking': thinking,
        "flow_name": "查找商品",
        "flow_type": "SEARCH",
        "debug_message": f"查找商品:\n\t思考过程: {thinking}\n\t回答: {answer}"
    }
