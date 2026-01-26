2025-12-19 18:41:59,358	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': '6f23cf53-3202-470b-a138-22a7f9baa589', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:41:59,359	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': 'b8de3acf-ad48-4975-a835-5be0247af7f1', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:41:59,362	"临时打印 qianniu__木瓜瓜木的小店__木瓜瓜木 异常2：Traceback (most recent call last):
  File ""/app/routers/client/api/client_router.py"", line 730, in copilot_agent_connect
    message = await websocket.receive_text()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 120, in receive_text
    self._raise_on_disconnect(message)
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 114, in _raise_on_disconnect
    raise WebSocketDisconnect(message[""code""], message.get(""reason""))
starlette.websockets.WebSocketDisconnect: (1000, '')
, equipment_information_id=576c9d67462d4d7b8be79431353c2f57"
2025-12-19 18:41:59,369	ws/client/message 新连接请求 - 客户端: 172.16.192.177:23578, channel: qianniu, shop_id: 木瓜瓜木的小店, assistant_id: 木瓜瓜木, workspace_id: a042945be289477b9af048014f0f7cdb, bty_user_id: 10058, customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f, desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:41:59,382	设备状态已更新: 576c9d67462d4d7b8be79431353c2f57 → disconnected
2025-12-19 18:41:59,383	移除WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 剩余连接数: 109
2025-12-19 18:41:59,383	RPA断开ws连接：qianniu__木瓜瓜木的小店__木瓜瓜木, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:41:59,398	设置全局WS连接状态: global_ws_connection:dev:client_message:qianniu__木瓜瓜木的小店__木瓜瓜木
2025-12-19 18:41:59,399	添加WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 当前本地连接数: 110
2025-12-19 18:41:59,410	自动更新用户: 从 10058 到 10058, 店铺-客服: qianniu-木瓜瓜木的小店-木瓜瓜木
2025-12-19 18:41:59,410	ws/client/message  existing_record: equipment_information={'status': 'disconnected', 'channel': 'qianniu', 'assistant_id': '木瓜瓜木', 'client_status': 'online', 'assistant_name': '木瓜瓜木', 'equipment_image': None} created_by='夕谷' created_at=datetime.datetime(2025, 12, 19, 17, 17, 36, 716056) channel='qianniu' expected_status='running' modified_by='夕谷' shop_id='木瓜瓜木的小店' connection_time=datetime.datetime(2025, 12, 19, 18, 41, 59, 339014) creator_id=10058 updated_at=datetime.datetime(2025, 12, 19, 18, 41, 59, 385154) bty_user_id='10058' disconnect_time=datetime.datetime(2025, 12, 19, 18, 41, 59, 374452) customer_agent_config_id='84fe447220aa4b0d907cc26b46cdfe1f' deleted=False robot_name='Robot_木瓜瓜木' disconnect_reason=None quality_inspection_config=None id=443 equipment_information_id='576c9d67462d4d7b8be79431353c2f57' status='disconnected' workspace_id='a042945be289477b9af048014f0f7cdb' robot_settings={'forward_group': {'pre_sales': '售前2'}} client_status='online' agent_mode='auto_reply' client_credentials={'encrypted_at': '2025-12-19T17:17:36.760634', 'client_password': 'YnVndTEyMzQ=', 'client_username': '5pyo55Oc55Oc5pyo'} assistant_id='木瓜瓜木' shared_user_ids=None cloud_desktop_id='aad6a6ab5543484aaf48929cf95e3e2b'
2025-12-19 18:41:59,411	Robot 建立消息上报连接: equipment_information_id=576c9d67462d4d7b8be79431353c2f57, channel=qianniu, shop_id=木瓜瓜木的小店, assistant_id=木瓜瓜木
2025-12-19 18:41:59,411	ws/client/message  desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:41:59,416	ws/client/message  customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:41:59,416	ws/client/message 绑定设备与customer_agent_config - customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:41:59,424	"临时打印 qianniu__木瓜瓜木的小店__木瓜瓜木 异常2：Traceback (most recent call last):
  File ""/app/routers/client/api/client_router.py"", line 583, in copilot_agent_connect
    message = await websocket.receive_text()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 120, in receive_text
    self._raise_on_disconnect(message)
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 114, in _raise_on_disconnect
    raise WebSocketDisconnect(message[""code""], message.get(""reason""))
starlette.websockets.WebSocketDisconnect: (<CloseCode.ABNORMAL_CLOSURE: 1006>, '')
, equipment_information_id=576c9d67462d4d7b8be79431353c2f57"
2025-12-19 18:41:59,435	设备状态已更新: 576c9d67462d4d7b8be79431353c2f57 → disconnected
2025-12-19 18:41:59,436	移除WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 剩余连接数: 109
2025-12-19 18:41:59,436	RPA断开ws连接：qianniu__木瓜瓜木的小店__木瓜瓜木, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:41:59,521	ws/client/message 新连接请求 - 客户端: 172.16.199.249:60354, channel: qianniu, shop_id: 木瓜瓜木的小店, assistant_id: 木瓜瓜木, workspace_id: a042945be289477b9af048014f0f7cdb, bty_user_id: 10058, customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f, desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:41:59,556	设置全局WS连接状态: global_ws_connection:dev:client_message:qianniu__木瓜瓜木的小店__木瓜瓜木
2025-12-19 18:41:59,556	添加WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 当前本地连接数: 110
2025-12-19 18:41:59,567	自动更新用户: 从 10058 到 10058, 店铺-客服: qianniu-木瓜瓜木的小店-木瓜瓜木
2025-12-19 18:41:59,568	ws/client/message  existing_record: equipment_information={'status': 'disconnected', 'channel': 'qianniu', 'assistant_id': '木瓜瓜木', 'client_status': 'online', 'assistant_name': '木瓜瓜木', 'equipment_image': None} created_by='夕谷' created_at=datetime.datetime(2025, 12, 19, 17, 17, 36, 716056) channel='qianniu' expected_status='running' modified_by='夕谷' shop_id='木瓜瓜木的小店' connection_time=datetime.datetime(2025, 12, 19, 18, 41, 59, 404469) creator_id=10058 updated_at=datetime.datetime(2025, 12, 19, 18, 41, 59, 432166) bty_user_id='10058' disconnect_time=datetime.datetime(2025, 12, 19, 18, 41, 59, 429463) customer_agent_config_id='84fe447220aa4b0d907cc26b46cdfe1f' deleted=False robot_name='Robot_木瓜瓜木' disconnect_reason=None quality_inspection_config=None id=443 equipment_information_id='576c9d67462d4d7b8be79431353c2f57' status='disconnected' workspace_id='a042945be289477b9af048014f0f7cdb' robot_settings={'forward_group': {'pre_sales': '售前2'}} client_status='online' agent_mode='auto_reply' client_credentials={'encrypted_at': '2025-12-19T17:17:36.760634', 'client_password': 'YnVndTEyMzQ=', 'client_username': '5pyo55Oc55Oc5pyo'} assistant_id='木瓜瓜木' shared_user_ids=None cloud_desktop_id='aad6a6ab5543484aaf48929cf95e3e2b'
2025-12-19 18:41:59,568	Robot 建立消息上报连接: equipment_information_id=576c9d67462d4d7b8be79431353c2f57, channel=qianniu, shop_id=木瓜瓜木的小店, assistant_id=木瓜瓜木
2025-12-19 18:41:59,569	ws/client/message  desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:41:59,574	ws/client/message  customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:41:59,575	ws/client/message 绑定设备与customer_agent_config - customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:41:59,582	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': '2afd7062-d6bf-4211-bb6b-0303c19b5877', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:41:59,583	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': 'c4445709-e87f-4ea5-bd32-a390ada2f998', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:41:59,695	"临时打印 qianniu__木瓜瓜木的小店__木瓜瓜木 异常2：Traceback (most recent call last):
  File ""/app/routers/client/api/client_router.py"", line 730, in copilot_agent_connect
    message = await websocket.receive_text()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 120, in receive_text
    self._raise_on_disconnect(message)
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 114, in _raise_on_disconnect
    raise WebSocketDisconnect(message[""code""], message.get(""reason""))
