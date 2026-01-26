
2025-12-19 18:42:01 EquipmentStatusHelper::: 开始发送设备状态消息到 WebSocket
2025-12-19 18:42:01 [DEBUG] EquipmentStatusHelper::: 开始发送设备状态消息到 WebSocket
2025-12-19 18:42:01 WebSocketMainManage::OnWebSocketOpened: 设备状态上报完成，等待业务消息
2025-12-19 18:42:01 WebSocketService::CreateServiceAsync: 开始监听服务器消息
2025-12-19 18:42:01 WebSocketService::ReceiveMessages: 启动消息接收循环: Open
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 连接结果: 成功
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 连接启动流程结束，_isConnecting 标记已重置
2025-12-19 18:42:01 WebSocketMainManage::OnWebSocketReconnected: 检测到WebSocket重连成功事件，恢复内部服务
2025-12-19 18:42:01 ConnectionStateManager::IsRunning: WebSocket运行状态变更为: True
2025-12-19 18:42:01 HeartbeatManager::Start: 心跳管理器已启动，开始参与连接状态维护
2025-12-19 18:42:01 RobotHealthReportService::Start: 健康状态上报已经在运行中
2025-12-19 18:42:01 ScreenService::Start: 截图上报已经在运行中
2025-12-19 18:42:01 WebSocketService::AttemptReconnect: 重连成功，自动处理 1 条待发送消息
2025-12-19 18:42:01 WebSocketService::ProcessPendingMessages: 队列处理完成，共发送 2 条消息
2025-12-19 18:42:01 HeartbeatManager::HandleTimerTickAsync: 开始执行心跳检测循环
2025-12-19 18:42:01 HeartbeatManager::HandleTimerTickAsync: 当前WebSocket连接状态: State=Open, AutoReconnect=True, IsConnecting=False, IsClosing=False, IsReceiving=True, PendingMessages=0, ReconnectAttempts=0, CancellationActive=True
2025-12-19 18:42:01 HeartbeatManager::ProcessHeartbeatLogicAsync: 当前计数 - 本地心跳:3, 服务端心跳:18
2025-12-19 18:42:01 HeartbeatManager::HandleTimerTickAsync: 心跳检测循环结束
2025-12-19 18:42:01 WebSocketService::AttemptReconnect: 执行第 1 次重连，目标地址: ws://dev-customer-servhub-api.betteryeah.com/v1/ws/client/message?workspace_id=a042945be289477b9af048014f0f7cdb&access_key=YTA0Mjk0NWJlMjg5NDc3YjlhZjA0ODAxNGYwZjdjZGIsMTAwNTgsMTc2NDA1MTU0MjMzMQ==&bty_user_id=10058&assistant_id=木瓜瓜木&channel=qianniu&shop_id=木瓜瓜木的小店&customer_agent_id=84fe447220aa4b0d907cc26b46cdfe1f&desktop_id=aad6a6ab5543484aaf48929cf95e3e2b&env=dev&equipment_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 启动WebSocket服务: ws://dev-customer-servhub-api.betteryeah.com/v1/ws/client/message?workspace_id=a042945be289477b9af048014f0f7cdb&access_key=YTA0Mjk0NWJlMjg5NDc3YjlhZjA0ODAxNGYwZjdjZGIsMTAwNTgsMTc2NDA1MTU0MjMzMQ==&bty_user_id=10058&assistant_id=木瓜瓜木&channel=qianniu&shop_id=木瓜瓜木的小店&customer_agent_id=84fe447220aa4b0d907cc26b46cdfe1f&desktop_id=aad6a6ab5543484aaf48929cf95e3e2b&env=dev&equipment_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 当前已有连接实例状态: Open
2025-12-19 18:42:01 WebSocketService::HandleExistingConnectionAsync: 发现仍然存在的连接，状态: Open
2025-12-19 18:42:01 WebSocketService::HandleExistingConnectionAsync: 旧连接状态为 Open，触发关闭流程
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 开始关闭服务，是否通知: False，是否禁用自动重连: False
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 旧连接处理完成，准备创建新连接
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 已取消并释放旧的取消标记源
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 取消标记源引用已重置为 null
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 取消标记源已清理
2025-12-19 18:42:01 WebSocketService::CreateServiceAsync: 开始建立连接: ws://dev-customer-servhub-api.betteryeah.com/v1/ws/client/message?workspace_id=a042945be289477b9af048014f0f7cdb&access_key=YTA0Mjk0NWJlMjg5NDc3YjlhZjA0ODAxNGYwZjdjZGIsMTAwNTgsMTc2NDA1MTU0MjMzMQ==&bty_user_id=10058&assistant_id=木瓜瓜木&channel=qianniu&shop_id=木瓜瓜木的小店&customer_agent_id=84fe447220aa4b0d907cc26b46cdfe1f&desktop_id=aad6a6ab5543484aaf48929cf95e3e2b&env=dev&equipment_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:01 WebSocketService::CloseWebSocketAsync: WebSocket已发送正常关闭帧
2025-12-19 18:42:01 MessageProcessor::ReceiveMessageAsync: 服务器主动关闭连接: NormalClosure, 
2025-12-19 18:42:01 [ERROR] WebSocketService::HandleConnectionClosed: 服务器主动关闭连接 - WebSocket异常断开
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 已取消并释放旧的取消标记源
2025-12-19 18:42:01 WebSocketService::StateChange: 服务器主动关闭: WebSocket状态变化 Open -> Closed
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 开始关闭服务，是否通知: True，是否禁用自动重连: False
2025-12-19 18:42:01 [ERROR] WebSocketService::CreateServiceAsync: 连接失败 - WebSocket异常断开: A task was canceled.
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 已触发关闭事件通知
2025-12-19 18:42:01 WebSocketMainManage::OnWebSocketError: WebSocket错误: Receive
2025-12-19 18:42:01 WebSocketMainManage::OnWebSocketClosed: WebSocket连接已断开，上报设备状态为 offline
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 取消标记源引用已重置为 null
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 开始关闭服务，是否通知: True，是否禁用自动重连: False
2025-12-19 18:42:01 WebSocketService::StartReceiveLoop: 接收循环结束，_isReceive=False，当前连接状态: Closed
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 已取消并释放旧的取消标记源
2025-12-19 18:42:01 WebSocketService::HandleConnectionClosed: 已发送钉钉连接关闭通知
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 已触发关闭事件通知
2025-12-19 18:42:01 EquipmentStatusHelper::: ReportStatus 开始上报设备状态 
2025-12-19 18:42:01 WebSocketService::DisposeWebSocket: WebSocket实例已成功释放
2025-12-19 18:42:01 WebSocketMainManage::OnWebSocketClosed: WebSocket连接已断开，上报设备状态为 offline
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 连接结果: 失败
2025-12-19 18:42:01 [DEBUG] EquipmentStatusHelper::: ReportStatus 开始上报设备状态 
2025-12-19 18:42:01 EquipmentStatusHelper::: ReportStatus 开始上报设备状态 
2025-12-19 18:42:01 EquipmentStatusHelper::: 序列化后的消息内容: {
2025-12-19 18:42:01   "data": {
2025-12-19 18:42:01     "equipment_image": null
2025-12-19 18:42:01   },
2025-12-19 18:42:01   "request_id": "a4395b39-67cd-4d61-b87e-13283d1cb04b",
2025-12-19 18:42:01   "type": "equipment-reporting",
2025-12-19 18:42:01   "require_ack": false
2025-12-19 18:42:01 }
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 底层连接资源释放完成
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 取消标记源引用已重置为 null
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 连接启动流程结束，_isConnecting 标记已重置
2025-12-19 18:42:01 [DEBUG] EquipmentStatusHelper::: ReportStatus 开始上报设备状态 
2025-12-19 18:42:01 EquipmentStatusHelper::: 序列化后的消息内容: {
2025-12-19 18:42:01   "data": {
2025-12-19 18:42:01     "equipment_image": null
2025-12-19 18:42:01   },
2025-12-19 18:42:01   "request_id": "2c9c3c95-82e3-4974-bada-e4b2f8632100",
2025-12-19 18:42:01   "type": "equipment-reporting",
2025-12-19 18:42:01   "require_ack": false
2025-12-19 18:42:01 }
2025-12-19 18:42:01 [DEBUG] EquipmentStatusHelper::: 序列化后的消息内容: {
2025-12-19 18:42:01   "data": {
2025-12-19 18:42:01     "equipment_image": null
2025-12-19 18:42:01   },
2025-12-19 18:42:01   "request_id": "a4395b39-67cd-4d61-b87e-13283d1cb04b",
2025-12-19 18:42:01   "type": "equipment-reporting",
2025-12-19 18:42:01   "require_ack": false
2025-12-19 18:42:01 }
2025-12-19 18:42:01 EquipmentStatusHelper::: 开始发送设备状态消息到 WebSocket
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 关闭流程结束
2025-12-19 18:42:01 WebSocketService::AttemptReconnect: 第 1 次重连失败
2025-12-19 18:42:01 [DEBUG] EquipmentStatusHelper::: 序列化后的消息内容: {
2025-12-19 18:42:01   "data": {
2025-12-19 18:42:01     "equipment_image": null
2025-12-19 18:42:01   },
2025-12-19 18:42:01   "request_id": "2c9c3c95-82e3-4974-bada-e4b2f8632100",
2025-12-19 18:42:01   "type": "equipment-reporting",
2025-12-19 18:42:01   "require_ack": false
2025-12-19 18:42:01 }
2025-12-19 18:42:01 EquipmentStatusHelper::: 开始发送设备状态消息到 WebSocket
2025-12-19 18:42:01 [DEBUG] EquipmentStatusHelper::: 开始发送设备状态消息到 WebSocket
2025-12-19 18:42:01 WebSocketMainManage::OnWebSocketClosed: 关闭通知事件已触发
2025-12-19 18:42:01 [DEBUG] EquipmentStatusHelper::: 开始发送设备状态消息到 WebSocket
2025-12-19 18:42:01 WebSocketService::DisposeWebSocket: WebSocket实例已成功释放
2025-12-19 18:42:01 WebSocketMainManage::OnWebSocketClosed: 关闭通知事件已触发
2025-12-19 18:42:01 WebSocketService::AttemptReconnect: 第 1 次重连尝试，1000毫秒后开始
2025-12-19 18:42:01 WebSocketService::SendDataAsync: 连接断开，消息加入待发送队列
2025-12-19 18:42:01 WebSocketService::SendDataAsync: 连接断开，消息加入待发送队列
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 已取消并释放旧的取消标记源
2025-12-19 18:42:01 WebSocketMainManage::SendMessageAsync: 消息发送失败
2025-12-19 18:42:01 WebSocketMainManage::SendMessageAsync: 消息发送失败
2025-12-19 18:42:01 WebSocketService::AttemptReconnect: 第 2 次重连尝试，2000毫秒后开始
2025-12-19 18:42:01 WebSocketService::AttemptReconnect: 第 3 次重连尝试，5000毫秒后开始
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 底层连接资源释放完成
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 取消标记源引用已重置为 null
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 关闭流程结束
2025-12-19 18:42:01 WebSocketService::DisposeWebSocket: WebSocket实例已成功释放
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 底层连接资源释放完成
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 关闭流程结束
2025-12-19 18:42:01 WebSocketService::AttemptReconnect: 执行第 2 次重连，目标地址: ws://dev-customer-servhub-api.betteryeah.com/v1/ws/client/message?workspace_id=a042945be289477b9af048014f0f7cdb&access_key=YTA0Mjk0NWJlMjg5NDc3YjlhZjA0ODAxNGYwZjdjZGIsMTAwNTgsMTc2NDA1MTU0MjMzMQ==&bty_user_id=10058&assistant_id=木瓜瓜木&channel=qianniu&shop_id=木瓜瓜木的小店&customer_agent_id=84fe447220aa4b0d907cc26b46cdfe1f&desktop_id=aad6a6ab5543484aaf48929cf95e3e2b&env=dev&equipment_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 启动WebSocket服务: ws://dev-customer-servhub-api.betteryeah.com/v1/ws/client/message?workspace_id=a042945be289477b9af048014f0f7cdb&access_key=YTA0Mjk0NWJlMjg5NDc3YjlhZjA0ODAxNGYwZjdjZGIsMTAwNTgsMTc2NDA1MTU0MjMzMQ==&bty_user_id=10058&assistant_id=木瓜瓜木&channel=qianniu&shop_id=木瓜瓜木的小店&customer_agent_id=84fe447220aa4b0d907cc26b46cdfe1f&desktop_id=aad6a6ab5543484aaf48929cf95e3e2b&env=dev&equipment_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 当前已有连接实例状态: Null
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 旧连接处理完成，准备创建新连接
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 已取消并释放旧的取消标记源
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 取消标记源引用已重置为 null
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 取消标记源已清理
2025-12-19 18:42:01 WebSocketService::CreateServiceAsync: 开始建立连接: ws://dev-customer-servhub-api.betteryeah.com/v1/ws/client/message?workspace_id=a042945be289477b9af048014f0f7cdb&access_key=YTA0Mjk0NWJlMjg5NDc3YjlhZjA0ODAxNGYwZjdjZGIsMTAwNTgsMTc2NDA1MTU0MjMzMQ==&bty_user_id=10058&assistant_id=木瓜瓜木&channel=qianniu&shop_id=木瓜瓜木的小店&customer_agent_id=84fe447220aa4b0d907cc26b46cdfe1f&desktop_id=aad6a6ab5543484aaf48929cf95e3e2b&env=dev&equipment_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:01 WebSocketService::CreateServiceAsync: 连接成功: Open
2025-12-19 18:42:01 WebSocketService::StateChange: 连接建立: WebSocket状态变化 Unknown -> Open
2025-12-19 18:42:01 WebSocketMainManage::OnWebSocketOpened: WebSocket连接已建立，上报设备状态为 running
2025-12-19 18:42:01 EquipmentStatusHelper::: ReportStatus 开始上报设备状态 
2025-12-19 18:42:01 [DEBUG] EquipmentStatusHelper::: ReportStatus 开始上报设备状态 
2025-12-19 18:42:01 EquipmentStatusHelper::: 序列化后的消息内容: {
2025-12-19 18:42:01   "data": {
2025-12-19 18:42:01     "equipment_image": null
2025-12-19 18:42:01   },
2025-12-19 18:42:01   "request_id": "6edc7a9b-c4b6-42e3-9302-765a13d039d8",
2025-12-19 18:42:01   "type": "equipment-reporting",
2025-12-19 18:42:01   "require_ack": false
2025-12-19 18:42:01 }
2025-12-19 18:42:01 [DEBUG] EquipmentStatusHelper::: 序列化后的消息内容: {
2025-12-19 18:42:01   "data": {
2025-12-19 18:42:01     "equipment_image": null
2025-12-19 18:42:01   },
2025-12-19 18:42:01   "request_id": "6edc7a9b-c4b6-42e3-9302-765a13d039d8",
2025-12-19 18:42:01   "type": "equipment-reporting",
2025-12-19 18:42:01   "require_ack": false
2025-12-19 18:42:01 }
2025-12-19 18:42:01 EquipmentStatusHelper::: 开始发送设备状态消息到 WebSocket
2025-12-19 18:42:01 [DEBUG] EquipmentStatusHelper::: 开始发送设备状态消息到 WebSocket
2025-12-19 18:42:01 WebSocketMainManage::OnWebSocketOpened: 设备状态上报完成，等待业务消息
2025-12-19 18:42:01 WebSocketService::CreateServiceAsync: 开始监听服务器消息
2025-12-19 18:42:01 WebSocketService::ReceiveMessages: 启动消息接收循环: Open
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 连接结果: 成功
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 连接启动流程结束，_isConnecting 标记已重置
2025-12-19 18:42:01 WebSocketMainManage::OnWebSocketReconnected: 检测到WebSocket重连成功事件，恢复内部服务
2025-12-19 18:42:01 ConnectionStateManager::IsRunning: WebSocket运行状态变更为: True
2025-12-19 18:42:01 HeartbeatManager::Start: 心跳管理器已启动，开始参与连接状态维护
2025-12-19 18:42:01 RobotHealthReportService::Start: 健康状态上报已经在运行中
2025-12-19 18:42:01 ScreenService::Start: 截图上报已经在运行中
2025-12-19 18:42:01 WebSocketService::AttemptReconnect: 重连成功，自动处理 1 条待发送消息
2025-12-19 18:42:01 WebSocketService::ProcessPendingMessages: 队列处理完成，共发送 2 条消息
2025-12-19 18:42:01 WebSocketService::AttemptReconnect: 执行第 3 次重连，目标地址: ws://dev-customer-servhub-api.betteryeah.com/v1/ws/client/message?workspace_id=a042945be289477b9af048014f0f7cdb&access_key=YTA0Mjk0NWJlMjg5NDc3YjlhZjA0ODAxNGYwZjdjZGIsMTAwNTgsMTc2NDA1MTU0MjMzMQ==&bty_user_id=10058&assistant_id=木瓜瓜木&channel=qianniu&shop_id=木瓜瓜木的小店&customer_agent_id=84fe447220aa4b0d907cc26b46cdfe1f&desktop_id=aad6a6ab5543484aaf48929cf95e3e2b&env=dev&equipment_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 启动WebSocket服务: ws://dev-customer-servhub-api.betteryeah.com/v1/ws/client/message?workspace_id=a042945be289477b9af048014f0f7cdb&access_key=YTA0Mjk0NWJlMjg5NDc3YjlhZjA0ODAxNGYwZjdjZGIsMTAwNTgsMTc2NDA1MTU0MjMzMQ==&bty_user_id=10058&assistant_id=木瓜瓜木&channel=qianniu&shop_id=木瓜瓜木的小店&customer_agent_id=84fe447220aa4b0d907cc26b46cdfe1f&desktop_id=aad6a6ab5543484aaf48929cf95e3e2b&env=dev&equipment_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 当前已有连接实例状态: Open
2025-12-19 18:42:01 WebSocketService::HandleExistingConnectionAsync: 发现仍然存在的连接，状态: Open
2025-12-19 18:42:01 WebSocketService::HandleExistingConnectionAsync: 旧连接状态为 Open，触发关闭流程
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 开始关闭服务，是否通知: False，是否禁用自动重连: False
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 旧连接处理完成，准备创建新连接
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 已取消并释放旧的取消标记源
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 取消标记源引用已重置为 null
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 取消标记源已清理
2025-12-19 18:42:01 WebSocketService::CreateServiceAsync: 开始建立连接: ws://dev-customer-servhub-api.betteryeah.com/v1/ws/client/message?workspace_id=a042945be289477b9af048014f0f7cdb&access_key=YTA0Mjk0NWJlMjg5NDc3YjlhZjA0ODAxNGYwZjdjZGIsMTAwNTgsMTc2NDA1MTU0MjMzMQ==&bty_user_id=10058&assistant_id=木瓜瓜木&channel=qianniu&shop_id=木瓜瓜木的小店&customer_agent_id=84fe447220aa4b0d907cc26b46cdfe1f&desktop_id=aad6a6ab5543484aaf48929cf95e3e2b&env=dev&equipment_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:01 MessageProcessor::ReceiveMessageAsync: 服务器主动关闭连接: NormalClosure, 
2025-12-19 18:42:01 WebSocketService::CloseWebSocketAsync: WebSocket已发送正常关闭帧
2025-12-19 18:42:01 [ERROR] WebSocketService::HandleConnectionClosed: 服务器主动关闭连接 - WebSocket异常断开
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 已取消并释放旧的取消标记源
2025-12-19 18:42:01 WebSocketService::StateChange: 服务器主动关闭: WebSocket状态变化 Open -> Closed
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 取消标记源引用已重置为 null
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 开始关闭服务，是否通知: True，是否禁用自动重连: False
2025-12-19 18:42:01 WebSocketService::DisposeWebSocket: WebSocket实例已成功释放
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 已触发关闭事件通知
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 底层连接资源释放完成
2025-12-19 18:42:01 [ERROR] WebSocketService::CreateServiceAsync: 连接失败 - WebSocket异常断开: A task was canceled.
2025-12-19 18:42:01 WebSocketMainManage::OnWebSocketClosed: WebSocket连接已断开，上报设备状态为 offline
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 已取消并释放旧的取消标记源
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 关闭流程结束
2025-12-19 18:42:01 WebSocketMainManage::OnWebSocketError: WebSocket错误: Receive
2025-12-19 18:42:01 WebSocketService::StartReceiveLoop: 接收循环结束，_isReceive=False，当前连接状态: Closed
2025-12-19 18:42:01 WebSocketService::HandleConnectionClosed: 已发送钉钉连接关闭通知
2025-12-19 18:42:01 EquipmentStatusHelper::: ReportStatus 开始上报设备状态 
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 取消标记源引用已重置为 null
2025-12-19 18:42:01 WebSocketService::AttemptReconnect: 第 1 次重连尝试，1000毫秒后开始
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 开始关闭服务，是否通知: True，是否禁用自动重连: False
2025-12-19 18:42:01 [DEBUG] EquipmentStatusHelper::: ReportStatus 开始上报设备状态 
2025-12-19 18:42:01 EquipmentStatusHelper::: 序列化后的消息内容: {
2025-12-19 18:42:01   "data": {
2025-12-19 18:42:01     "equipment_image": null
2025-12-19 18:42:01   },
2025-12-19 18:42:01   "request_id": "b75522fe-d4d9-49b0-9a2b-9b12dfd73c62",
2025-12-19 18:42:01   "type": "equipment-reporting",
2025-12-19 18:42:01   "require_ack": false
2025-12-19 18:42:01 }
2025-12-19 18:42:01 WebSocketService::DisposeWebSocket: WebSocket实例已成功释放
2025-12-19 18:42:01 [DEBUG] EquipmentStatusHelper::: 序列化后的消息内容: {
2025-12-19 18:42:01   "data": {
2025-12-19 18:42:01     "equipment_image": null
2025-12-19 18:42:01   },
2025-12-19 18:42:01   "request_id": "b75522fe-d4d9-49b0-9a2b-9b12dfd73c62",
2025-12-19 18:42:01   "type": "equipment-reporting",
2025-12-19 18:42:01   "require_ack": false
2025-12-19 18:42:01 }
2025-12-19 18:42:01 EquipmentStatusHelper::: 开始发送设备状态消息到 WebSocket
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 已触发关闭事件通知
2025-12-19 18:42:01 [DEBUG] EquipmentStatusHelper::: 开始发送设备状态消息到 WebSocket
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 底层连接资源释放完成
2025-12-19 18:42:01 WebSocketMainManage::OnWebSocketClosed: 关闭通知事件已触发
2025-12-19 18:42:01 WebSocketMainManage::OnWebSocketClosed: WebSocket连接已断开，上报设备状态为 offline
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 关闭流程结束
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 已取消并释放旧的取消标记源
2025-12-19 18:42:01 WebSocketService::SendDataAsync: 连接断开，消息加入待发送队列
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 连接结果: 失败
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 取消标记源引用已重置为 null
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 连接启动流程结束，_isConnecting 标记已重置
2025-12-19 18:42:01 EquipmentStatusHelper::: ReportStatus 开始上报设备状态 
2025-12-19 18:42:01 WebSocketService::AttemptReconnect: 第 3 次重连失败
2025-12-19 18:42:01 WebSocketMainManage::SendMessageAsync: 消息发送失败
2025-12-19 18:42:01 WebSocketService::AttemptReconnect: 第 2 次重连尝试，2000毫秒后开始
2025-12-19 18:42:01 WebSocketService::DisposeWebSocket: WebSocket实例已成功释放
2025-12-19 18:42:01 WebSocketService::AttemptReconnect: 第 3 次重连尝试，5000毫秒后开始
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 底层连接资源释放完成
2025-12-19 18:42:01 [DEBUG] EquipmentStatusHelper::: ReportStatus 开始上报设备状态 
2025-12-19 18:42:01 EquipmentStatusHelper::: 序列化后的消息内容: {
2025-12-19 18:42:01   "data": {
2025-12-19 18:42:01     "equipment_image": null
2025-12-19 18:42:01   },
2025-12-19 18:42:01   "request_id": "d01fdd8b-b976-43ba-9837-2b80dcbc7663",
2025-12-19 18:42:01   "type": "equipment-reporting",
2025-12-19 18:42:01   "require_ack": false
2025-12-19 18:42:01 }
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 关闭流程结束
2025-12-19 18:42:01 [DEBUG] EquipmentStatusHelper::: 序列化后的消息内容: {
2025-12-19 18:42:01   "data": {
2025-12-19 18:42:01     "equipment_image": null
2025-12-19 18:42:01   },
2025-12-19 18:42:01   "request_id": "d01fdd8b-b976-43ba-9837-2b80dcbc7663",
2025-12-19 18:42:01   "type": "equipment-reporting",
2025-12-19 18:42:01   "require_ack": false
2025-12-19 18:42:01 }
2025-12-19 18:42:01 EquipmentStatusHelper::: 开始发送设备状态消息到 WebSocket
2025-12-19 18:42:01 [DEBUG] EquipmentStatusHelper::: 开始发送设备状态消息到 WebSocket
2025-12-19 18:42:01 WebSocketMainManage::OnWebSocketClosed: 关闭通知事件已触发
2025-12-19 18:42:01 WebSocketService::SendDataAsync: 连接断开，消息加入待发送队列
2025-12-19 18:42:01 WebSocketMainManage::SendMessageAsync: 消息发送失败
2025-12-19 18:42:01 WebSocketService::AttemptReconnect: 第 4 次重连尝试，10000毫秒后开始
2025-12-19 18:42:01 WebSocketService::AttemptReconnect: 执行第 2 次重连，目标地址: ws://dev-customer-servhub-api.betteryeah.com/v1/ws/client/message?workspace_id=a042945be289477b9af048014f0f7cdb&access_key=YTA0Mjk0NWJlMjg5NDc3YjlhZjA0ODAxNGYwZjdjZGIsMTAwNTgsMTc2NDA1MTU0MjMzMQ==&bty_user_id=10058&assistant_id=木瓜瓜木&channel=qianniu&shop_id=木瓜瓜木的小店&customer_agent_id=84fe447220aa4b0d907cc26b46cdfe1f&desktop_id=aad6a6ab5543484aaf48929cf95e3e2b&env=dev&equipment_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 启动WebSocket服务: ws://dev-customer-servhub-api.betteryeah.com/v1/ws/client/message?workspace_id=a042945be289477b9af048014f0f7cdb&access_key=YTA0Mjk0NWJlMjg5NDc3YjlhZjA0ODAxNGYwZjdjZGIsMTAwNTgsMTc2NDA1MTU0MjMzMQ==&bty_user_id=10058&assistant_id=木瓜瓜木&channel=qianniu&shop_id=木瓜瓜木的小店&customer_agent_id=84fe447220aa4b0d907cc26b46cdfe1f&desktop_id=aad6a6ab5543484aaf48929cf95e3e2b&env=dev&equipment_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 当前已有连接实例状态: Null
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 旧连接处理完成，准备创建新连接
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 已取消并释放旧的取消标记源
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 取消标记源引用已重置为 null
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 取消标记源已清理
2025-12-19 18:42:01 WebSocketService::CreateServiceAsync: 开始建立连接: ws://dev-customer-servhub-api.betteryeah.com/v1/ws/client/message?workspace_id=a042945be289477b9af048014f0f7cdb&access_key=YTA0Mjk0NWJlMjg5NDc3YjlhZjA0ODAxNGYwZjdjZGIsMTAwNTgsMTc2NDA1MTU0MjMzMQ==&bty_user_id=10058&assistant_id=木瓜瓜木&channel=qianniu&shop_id=木瓜瓜木的小店&customer_agent_id=84fe447220aa4b0d907cc26b46cdfe1f&desktop_id=aad6a6ab5543484aaf48929cf95e3e2b&env=dev&equipment_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:01 WebSocketService::AttemptReconnect: 执行第 1 次重连，目标地址: ws://dev-customer-servhub-api.betteryeah.com/v1/ws/client/message?workspace_id=a042945be289477b9af048014f0f7cdb&access_key=YTA0Mjk0NWJlMjg5NDc3YjlhZjA0ODAxNGYwZjdjZGIsMTAwNTgsMTc2NDA1MTU0MjMzMQ==&bty_user_id=10058&assistant_id=木瓜瓜木&channel=qianniu&shop_id=木瓜瓜木的小店&customer_agent_id=84fe447220aa4b0d907cc26b46cdfe1f&desktop_id=aad6a6ab5543484aaf48929cf95e3e2b&env=dev&equipment_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 已有连接操作进行中，忽略本次调用
2025-12-19 18:42:01 WebSocketService::AttemptReconnect: 第 1 次重连失败
2025-12-19 18:42:01 WebSocketService::AttemptReconnect: 第 5 次重连尝试，30000毫秒后开始
2025-12-19 18:42:01 WebSocketService::CreateServiceAsync: 连接成功: Open
2025-12-19 18:42:01 LogWindow::LoadConfigFile: 成功加载配置文件: C:\Users\admin\AppData\Local\Bantouyan\qianniu\RPAConfig.json
2025-12-19 18:42:01 WebSocketService::ProcessPendingMessages: 队列处理暂停，剩余消息: 1，已处理: 1
2025-12-19 18:42:01 WebSocketService::CloseWebSocketAsync: WebSocket已发送正常关闭帧
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 已取消并释放旧的取消标记源
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 取消标记源引用已重置为 null
2025-12-19 18:42:01 WebSocketService::DisposeWebSocket: WebSocket实例已成功释放
2025-12-19 18:42:01 [ERROR] WebSocketService::CreateServiceAsync: 连接失败 - WebSocket异常断开: The operation was canceled.
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 底层连接资源释放完成
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 开始关闭服务，是否通知: True，是否禁用自动重连: False
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 关闭流程结束
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 已触发关闭事件通知
2025-12-19 18:42:01 WebSocketMainManage::OnWebSocketClosed: WebSocket连接已断开，上报设备状态为 offline
2025-12-19 18:42:01 EquipmentStatusHelper::: ReportStatus 开始上报设备状态 
2025-12-19 18:42:01 [DEBUG] EquipmentStatusHelper::: ReportStatus 开始上报设备状态 
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 已取消并释放旧的取消标记源
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 连接结果: 失败
2025-12-19 18:42:01 EquipmentStatusHelper::: 序列化后的消息内容: {
2025-12-19 18:42:01   "data": {
2025-12-19 18:42:01     "equipment_image": null
2025-12-19 18:42:01   },
2025-12-19 18:42:01   "request_id": "f018b997-e93f-41cf-a129-96cddf464781",
2025-12-19 18:42:01   "type": "equipment-reporting",
2025-12-19 18:42:01   "require_ack": false
2025-12-19 18:42:01 }
2025-12-19 18:42:01 WebSocketService::StartServiceAsync: 连接启动流程结束，_isConnecting 标记已重置
2025-12-19 18:42:01 WebSocketService::CleanupCancellationToken: 取消标记源引用已重置为 null
2025-12-19 18:42:01 WebSocketService::AttemptReconnect: 第 2 次重连失败
2025-12-19 18:42:01 [DEBUG] EquipmentStatusHelper::: 序列化后的消息内容: {
2025-12-19 18:42:01   "data": {
2025-12-19 18:42:01     "equipment_image": null
2025-12-19 18:42:01   },
2025-12-19 18:42:01   "request_id": "f018b997-e93f-41cf-a129-96cddf464781",
2025-12-19 18:42:01   "type": "equipment-reporting",
2025-12-19 18:42:01   "require_ack": false
2025-12-19 18:42:01 }
2025-12-19 18:42:01 WebSocketService::DisposeWebSocket: WebSocket实例已成功释放
2025-12-19 18:42:01 EquipmentStatusHelper::: 开始发送设备状态消息到 WebSocket
2025-12-19 18:42:01 WebSocketService::AttemptReconnect: 当前处于关闭流程，跳过自动重连
2025-12-19 18:42:01 [DEBUG] EquipmentStatusHelper::: 开始发送设备状态消息到 WebSocket
2025-12-19 18:42:01 WebSocketMainManage::OnWebSocketClosed: 关闭通知事件已触发
2025-12-19 18:42:01 WebSocketService::SendDataAsync: 连接断开，消息加入待发送队列
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 底层连接资源释放完成
2025-12-19 18:42:01 RPAFunService::: CloseDuplicateMessageWarningWindow: 未找到'接待中心'窗口
2025-12-19 18:42:01 WebSocketMainManage::SendMessageAsync: 消息发送失败
2025-12-19 18:42:01 WebSocketService::CloseServiceWithEventAsync: 关闭流程结束
2025-12-19 18:42:01 [DEBUG] RPAFunService::: CloseDuplicateMessageWarningWindow: 未找到'接待中心'窗口
2025-12-19 18:42:02 MessageProcessor::ReceiveMessageAsync: 接收消息异常: Cannot access a disposed object.
2025-12-19 18:42:02 Object name: 'System.Net.WebSockets.ClientWebSocket'.
2025-12-19 18:42:02 WebSocketService::HandleReceiveException: WebSocket对象已释放: ObjectDisposedException - Cannot access a disposed object.
2025-12-19 18:42:02 Object name: 'System.Net.WebSockets.ClientWebSocket'.
2025-12-19 18:42:02 WebSocketMainManage::OnWebSocketError: WebSocket错误: Receive
2025-12-19 18:42:02 WebSocketService::StartReceiveLoop: 接收循环结束，_isReceive=False，当前连接状态: Closed
2025-12-19 18:42:02 WebSocketService::HandleReceiveException: 已发送钉钉异常通知
2025-12-19 18:42:02 WebSocketService::AttemptReconnect: 执行第 5 次重连，目标地址: ws://dev-customer-servhub-api.betteryeah.com/v1/ws/client/message?workspace_id=a042945be289477b9af048014f0f7cdb&access_key=YTA0Mjk0NWJlMjg5NDc3YjlhZjA0ODAxNGYwZjdjZGIsMTAwNTgsMTc2NDA1MTU0MjMzMQ==&bty_user_id=10058&assistant_id=木瓜瓜木&channel=qianniu&shop_id=木瓜瓜木的小店&customer_agent_id=84fe447220aa4b0d907cc26b46cdfe1f&desktop_id=aad6a6ab5543484aaf48929cf95e3e2b&env=dev&equipment_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:02 WebSocketService::StartServiceAsync: 启动WebSocket服务: ws://dev-customer-servhub-api.betteryeah.com/v1/ws/client/message?workspace_id=a042945be289477b9af048014f0f7cdb&access_key=YTA0Mjk0NWJlMjg5NDc3YjlhZjA0ODAxNGYwZjdjZGIsMTAwNTgsMTc2NDA1MTU0MjMzMQ==&bty_user_id=10058&assistant_id=木瓜瓜木&channel=qianniu&shop_id=木瓜瓜木的小店&customer_agent_id=84fe447220aa4b0d907cc26b46cdfe1f&desktop_id=aad6a6ab5543484aaf48929cf95e3e2b&env=dev&equipment_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:02 WebSocketService::StartServiceAsync: 当前已有连接实例状态: Null
2025-12-19 18:42:02 WebSocketService::StartServiceAsync: 旧连接处理完成，准备创建新连接
2025-12-19 18:42:02 WebSocketService::CleanupCancellationToken: 已取消并释放旧的取消标记源
2025-12-19 18:42:02 WebSocketService::CleanupCancellationToken: 取消标记源引用已重置为 null
2025-12-19 18:42:02 WebSocketService::StartServiceAsync: 取消标记源已清理
2025-12-19 18:42:02 WebSocketService::CreateServiceAsync: 开始建立连接: ws://dev-customer-servhub-api.betteryeah.com/v1/ws/client/message?workspace_id=a042945be289477b9af048014f0f7cdb&access_key=YTA0Mjk0NWJlMjg5NDc3YjlhZjA0ODAxNGYwZjdjZGIsMTAwNTgsMTc2NDA1MTU0MjMzMQ==&bty_user_id=10058&assistant_id=木瓜瓜木&channel=qianniu&shop_id=木瓜瓜木的小店&customer_agent_id=84fe447220aa4b0d907cc26b46cdfe1f&desktop_id=aad6a6ab5543484aaf48929cf95e3e2b&env=dev&equipment_id=576c9d67462d4d7b8be79431353c2f57
2025-12-19 18:42:02 WebSocketService::CreateServiceAsync: 连接成功: Open
2025-12-19 18:42:02 WebSocketService::StateChange: 连接建立: WebSocket状态变化 Unknown -> Open
2025-12-19 18:42:02 WebSocketMainManage::OnWebSocketOpened: WebSocket连接已建立，上报设备状态为 running
2025-12-19 18:42:02 EquipmentStatusHelper::: ReportStatus 开始上报设备状态 
2025-12-19 18:42:02 [DEBUG] EquipmentStatusHelper::: ReportStatus 开始上报设备状态 
2025-12-19 18:42:02 EquipmentStatusHelper::: 序列化后的消息内容: {
2025-12-19 18:42:02   "data": {
2025-12-19 18:42:02     "equipment_image": null
2025-12-19 18:42:02   },
2025-12-19 18:42:02   "request_id": "e1cbb816-d9b8-42c7-8ef2-618c813dd619",
2025-12-19 18:42:02   "type": "equipment-reporting",
2025-12-19 18:42:02   "require_ack": false
2025-12-19 18:42:02 }
2025-12-19 18:42:02 [DEBUG] EquipmentStatusHelper::: 序列化后的消息内容: {
2025-12-19 18:42:02   "data": {
2025-12-19 18:42:02     "equipment_image": null
2025-12-19 18:42:02   },
2025-12-19 18:42:02   "request_id": "e1cbb816-d9b8-42c7-8ef2-618c813dd619",
2025-12-19 18:42:02   "type": "equipment-reporting",
2025-12-19 18:42:02   "require_ack": false
2025-12-19 18:42:02 }


