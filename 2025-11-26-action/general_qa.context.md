<user>
  <conversation>
    dialogue:
      content: "{{dialogue}}"
      description: "历史对话记录"
    message:
      content: "{{latest_message}}"
      description: "顾客最新消息"
  </conversation>

  <data_source>
    product_data:
      content: "{{context.data}}"
      description: "商品id | 商品参数信息 | 商品 SKU 信息"
    faq_knowledge:
      content: "{{context.faq}}"
      description: "FAQ知识"
    common_knowledge:
      content: "{{context.common}}"
      description: "通用知识库"
  </data_source>

  <reference>
    time:
      content: "{{context.current_time}}"
      description: "当前时间"
    image:
      content: "{{image}}"
      description: "图片内容描述（如有）"
  </reference>

  <instruction>
    请根据规则，准确回复顾客咨询。
  </instruction>
</user>
