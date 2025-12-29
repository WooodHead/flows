from betteryeah import BetterYeah, Model
better_yeah = BetterYeah()

async def main():
    thinking = summary.get('thinking')
    messages = summary.get('messages', [])
    answer = '\n'.join(messages) 
    
    return {
        'messages': messages,
        'thinking': thinking,
        "flow_name": "商品推荐",
        "flow_type": "RECOMMEND",
        "debug_message":f"商品推荐:\n\t思考过程: {thinking}\n\t回答: {answer}"
    }