starlette.websockets.WebSocketDisconnect: (1000, '')
, equipment_information_id=576c9d67462d4d7b8be79431353c2f57"
2025-12-19 18:41:59,706	设备状态已更新: 576c9d67462d4d7b8be79431353c2f57 → disconnected
2025-12-19 18:41:59,707	移除WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 剩余连接数: 109
2025-12-19 18:41:59,707	RPA断开ws连接：qianniu__木瓜瓜木的小店__木瓜瓜木, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:41:59,729	RPA断连告警被限频: channel=qianniu, shop_id=木瓜瓜木的小店, assistant_id=木瓜瓜木, equipment_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:41:59,738	ws/client/message 新连接请求 - 客户端: 172.16.199.249:60364, channel: qianniu, shop_id: 木瓜瓜木的小店, assistant_id: 木瓜瓜木, workspace_id: a042945be289477b9af048014f0f7cdb, bty_user_id: 10058, customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f, desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:41:59,757	设置全局WS连接状态: global_ws_connection:dev:client_message:qianniu__木瓜瓜木的小店__木瓜瓜木
2025-12-19 18:41:59,758	添加WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 当前本地连接数: 110
2025-12-19 18:41:59,768	自动更新用户: 从 10058 到 10058, 店铺-客服: qianniu-木瓜瓜木的小店-木瓜瓜木
2025-12-19 18:41:59,768	ws/client/message  existing_record: equipment_information={'status': 'disconnected', 'channel': 'qianniu', 'assistant_id': '木瓜瓜木', 'client_status': 'online', 'assistant_name': '木瓜瓜木', 'equipment_image': None} created_by='夕谷' created_at=datetime.datetime(2025, 12, 19, 17, 17, 36, 716056) channel='qianniu' expected_status='running' modified_by='夕谷' shop_id='木瓜瓜木的小店' connection_time=datetime.datetime(2025, 12, 19, 18, 41, 59, 561920) creator_id=10058 updated_at=datetime.datetime(2025, 12, 19, 18, 41, 59, 703868) bty_user_id='10058' disconnect_time=datetime.datetime(2025, 12, 19, 18, 41, 59, 700905) customer_agent_config_id='84fe447220aa4b0d907cc26b46cdfe1f' deleted=False robot_name='Robot_木瓜瓜木' disconnect_reason=None quality_inspection_config=None id=443 equipment_information_id='576c9d67462d4d7b8be79431353c2f57' status='disconnected' workspace_id='a042945be289477b9af048014f0f7cdb' robot_settings={'forward_group': {'pre_sales': '售前2'}} client_status='online' agent_mode='auto_reply' client_credentials={'encrypted_at': '2025-12-19T17:17:36.760634', 'client_password': 'YnVndTEyMzQ=', 'client_username': '5pyo55Oc55Oc5pyo'} assistant_id='木瓜瓜木' shared_user_ids=None cloud_desktop_id='aad6a6ab5543484aaf48929cf95e3e2b'
2025-12-19 18:41:59,769	Robot 建立消息上报连接: equipment_information_id=576c9d67462d4d7b8be79431353c2f57, channel=qianniu, shop_id=木瓜瓜木的小店, assistant_id=木瓜瓜木
2025-12-19 18:41:59,769	ws/client/message  desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:41:59,774	ws/client/message  customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:41:59,775	ws/client/message 绑定设备与customer_agent_config - customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:41:59,783	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': '944fb3bf-57b0-49fa-a5f3-22887b695595', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:41:59,784	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': 'f6a2dc83-8ec6-406b-83f0-cd57a26f33d1', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:41:59,785	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': '68617da3-4da1-497b-b84b-fbbcb5c3cc9e', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:41:59,788	"临时打印 qianniu__木瓜瓜木的小店__木瓜瓜木 异常2：Traceback (most recent call last):
  File ""/app/routers/client/api/client_router.py"", line 730, in copilot_agent_connect
    message = await websocket.receive_text()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 120, in receive_text
    self._raise_on_disconnect(message)
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 114, in _raise_on_disconnect
    raise WebSocketDisconnect(message[""code""], message.get(""reason""))
