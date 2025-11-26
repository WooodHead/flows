<user>
  <data_source>
    event_list:
      content: "{{preprocess.tags}}"
      description: "事件分类列表，包含一级和二级分类"
  </data_source>

  <conversation>
    message:
      content: "{{preprocess.latest_message}}"
      description: "顾客最新消息"
    dialogue:
      content: "{{dialogue}}"
      description: "完整对话记录"
    images:
      content: "{{preprocess.images}}"
      description: "图片内容描述（如有）"
  </conversation>
</user>