starlette.websockets.WebSocketDisconnect: (1000, '')
, equipment_information_id=576c9d67462d4d7b8be79431353c2f57"
2025-12-19 18:41:59,805	设备状态已更新: 576c9d67462d4d7b8be79431353c2f57 → disconnected
2025-12-19 18:41:59,806	移除WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 剩余连接数: 109
2025-12-19 18:41:59,806	RPA断开ws连接：qianniu__木瓜瓜木的小店__木瓜瓜木, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:41:59,899	ws/client/message 新连接请求 - 客户端: 172.16.192.177:23596, channel: qianniu, shop_id: 木瓜瓜木的小店, assistant_id: 木瓜瓜木, workspace_id: a042945be289477b9af048014f0f7cdb, bty_user_id: 10058, customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f, desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:41:59,918	设置全局WS连接状态: global_ws_connection:dev:client_message:qianniu__木瓜瓜木的小店__木瓜瓜木
2025-12-19 18:41:59,918	添加WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 当前本地连接数: 110
2025-12-19 18:41:59,929	自动更新用户: 从 10058 到 10058, 店铺-客服: qianniu-木瓜瓜木的小店-木瓜瓜木
2025-12-19 18:41:59,930	ws/client/message  existing_record: equipment_information={'status': 'disconnected', 'channel': 'qianniu', 'assistant_id': '木瓜瓜木', 'client_status': 'online', 'assistant_name': '木瓜瓜木', 'equipment_image': None} created_by='夕谷' created_at=datetime.datetime(2025, 12, 19, 17, 17, 36, 716056) channel='qianniu' expected_status='running' modified_by='夕谷' shop_id='木瓜瓜木的小店' connection_time=datetime.datetime(2025, 12, 19, 18, 41, 59, 763421) creator_id=10058 updated_at=datetime.datetime(2025, 12, 19, 18, 41, 59, 807606) bty_user_id='10058' disconnect_time=datetime.datetime(2025, 12, 19, 18, 41, 59, 797093) customer_agent_config_id='84fe447220aa4b0d907cc26b46cdfe1f' deleted=False robot_name='Robot_木瓜瓜木' disconnect_reason=None quality_inspection_config=None id=443 equipment_information_id='576c9d67462d4d7b8be79431353c2f57' status='disconnected' workspace_id='a042945be289477b9af048014f0f7cdb' robot_settings={'forward_group': {'pre_sales': '售前2'}} client_status='online' agent_mode='auto_reply' client_credentials={'encrypted_at': '2025-12-19T17:17:36.760634', 'client_password': 'YnVndTEyMzQ=', 'client_username': '5pyo55Oc55Oc5pyo'} assistant_id='木瓜瓜木' shared_user_ids=None cloud_desktop_id='aad6a6ab5543484aaf48929cf95e3e2b'
2025-12-19 18:41:59,930	Robot 建立消息上报连接: equipment_information_id=576c9d67462d4d7b8be79431353c2f57, channel=qianniu, shop_id=木瓜瓜木的小店, assistant_id=木瓜瓜木
2025-12-19 18:41:59,931	ws/client/message  desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:41:59,935	ws/client/message  customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:41:59,936	ws/client/message 绑定设备与customer_agent_config - customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:41:59,943	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': '4ffdbb35-ee2c-4581-b617-06b85c440f1a', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:41:59,944	临时打印 心跳 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'request_id': '6986cd72-aa23-4975-970d-803af28479a2', 'type': 'health', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:41:59,947	Robot健康度报告 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'last_agent_reply_time': 1766136304, 'last_action_time': 1766140918, 'message_queue_size': 0, 'waiting_users_count': 0, 'cpu_usage': 11.4, 'memory_usage': 10538.8, 'rpa_cpu_usage': 0.0, 'rpa_memory_usage': 0.0, 'rpa_status': 'running', 'client_status': 'online', 'recent_errors': []}, 'request_id': '78e8bcff-b5ba-4135-a81d-417c1a633a5b', 'type': 'robot-health-report', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:41:59,949	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': '1c4d1c24-57e3-41a0-8b30-46ec4eb65fcd', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:41:59,968	"临时打印 qianniu__木瓜瓜木的小店__木瓜瓜木 异常2：Traceback (most recent call last):
  File ""/app/routers/client/api/client_router.py"", line 730, in copilot_agent_connect
    message = await websocket.receive_text()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 120, in receive_text
    self._raise_on_disconnect(message)
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 114, in _raise_on_disconnect
    raise WebSocketDisconnect(message[""code""], message.get(""reason""))
starlette.websockets.WebSocketDisconnect: (1000, '')
, equipment_information_id=576c9d67462d4d7b8be79431353c2f57"
2025-12-19 18:41:59,976	设备状态已更新: 576c9d67462d4d7b8be79431353c2f57 → running
2025-12-19 18:41:59,978	workspace websocket_send_message. workspace_id: a042945be289477b9af048014f0f7cdb
2025-12-19 18:41:59,983	设备状态已更新: 576c9d67462d4d7b8be79431353c2f57 → disconnected
2025-12-19 18:41:59,984	移除WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 剩余连接数: 109
2025-12-19 18:41:59,984	RPA断开ws连接：qianniu__木瓜瓜木的小店__木瓜瓜木, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:00,614	
2025-12-19 18:42:00,958	
2025-12-19 18:42:00,009	RPA断连告警被限频: channel=qianniu, shop_id=木瓜瓜木的小店, assistant_id=木瓜瓜木, equipment_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:00,268	ws/client/message 新连接请求 - 客户端: 172.16.199.249:60374, channel: qianniu, shop_id: 木瓜瓜木的小店, assistant_id: 木瓜瓜木, workspace_id: a042945be289477b9af048014f0f7cdb, bty_user_id: 10058, customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f, desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:42:00,290	设置全局WS连接状态: global_ws_connection:dev:client_message:qianniu__木瓜瓜木的小店__木瓜瓜木
2025-12-19 18:42:00,290	添加WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 当前本地连接数: 110
2025-12-19 18:42:00,301	自动更新用户: 从 10058 到 10058, 店铺-客服: qianniu-木瓜瓜木的小店-木瓜瓜木
2025-12-19 18:42:00,301	ws/client/message  existing_record: equipment_information={'status': 'disconnected', 'channel': 'qianniu', 'assistant_id': '木瓜瓜木', 'client_status': 'online', 'assistant_name': '木瓜瓜木', 'equipment_image': None} created_by='夕谷' created_at=datetime.datetime(2025, 12, 19, 17, 17, 36, 716056) channel='qianniu' expected_status='running' modified_by='夕谷' shop_id='木瓜瓜木的小店' connection_time=datetime.datetime(2025, 12, 19, 18, 41, 59, 924326) creator_id=10058 updated_at=datetime.datetime(2025, 12, 19, 18, 41, 59, 980079) bty_user_id='10058' disconnect_time=datetime.datetime(2025, 12, 19, 18, 41, 59, 975469) customer_agent_config_id='84fe447220aa4b0d907cc26b46cdfe1f' deleted=False robot_name='Robot_木瓜瓜木' disconnect_reason=None quality_inspection_config=None id=443 equipment_information_id='576c9d67462d4d7b8be79431353c2f57' status='disconnected' workspace_id='a042945be289477b9af048014f0f7cdb' robot_settings={'forward_group': {'pre_sales': '售前2'}} client_status='online' agent_mode='auto_reply' client_credentials={'encrypted_at': '2025-12-19T17:17:36.760634', 'client_password': 'YnVndTEyMzQ=', 'client_username': '5pyo55Oc55Oc5pyo'} assistant_id='木瓜瓜木' shared_user_ids=None cloud_desktop_id='aad6a6ab5543484aaf48929cf95e3e2b'
2025-12-19 18:42:00,302	Robot 建立消息上报连接: equipment_information_id=576c9d67462d4d7b8be79431353c2f57, channel=qianniu, shop_id=木瓜瓜木的小店, assistant_id=木瓜瓜木
2025-12-19 18:42:00,302	ws/client/message  desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:42:00,307	ws/client/message  customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:42:00,308	ws/client/message 绑定设备与customer_agent_config - customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:42:00,315	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': '1e05ccd5-3be5-41fe-bbea-94323f762f1f', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:00,316	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': '4f8d76cc-6869-4046-a96b-043be9b951b1', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:00,529	"临时打印 qianniu__木瓜瓜木的小店__木瓜瓜木 异常2：Traceback (most recent call last):
  File ""/app/routers/client/api/client_router.py"", line 730, in copilot_agent_connect
    message = await websocket.receive_text()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 120, in receive_text
    self._raise_on_disconnect(message)
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 114, in _raise_on_disconnect
    raise WebSocketDisconnect(message[""code""], message.get(""reason""))
starlette.websockets.WebSocketDisconnect: (1000, '')
, equipment_information_id=576c9d67462d4d7b8be79431353c2f57"
2025-12-19 18:42:00,538	ws/client/message 新连接请求 - 客户端: 172.16.192.177:23608, channel: qianniu, shop_id: 木瓜瓜木的小店, assistant_id: 木瓜瓜木, workspace_id: a042945be289477b9af048014f0f7cdb, bty_user_id: 10058, customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f, desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:42:00,543	设备状态已更新: 576c9d67462d4d7b8be79431353c2f57 → disconnected
2025-12-19 18:42:00,544	移除WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 剩余连接数: 109
2025-12-19 18:42:00,544	RPA断开ws连接：qianniu__木瓜瓜木的小店__木瓜瓜木, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:00,556	设置全局WS连接状态: global_ws_connection:dev:client_message:qianniu__木瓜瓜木的小店__木瓜瓜木
2025-12-19 18:42:00,556	添加WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 当前本地连接数: 110
2025-12-19 18:42:00,566	自动更新用户: 从 10058 到 10058, 店铺-客服: qianniu-木瓜瓜木的小店-木瓜瓜木
2025-12-19 18:42:00,567	ws/client/message  existing_record: equipment_information={'status': 'disconnected', 'channel': 'qianniu', 'assistant_id': '木瓜瓜木', 'client_status': 'online', 'assistant_name': '木瓜瓜木', 'equipment_image': None} created_by='夕谷' created_at=datetime.datetime(2025, 12, 19, 17, 17, 36, 716056) channel='qianniu' expected_status='running' modified_by='夕谷' shop_id='木瓜瓜木的小店' connection_time=datetime.datetime(2025, 12, 19, 18, 42, 0, 296004) creator_id=10058 updated_at=datetime.datetime(2025, 12, 19, 18, 42, 0, 541110) bty_user_id='10058' disconnect_time=datetime.datetime(2025, 12, 19, 18, 42, 0, 536025) customer_agent_config_id='84fe447220aa4b0d907cc26b46cdfe1f' deleted=False robot_name='Robot_木瓜瓜木' disconnect_reason=None quality_inspection_config=None id=443 equipment_information_id='576c9d67462d4d7b8be79431353c2f57' status='disconnected' workspace_id='a042945be289477b9af048014f0f7cdb' robot_settings={'forward_group': {'pre_sales': '售前2'}} client_status='online' agent_mode='auto_reply' client_credentials={'encrypted_at': '2025-12-19T17:17:36.760634', 'client_password': 'YnVndTEyMzQ=', 'client_username': '5pyo55Oc55Oc5pyo'} assistant_id='木瓜瓜木' shared_user_ids=None cloud_desktop_id='aad6a6ab5543484aaf48929cf95e3e2b'
2025-12-19 18:42:00,567	Robot 建立消息上报连接: equipment_information_id=576c9d67462d4d7b8be79431353c2f57, channel=qianniu, shop_id=木瓜瓜木的小店, assistant_id=木瓜瓜木
2025-12-19 18:42:00,568	ws/client/message  desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:42:00,573	ws/client/message  customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:42:00,573	ws/client/message 绑定设备与customer_agent_config - customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:42:00,581	"临时打印 qianniu__木瓜瓜木的小店__木瓜瓜木 异常2：Traceback (most recent call last):
  File ""/app/routers/client/api/client_router.py"", line 583, in copilot_agent_connect
    message = await websocket.receive_text()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 120, in receive_text
    self._raise_on_disconnect(message)
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 114, in _raise_on_disconnect
    raise WebSocketDisconnect(message[""code""], message.get(""reason""))
starlette.websockets.WebSocketDisconnect: (<CloseCode.ABNORMAL_CLOSURE: 1006>, '')
, equipment_information_id=576c9d67462d4d7b8be79431353c2f57"
2025-12-19 18:42:00,593	设备状态已更新: 576c9d67462d4d7b8be79431353c2f57 → disconnected
2025-12-19 18:42:00,593	移除WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 剩余连接数: 109
2025-12-19 18:42:00,594	RPA断开ws连接：qianniu__木瓜瓜木的小店__木瓜瓜木, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:00,633	ws/client/message 新连接请求 - 客户端: 172.16.192.177:23614, channel: qianniu, shop_id: 木瓜瓜木的小店, assistant_id: 木瓜瓜木, workspace_id: a042945be289477b9af048014f0f7cdb, bty_user_id: 10058, customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f, desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:42:00,653	设置全局WS连接状态: global_ws_connection:dev:client_message:qianniu__木瓜瓜木的小店__木瓜瓜木
2025-12-19 18:42:00,653	添加WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 当前本地连接数: 110
2025-12-19 18:42:00,663	自动更新用户: 从 10058 到 10058, 店铺-客服: qianniu-木瓜瓜木的小店-木瓜瓜木
2025-12-19 18:42:00,664	ws/client/message  existing_record: equipment_information={'status': 'disconnected', 'channel': 'qianniu', 'assistant_id': '木瓜瓜木', 'client_status': 'online', 'assistant_name': '木瓜瓜木', 'equipment_image': None} created_by='夕谷' created_at=datetime.datetime(2025, 12, 19, 17, 17, 36, 716056) channel='qianniu' expected_status='running' modified_by='夕谷' shop_id='木瓜瓜木的小店' connection_time=datetime.datetime(2025, 12, 19, 18, 42, 0, 561479) creator_id=10058 updated_at=datetime.datetime(2025, 12, 19, 18, 42, 0, 590466) bty_user_id='10058' disconnect_time=datetime.datetime(2025, 12, 19, 18, 42, 0, 587673) customer_agent_config_id='84fe447220aa4b0d907cc26b46cdfe1f' deleted=False robot_name='Robot_木瓜瓜木' disconnect_reason=None quality_inspection_config=None id=443 equipment_information_id='576c9d67462d4d7b8be79431353c2f57' status='disconnected' workspace_id='a042945be289477b9af048014f0f7cdb' robot_settings={'forward_group': {'pre_sales': '售前2'}} client_status='online' agent_mode='auto_reply' client_credentials={'encrypted_at': '2025-12-19T17:17:36.760634', 'client_password': 'YnVndTEyMzQ=', 'client_username': '5pyo55Oc55Oc5pyo'} assistant_id='木瓜瓜木' shared_user_ids=None cloud_desktop_id='aad6a6ab5543484aaf48929cf95e3e2b'
2025-12-19 18:42:00,664	Robot 建立消息上报连接: equipment_information_id=576c9d67462d4d7b8be79431353c2f57, channel=qianniu, shop_id=木瓜瓜木的小店, assistant_id=木瓜瓜木
2025-12-19 18:42:00,665	ws/client/message  desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:42:00,669	ws/client/message  customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:42:00,669	ws/client/message 绑定设备与customer_agent_config - customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:42:00,676	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': '463c775b-9b79-4f9e-b610-891ee92bad57', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:00,677	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': '83f1863e-1f88-438a-b741-16a5db476aaf', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:00,678	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': 'cb7b7747-2b4f-4a2d-b8a6-ea4104bde109', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:00,697	"临时打印 qianniu__木瓜瓜木的小店__木瓜瓜木 异常2：Traceback (most recent call last):
  File ""/app/routers/client/api/client_router.py"", line 730, in copilot_agent_connect
    message = await websocket.receive_text()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 120, in receive_text
    self._raise_on_disconnect(message)
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 114, in _raise_on_disconnect
    raise WebSocketDisconnect(message[""code""], message.get(""reason""))
starlette.websockets.WebSocketDisconnect: (1000, '')
, equipment_information_id=576c9d67462d4d7b8be79431353c2f57"
2025-12-19 18:42:00,708	设备状态已更新: 576c9d67462d4d7b8be79431353c2f57 → disconnected
2025-12-19 18:42:00,709	移除WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 剩余连接数: 109
2025-12-19 18:42:00,709	RPA断开ws连接：qianniu__木瓜瓜木的小店__木瓜瓜木, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:00,739	ws/client/message 新连接请求 - 客户端: 172.16.199.249:60378, channel: qianniu, shop_id: 木瓜瓜木的小店, assistant_id: 木瓜瓜木, workspace_id: a042945be289477b9af048014f0f7cdb, bty_user_id: 10058, customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f, desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:42:00,766	设置全局WS连接状态: global_ws_connection:dev:client_message:qianniu__木瓜瓜木的小店__木瓜瓜木
2025-12-19 18:42:00,766	添加WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 当前本地连接数: 110
2025-12-19 18:42:00,777	自动更新用户: 从 10058 到 10058, 店铺-客服: qianniu-木瓜瓜木的小店-木瓜瓜木
2025-12-19 18:42:00,777	ws/client/message  existing_record: equipment_information={'status': 'disconnected', 'channel': 'qianniu', 'assistant_id': '木瓜瓜木', 'client_status': 'online', 'assistant_name': '木瓜瓜木', 'equipment_image': None} created_by='夕谷' created_at=datetime.datetime(2025, 12, 19, 17, 17, 36, 716056) channel='qianniu' expected_status='running' modified_by='夕谷' shop_id='木瓜瓜木的小店' connection_time=datetime.datetime(2025, 12, 19, 18, 42, 0, 658537) creator_id=10058 updated_at=datetime.datetime(2025, 12, 19, 18, 42, 0, 705940) bty_user_id='10058' disconnect_time=datetime.datetime(2025, 12, 19, 18, 42, 0, 703379) customer_agent_config_id='84fe447220aa4b0d907cc26b46cdfe1f' deleted=False robot_name='Robot_木瓜瓜木' disconnect_reason=None quality_inspection_config=None id=443 equipment_information_id='576c9d67462d4d7b8be79431353c2f57' status='disconnected' workspace_id='a042945be289477b9af048014f0f7cdb' robot_settings={'forward_group': {'pre_sales': '售前2'}} client_status='online' agent_mode='auto_reply' client_credentials={'encrypted_at': '2025-12-19T17:17:36.760634', 'client_password': 'YnVndTEyMzQ=', 'client_username': '5pyo55Oc55Oc5pyo'} assistant_id='木瓜瓜木' shared_user_ids=None cloud_desktop_id='aad6a6ab5543484aaf48929cf95e3e2b'
2025-12-19 18:42:00,778	Robot 建立消息上报连接: equipment_information_id=576c9d67462d4d7b8be79431353c2f57, channel=qianniu, shop_id=木瓜瓜木的小店, assistant_id=木瓜瓜木
2025-12-19 18:42:00,778	ws/client/message  desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:42:00,783	ws/client/message  customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:42:00,783	ws/client/message 绑定设备与customer_agent_config - customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:42:00,791	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': 'c9b39fe7-e93e-44c1-9c57-b3b6cef62617', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:00,792	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': '5cca7c10-d39a-48ac-b5cb-267fe60f94c6', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:00,794	"临时打印 qianniu__木瓜瓜木的小店__木瓜瓜木 异常2：Traceback (most recent call last):
  File ""/app/routers/client/api/client_router.py"", line 730, in copilot_agent_connect
    message = await websocket.receive_text()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 120, in receive_text
    self._raise_on_disconnect(message)
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 114, in _raise_on_disconnect
    raise WebSocketDisconnect(message[""code""], message.get(""reason""))
starlette.websockets.WebSocketDisconnect: (1000, '')
, equipment_information_id=576c9d67462d4d7b8be79431353c2f57"
2025-12-19 18:42:00,800	ws/client/message 新连接请求 - 客户端: 172.16.192.177:23626, channel: qianniu, shop_id: 木瓜瓜木的小店, assistant_id: 木瓜瓜木, workspace_id: a042945be289477b9af048014f0f7cdb, bty_user_id: 10058, customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f, desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:42:00,809	设备状态已更新: 576c9d67462d4d7b8be79431353c2f57 → disconnected
2025-12-19 18:42:00,810	移除WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 剩余连接数: 109
2025-12-19 18:42:00,810	RPA断开ws连接：qianniu__木瓜瓜木的小店__木瓜瓜木, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:00,820	设置全局WS连接状态: global_ws_connection:dev:client_message:qianniu__木瓜瓜木的小店__木瓜瓜木
2025-12-19 18:42:00,820	添加WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 当前本地连接数: 110
2025-12-19 18:42:00,830	自动更新用户: 从 10058 到 10058, 店铺-客服: qianniu-木瓜瓜木的小店-木瓜瓜木
2025-12-19 18:42:00,830	ws/client/message  existing_record: equipment_information={'status': 'disconnected', 'channel': 'qianniu', 'assistant_id': '木瓜瓜木', 'client_status': 'online', 'assistant_name': '木瓜瓜木', 'equipment_image': None} created_by='夕谷' created_at=datetime.datetime(2025, 12, 19, 17, 17, 36, 716056) channel='qianniu' expected_status='running' modified_by='夕谷' shop_id='木瓜瓜木的小店' connection_time=datetime.datetime(2025, 12, 19, 18, 42, 0, 771699) creator_id=10058 updated_at=datetime.datetime(2025, 12, 19, 18, 42, 0, 815271) bty_user_id='10058' disconnect_time=datetime.datetime(2025, 12, 19, 18, 42, 0, 803830) customer_agent_config_id='84fe447220aa4b0d907cc26b46cdfe1f' deleted=False robot_name='Robot_木瓜瓜木' disconnect_reason=None quality_inspection_config=None id=443 equipment_information_id='576c9d67462d4d7b8be79431353c2f57' status='disconnected' workspace_id='a042945be289477b9af048014f0f7cdb' robot_settings={'forward_group': {'pre_sales': '售前2'}} client_status='online' agent_mode='auto_reply' client_credentials={'encrypted_at': '2025-12-19T17:17:36.760634', 'client_password': 'YnVndTEyMzQ=', 'client_username': '5pyo55Oc55Oc5pyo'} assistant_id='木瓜瓜木' shared_user_ids=None cloud_desktop_id='aad6a6ab5543484aaf48929cf95e3e2b'
2025-12-19 18:42:00,831	Robot 建立消息上报连接: equipment_information_id=576c9d67462d4d7b8be79431353c2f57, channel=qianniu, shop_id=木瓜瓜木的小店, assistant_id=木瓜瓜木
2025-12-19 18:42:00,831	ws/client/message  desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:42:00,833	ws/client/message 新连接请求 - 客户端: 172.16.199.249:60386, channel: qianniu, shop_id: 木瓜瓜木的小店, assistant_id: 木瓜瓜木, workspace_id: a042945be289477b9af048014f0f7cdb, bty_user_id: 10058, customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f, desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:42:00,838	ws/client/message  customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:42:00,838	ws/client/message 绑定设备与customer_agent_config - customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:42:00,847	"临时打印 qianniu__木瓜瓜木的小店__木瓜瓜木 异常2：Traceback (most recent call last):
  File ""/app/routers/client/api/client_router.py"", line 583, in copilot_agent_connect
    message = await websocket.receive_text()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 120, in receive_text
    self._raise_on_disconnect(message)
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 114, in _raise_on_disconnect
    raise WebSocketDisconnect(message[""code""], message.get(""reason""))
starlette.websockets.WebSocketDisconnect: (<CloseCode.ABNORMAL_CLOSURE: 1006>, '')
, equipment_information_id=576c9d67462d4d7b8be79431353c2f57"
2025-12-19 18:42:00,856	设置全局WS连接状态: global_ws_connection:dev:client_message:qianniu__木瓜瓜木的小店__木瓜瓜木
2025-12-19 18:42:00,857	添加WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 当前本地连接数: 111
2025-12-19 18:42:00,859	设备状态已更新: 576c9d67462d4d7b8be79431353c2f57 → disconnected
2025-12-19 18:42:00,860	移除WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 剩余连接数: 110
2025-12-19 18:42:00,860	RPA断开ws连接：qianniu__木瓜瓜木的小店__木瓜瓜木, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:00,868	自动更新用户: 从 10058 到 10058, 店铺-客服: qianniu-木瓜瓜木的小店-木瓜瓜木
2025-12-19 18:42:00,868	ws/client/message  existing_record: equipment_information={'status': 'disconnected', 'channel': 'qianniu', 'assistant_id': '木瓜瓜木', 'client_status': 'online', 'assistant_name': '木瓜瓜木', 'equipment_image': None} created_by='夕谷' created_at=datetime.datetime(2025, 12, 19, 17, 17, 36, 716056) channel='qianniu' expected_status='running' modified_by='夕谷' shop_id='木瓜瓜木的小店' connection_time=datetime.datetime(2025, 12, 19, 18, 42, 0, 825340) creator_id=10058 updated_at=datetime.datetime(2025, 12, 19, 18, 42, 0, 856872) bty_user_id='10058' disconnect_time=datetime.datetime(2025, 12, 19, 18, 42, 0, 854316) customer_agent_config_id='84fe447220aa4b0d907cc26b46cdfe1f' deleted=False robot_name='Robot_木瓜瓜木' disconnect_reason=None quality_inspection_config=None id=443 equipment_information_id='576c9d67462d4d7b8be79431353c2f57' status='disconnected' workspace_id='a042945be289477b9af048014f0f7cdb' robot_settings={'forward_group': {'pre_sales': '售前2'}} client_status='online' agent_mode='auto_reply' client_credentials={'encrypted_at': '2025-12-19T17:17:36.760634', 'client_password': 'YnVndTEyMzQ=', 'client_username': '5pyo55Oc55Oc5pyo'} assistant_id='木瓜瓜木' shared_user_ids=None cloud_desktop_id='aad6a6ab5543484aaf48929cf95e3e2b'
2025-12-19 18:42:00,869	Robot 建立消息上报连接: equipment_information_id=576c9d67462d4d7b8be79431353c2f57, channel=qianniu, shop_id=木瓜瓜木的小店, assistant_id=木瓜瓜木
2025-12-19 18:42:00,869	ws/client/message  desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:42:00,874	ws/client/message  customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:42:00,874	ws/client/message 绑定设备与customer_agent_config - customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:42:00,881	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': '34e5547b-89ff-4296-abf0-137b0f846c7f', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:00,882	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': '80ca4b89-5ebd-486b-8a1d-b36fd1916ca8', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:00,985	"临时打印 qianniu__木瓜瓜木的小店__木瓜瓜木 异常2：Traceback (most recent call last):
  File ""/app/routers/client/api/client_router.py"", line 730, in copilot_agent_connect
    message = await websocket.receive_text()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 120, in receive_text
    self._raise_on_disconnect(message)
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 114, in _raise_on_disconnect
    raise WebSocketDisconnect(message[""code""], message.get(""reason""))
starlette.websockets.WebSocketDisconnect: (1000, '')
, equipment_information_id=576c9d67462d4d7b8be79431353c2f57"
2025-12-19 18:42:00,997	ws/client/message 新连接请求 - 客户端: 172.16.192.177:23642, channel: qianniu, shop_id: 木瓜瓜木的小店, assistant_id: 木瓜瓜木, workspace_id: a042945be289477b9af048014f0f7cdb, bty_user_id: 10058, customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f, desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:42:01,101	
2025-12-19 18:42:01,455	
2025-12-19 18:42:01,787	
2025-12-19 18:42:00,999	设备状态已更新: 576c9d67462d4d7b8be79431353c2f57 → disconnected
2025-12-19 18:42:01,001	移除WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 剩余连接数: 109
2025-12-19 18:42:01,001	RPA断开ws连接：qianniu__木瓜瓜木的小店__木瓜瓜木, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:01,020	设置全局WS连接状态: global_ws_connection:dev:client_message:qianniu__木瓜瓜木的小店__木瓜瓜木
2025-12-19 18:42:01,020	添加WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 当前本地连接数: 110
2025-12-19 18:42:01,032	自动更新用户: 从 10058 到 10058, 店铺-客服: qianniu-木瓜瓜木的小店-木瓜瓜木
2025-12-19 18:42:01,032	ws/client/message  existing_record: equipment_information={'status': 'disconnected', 'channel': 'qianniu', 'assistant_id': '木瓜瓜木', 'client_status': 'online', 'assistant_name': '木瓜瓜木', 'equipment_image': None} created_by='夕谷' created_at=datetime.datetime(2025, 12, 19, 17, 17, 36, 716056) channel='qianniu' expected_status='running' modified_by='夕谷' shop_id='木瓜瓜木的小店' connection_time=datetime.datetime(2025, 12, 19, 18, 42, 0, 863356) creator_id=10058 updated_at=datetime.datetime(2025, 12, 19, 18, 42, 0, 994929) bty_user_id='10058' disconnect_time=datetime.datetime(2025, 12, 19, 18, 42, 0, 991923) customer_agent_config_id='84fe447220aa4b0d907cc26b46cdfe1f' deleted=False robot_name='Robot_木瓜瓜木' disconnect_reason=None quality_inspection_config=None id=443 equipment_information_id='576c9d67462d4d7b8be79431353c2f57' status='disconnected' workspace_id='a042945be289477b9af048014f0f7cdb' robot_settings={'forward_group': {'pre_sales': '售前2'}} client_status='online' agent_mode='auto_reply' client_credentials={'encrypted_at': '2025-12-19T17:17:36.760634', 'client_password': 'YnVndTEyMzQ=', 'client_username': '5pyo55Oc55Oc5pyo'} assistant_id='木瓜瓜木' shared_user_ids=None cloud_desktop_id='aad6a6ab5543484aaf48929cf95e3e2b'
2025-12-19 18:42:01,033	Robot 建立消息上报连接: equipment_information_id=576c9d67462d4d7b8be79431353c2f57, channel=qianniu, shop_id=木瓜瓜木的小店, assistant_id=木瓜瓜木
2025-12-19 18:42:01,033	ws/client/message  desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:42:01,038	ws/client/message  customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:42:01,038	ws/client/message 绑定设备与customer_agent_config - customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:42:01,046	"临时打印 qianniu__木瓜瓜木的小店__木瓜瓜木 异常2：Traceback (most recent call last):
  File ""/app/routers/client/api/client_router.py"", line 583, in copilot_agent_connect
    message = await websocket.receive_text()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 120, in receive_text
    self._raise_on_disconnect(message)
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 114, in _raise_on_disconnect
    raise WebSocketDisconnect(message[""code""], message.get(""reason""))
starlette.websockets.WebSocketDisconnect: (<CloseCode.ABNORMAL_CLOSURE: 1006>, '')
, equipment_information_id=576c9d67462d4d7b8be79431353c2f57"
2025-12-19 18:42:01,057	设备状态已更新: 576c9d67462d4d7b8be79431353c2f57 → disconnected
2025-12-19 18:42:01,058	移除WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 剩余连接数: 109
2025-12-19 18:42:01,058	RPA断开ws连接：qianniu__木瓜瓜木的小店__木瓜瓜木, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:01,094	ws/client/message 新连接请求 - 客户端: 172.16.199.249:60402, channel: qianniu, shop_id: 木瓜瓜木的小店, assistant_id: 木瓜瓜木, workspace_id: a042945be289477b9af048014f0f7cdb, bty_user_id: 10058, customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f, desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:42:01,122	设置全局WS连接状态: global_ws_connection:dev:client_message:qianniu__木瓜瓜木的小店__木瓜瓜木
2025-12-19 18:42:01,122	添加WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 当前本地连接数: 110
2025-12-19 18:42:01,132	自动更新用户: 从 10058 到 10058, 店铺-客服: qianniu-木瓜瓜木的小店-木瓜瓜木
2025-12-19 18:42:01,132	ws/client/message  existing_record: equipment_information={'status': 'disconnected', 'channel': 'qianniu', 'assistant_id': '木瓜瓜木', 'client_status': 'online', 'assistant_name': '木瓜瓜木', 'equipment_image': None} created_by='夕谷' created_at=datetime.datetime(2025, 12, 19, 17, 17, 36, 716056) channel='qianniu' expected_status='running' modified_by='夕谷' shop_id='木瓜瓜木的小店' connection_time=datetime.datetime(2025, 12, 19, 18, 42, 1, 25727) creator_id=10058 updated_at=datetime.datetime(2025, 12, 19, 18, 42, 1, 54846) bty_user_id='10058' disconnect_time=datetime.datetime(2025, 12, 19, 18, 42, 1, 52094) customer_agent_config_id='84fe447220aa4b0d907cc26b46cdfe1f' deleted=False robot_name='Robot_木瓜瓜木' disconnect_reason=None quality_inspection_config=None id=443 equipment_information_id='576c9d67462d4d7b8be79431353c2f57' status='disconnected' workspace_id='a042945be289477b9af048014f0f7cdb' robot_settings={'forward_group': {'pre_sales': '售前2'}} client_status='online' agent_mode='auto_reply' client_credentials={'encrypted_at': '2025-12-19T17:17:36.760634', 'client_password': 'YnVndTEyMzQ=', 'client_username': '5pyo55Oc55Oc5pyo'} assistant_id='木瓜瓜木' shared_user_ids=None cloud_desktop_id='aad6a6ab5543484aaf48929cf95e3e2b'
2025-12-19 18:42:01,133	Robot 建立消息上报连接: equipment_information_id=576c9d67462d4d7b8be79431353c2f57, channel=qianniu, shop_id=木瓜瓜木的小店, assistant_id=木瓜瓜木
2025-12-19 18:42:01,133	ws/client/message  desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:42:01,138	ws/client/message  customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:42:01,138	ws/client/message 绑定设备与customer_agent_config - customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:42:01,145	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': '73250061-c67f-4dc4-8698-216e6719c7dc', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:01,146	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': 'be612290-e93c-4625-8c3e-d589f90f4879', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:01,175	临时打印 设备上报 qianniu__木瓜瓜木的小店__木瓜瓜木 消息内容：{'data': {'equipment_image': None}, 'request_id': '4172a58c-b043-4c72-9a92-2543fd7c2689', 'type': 'equipment-reporting', 'require_ack': False}, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:01,316	"临时打印 qianniu__木瓜瓜木的小店__木瓜瓜木 异常2：Traceback (most recent call last):
  File ""/app/routers/client/api/client_router.py"", line 730, in copilot_agent_connect
    message = await websocket.receive_text()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 120, in receive_text
    self._raise_on_disconnect(message)
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 114, in _raise_on_disconnect
    raise WebSocketDisconnect(message[""code""], message.get(""reason""))
starlette.websockets.WebSocketDisconnect: (1000, '')
, equipment_information_id=576c9d67462d4d7b8be79431353c2f57"
2025-12-19 18:42:01,318	ws/client/message 新连接请求 - 客户端: 172.16.199.249:60408, channel: qianniu, shop_id: 木瓜瓜木的小店, assistant_id: 木瓜瓜木, workspace_id: a042945be289477b9af048014f0f7cdb, bty_user_id: 10058, customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f, desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:42:01,329	设备状态已更新: 576c9d67462d4d7b8be79431353c2f57 → disconnected
2025-12-19 18:42:01,330	移除WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 剩余连接数: 109
2025-12-19 18:42:01,331	RPA断开ws连接：qianniu__木瓜瓜木的小店__木瓜瓜木, equipment_information_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:01,338	设置全局WS连接状态: global_ws_connection:dev:client_message:qianniu__木瓜瓜木的小店__木瓜瓜木
2025-12-19 18:42:01,338	添加WebSocket连接: qianniu__木瓜瓜木的小店__木瓜瓜木, 当前本地连接数: 110
2025-12-19 18:42:01,349	自动更新用户: 从 10058 到 10058, 店铺-客服: qianniu-木瓜瓜木的小店-木瓜瓜木
2025-12-19 18:42:01,349	ws/client/message  existing_record: equipment_information={'status': 'disconnected', 'channel': 'qianniu', 'assistant_id': '木瓜瓜木', 'client_status': 'online', 'assistant_name': '木瓜瓜木', 'equipment_image': None} created_by='夕谷' created_at=datetime.datetime(2025, 12, 19, 17, 17, 36, 716056) channel='qianniu' expected_status='running' modified_by='夕谷' shop_id='木瓜瓜木的小店' connection_time=datetime.datetime(2025, 12, 19, 18, 42, 1, 127273) creator_id=10058 updated_at=datetime.datetime(2025, 12, 19, 18, 42, 1, 327024) bty_user_id='10058' disconnect_time=datetime.datetime(2025, 12, 19, 18, 42, 1, 324441) customer_agent_config_id='84fe447220aa4b0d907cc26b46cdfe1f' deleted=False robot_name='Robot_木瓜瓜木' disconnect_reason=None quality_inspection_config=None id=443 equipment_information_id='576c9d67462d4d7b8be79431353c2f57' status='disconnected' workspace_id='a042945be289477b9af048014f0f7cdb' robot_settings={'forward_group': {'pre_sales': '售前2'}} client_status='online' agent_mode='auto_reply' client_credentials={'encrypted_at': '2025-12-19T17:17:36.760634', 'client_password': 'YnVndTEyMzQ=', 'client_username': '5pyo55Oc55Oc5pyo'} assistant_id='木瓜瓜木' shared_user_ids=None cloud_desktop_id='aad6a6ab5543484aaf48929cf95e3e2b'
2025-12-19 18:42:01,350	Robot 建立消息上报连接: equipment_information_id=576c9d67462d4d7b8be79431353c2f57, channel=qianniu, shop_id=木瓜瓜木的小店, assistant_id=木瓜瓜木
2025-12-19 18:42:01,350	ws/client/message  desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:42:01,352	ws/client/message 新连接请求 - 客户端: 172.16.192.177:23648, channel: qianniu, shop_id: 木瓜瓜木的小店, assistant_id: 木瓜瓜木, workspace_id: a042945be289477b9af048014f0f7cdb, bty_user_id: 10058, customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f, desktop_id: aad6a6ab5543484aaf48929cf95e3e2b
2025-12-19 18:42:01,356	ws/client/message  customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:42:01,357	ws/client/message 绑定设备与customer_agent_config - customer_agent_id: 84fe447220aa4b0d907cc26b46cdfe1f
2025-12-19 18:42:01,364	"临时打印 qianniu__木瓜瓜木的小店__木瓜瓜木 异常2：Traceback (most recent call last):
  File ""/app/routers/client/api/client_router.py"", line 583, in copilot_agent_connect
    message = await websocket.receive_text()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 120, in receive_text
    self._raise_on_disconnect(message)
  File ""/usr/local/lib/python3.12/site-packages/starlette/websockets.py"", line 114, in _raise_on_disconnect
    raise WebSocketDisconnect(message[""code""], message.get(""reason""))
starlette.websockets.WebSocketDisconnect: (<CloseCode.ABNORMAL_CLOSURE: 1006>, '')
, equipment_information_id=576c9d67462d4d7b8be79431353c2f57"
