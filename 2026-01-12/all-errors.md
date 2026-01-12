LogWithUserName,
LogWithUserNameConsole,
LogWithUserName(safeUserName, "ResolveCenterInServiceList", "检测到 NoClickablePointException，准备关闭并重新打开千牛");
LogWithUserName("userName", "CloseReceptionWindows", $"消息发送失败，输入框已有内容:{edit.Text}");
LogWithUserName(userName, "GetEditControlContent", $"消息发送失败，输入框已有内容:{edit.Text}");
LogWithUserName(userName, "GetEditControlContent", "未找到输入框控件");
LogWithUserName(userName, "GetEditControlContent", "输入框异常：{0}", ex.Message);
LogWithUserName(string userName, string functionName, string message, params object[] args)
LogWithUserName(userName, functionName, formattedMessage);
LogWithUserName(long executionTimeMs, string userName, string functionName, string message, params object[] args)
LogWithUserName(executionTimeMs, userName, functionName, formattedMessage);
LogWithUserNameConsole(string userName, string functionName, string message, params object[] args)
LogWithUserNameConsole(userName, functionName, formattedMessage);
LogWithUserNameConsole(long executionTimeMs, string userName, string functionName, string message, params object[] args)
LogWithUserNameConsole(executionTimeMs, userName, functionName, formattedMessage);
LogWithUserNameConsole(userName, "ClearUserStatistics", "已清除用户统计信息");
LogWithUserName(childText ?? "未知用户", "ResolveAlertList", " 警告弹窗用户名 childText:{0}", childText);
LogWithUserName(childText, "ResolveAlertList", " click:{0}", childText);
LogWithUserNameConsole(userName, "CloseCurrentWindows", "开始关闭当前会话窗口 ---- userName: " + userName);
LogWithUserName(userName, "CloseCurrentWindows", "失败 - 千牛主窗口未初始化");
LogWithUserName(userName, "CloseCurrentWindows", "失败 - 未找到关闭按钮");
LogWithUserName("关闭", "SetOffline", "-----设置离线状态失败---- ex:" + ex.Message);
LogWithUserName("关闭", "SetOnline", "-----设置在线状态失败---- ex:" + ex.Message);
LogWithUserName(userName, "SetGlobalUserState", "添加新用户: {0}, 当前数量: {1}", userName, GlobalHelper.InServiceUserDic.Count);
LogWithUserName(userName, "WaitForChatWindowToLoad", "当前显示用户名: '{0}', 期望用户名: '{1}', 匹配: {2}", currentUserName, userName, isMatched);
LogWithUserName(userName, "WaitForChatWindowToLoad", "用户名不匹配，继续重试，当前: '{0}', 期望: '{1}', 第{2}次尝试", currentUserName, userName, currentAttempt);
LogWithUserName(userName, "WaitForChatWindowToLoad", "读取标题元素属性时异常，第{0}次尝试: {1}", currentAttempt, titlePropertyEx.Message);
LogWithUserName(userName, "WaitForChatWindowToLoad", "搜索标题元素时异常，第{0}次尝试: {1}", currentAttempt, titleSearchEx.Message);
LogWithUserName(userName, "WaitForChatWindowToLoad", "编辑框元素未找到，聊天窗口可能未完全加载，第{0}次尝试", currentAttempt);
LogWithUserName(userName, "WaitForChatWindowToLoad", "搜索编辑框元素时异常，第{0}次尝试: {1}", currentAttempt, editSearchEx.Message);
LogWithUserName(expectedUserName, "WaitForChatWindowToLoad", "千牛消息聊天元素未找到，第{0}次尝试", currentAttempt);
LogWithUserName(userName, "WaitForChatWindowToLoad", "搜索聊天元素时异常，第{0}次尝试: {1}", currentAttempt, chatSearchEx.Message);
LogWithUserName(userName, "WaitForChatWindowToLoad", "搜索千牛工作台窗口时异常，第{0}次尝试: {1}", currentAttempt, candidatesSearchEx.Message);
LogWithUserName(userName, "WaitForChatWindowToLoad", "等待间隔时异常: {0}", sleepEx.Message);
LogWithUserName(userName, "WaitForChatWindowToLoad", "当前显示用户名: '{0}', 期望用户名: '{1}', 匹配:{2}", currentUserName, userName, isMatched);
LogWithUserName(userName, "WaitForChatWindowToLoad", "用户名匹配成功，返回 true");
LogWithUserName(userName, "CommandWaitForTitleElementToLoad", "千牛主窗口为 null，返回失败");
LogWithUserName(userName, "CommandWaitForTitleElementToLoad", $"开始匹配 - headerName: {headerName}");
LogWithUserName(userName, "CommandWaitForTitleElementToLoad", "步骤1：精确匹配检查");
LogWithUserName(userName, "CommandWaitForTitleElementToLoad", "精确匹配成功，headerName: {0} , userName: {1}", headerName, userName);
LogWithUserName(userName, "CommandWaitForTitleElementToLoad", $"步骤2：前缀匹配检查（前{_prefixMatchLength}个字符）");
LogWithUserName(userName, "CommandWaitForTitleElementToLoad",
LogWithUserName(userName, "CommandWaitForTitleElementToLoad", $"检查 nameList 前缀匹配，列表长度: {nameList.Count}");
LogWithUserName(userName, "CommandWaitForTitleElementToLoad", "步骤3：占用检查");
LogWithUserName(userName, "CommandWaitForTitleElementToLoad", $"所有常规匹配都失败 - headerName: {headerName}");
LogWithUserName(userName, "CommandWaitForTitleElementToLoad", $"标题元素未找到，第 {i + 1} 次尝试");
LogWithUserName(userName, "CommandWaitForTitleElementToLoad", "titleElement未加载或为空，重试第{0}次，等待{1}ms, 标题名称{2}", i + 1, delayMs, headerName);
LogWithUserName(userName, "CommandWaitForTitleElementToLoad", $"常规匹配失败，尝试历史消息匹配 - headerName: {headerName}");
LogWithUserName(userName, "CommandWaitForTitleElementToLoad", $"历史消息匹配成功 - headerName: {headerName}");
LogWithUserName(userName, "CommandWaitForTitleElementToLoad", $"历史消息匹配失败 - headerName: {headerName}");
LogWithUserName(userName, "CommandWaitForTitleElementToLoad", "经过{0}次重试后仍未能加载标题元素", maxRetries);
LogWithUserName(userName, "CommandWaitForTitleElementToLoad", $"最终结果 - headerName: {headerName}, isMatched: {isMatched}");
LogWithUserName(userName, "UpdateUserHeaderMapping",
LogWithUserName(userName, "IsHeaderNameOccupiedByOther",
LogWithUserName(userName, "RemoveUserHeaderMapping",
LogWithUserName(userName, "HistoryMatched", "开始历史消息对比，userName: {0}, headerName: {1}, historyListCount: {2}", userName, headerName, historyList?.Count ?? 0);
LogWithUserName(userName, "HistoryMatched", "历史消息列表为空，无法进行匹配验证");
LogWithUserName(userName, "HistoryMatched", "通过历史消息对比，确认用户匹配，原用户名: {0} 标题名称: {1}, historyCount:{2}", userName, headerName, count);
LogWithUserName(userName, "HistoryMatched", "历史消息对比失败，匹配数不足，原用户名: {0} 标题名称: {1}, 匹配数:{2}, 总数:{3}", userName, headerName, count, historyList.Count);
LogWithUserName(userName, "HistoryMatched", "无法解析消息列表，对比失败，userName: {0}, headerName: {1}", userName, headerName);
LogWithUserName(headerName, "SendUnreadMessageListRetry", "侧边栏用户名: {0}", sidebarUserName);
LogWithUserName(headerName, "SendUnreadMessageListRetry", "标题栏用户名: {0}", headerName);
LogWithUserName(headerName, "SendUnreadMessageListRetry", "调用结果: {0}, useMessageIndexes: {1}", result, useMessageIndexes);
LogWithUserName(headerName, "SendUnreadMessageListRetry", "重试第{0}次，等待{1}ms", i + 1, 500 * (i + 1));
LogWithUserName(headerName, "SendUnreadMessageListRetry", "重试4次后仍返回NoData，消息列表持续为空");
LogWithUserName(headerName, "SendUnreadMessageList", "GlobalHelper.InServiceUserDic 中没有找到用户，添加用户全局状态");
LogWithUserName(headerName, "SendUnreadMessageList", "初始化用户状态失败: {0}", ex.Message);
LogWithUserName(headerName, "SendUnreadMessageList", "未找到千牛工作台窗口");
LogWithUserName(headerName, "SendUnreadMessageList", "查找千牛工作台窗口失败: {0}", ex.Message);
LogWithUserName(headerName, "SendUnreadMessageList", "查找千牛消息聊天控件失败: {0}", ex.Message);
LogWithUserName(headerName, "SendUnreadMessageList", "ParseMessages开始执行 - 时间: {0}, useMessageIndexes: {1}", DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss.fff"), useMessageIndexes);
LogWithUserName(headerName, "SendUnreadMessageList", "查找千牛消息聊天控件失败-isNotSupport--开始元素重绘");
LogWithUserName(headerName, "SendUnreadMessageList", "元素重绘成功--未找到千牛工作台窗口");
LogWithUserName(headerName ?? "未知用户", "SendUnreadMessageList：", "元素重绘成功--开始重新获取数据");
LogWithUserName(headerName ?? "未知用户", "SendUnreadMessageList：", "元素重绘成功--开始重新获取数据失败--isNotSupport");
LogWithUserName(headerName ?? "未知用户", "SendUnreadMessageList：", "元素重绘失败");
LogWithUserName(headerName, "SendUnreadMessageList", "ParseMessages解析消息失败: {0}", ex.Message);
LogWithUserName(headerName, "SendUnreadMessageList", "消息列表为空，聊天窗口可能还在加载中");
LogWithUserName(headerName, "SendUnreadMessageList",
LogWithUserName(headerName, "SendUnreadMessageList", "遍历抓取到的用户名称，找到匹配的名称: {0}", obj);
LogWithUserName(headerName, "SendUnreadMessageList", "遍历抓取到的用户名称，没有找到匹配的名称,在缓存中有该对象，但用户列表为空: {0}", obj);
LogWithUserName(headerName, "SendUnreadMessageList", "遍历抓取到的用户名称，没有找到匹配的名称,需要重新抓取数据: {0}，打印用户列表{1}", obj, name);
LogWithUserName(headerName, "SendUnreadMessageList", "遍历抓取到的用户名称，没有找到匹配的名称,需要重新抓取数据: {0}", obj);
LogWithUserName(headerName, "SendUnreadMessageList", "遍历抓取的用户信息异常: {0}", ex.Message);
LogWithUserName(headerName, "SendUnreadMessageList", "【回复判断】检测到欢迎语，跳过: {0}",
LogWithUserName(headerName, "SendUnreadMessageList", "【回复判断】检测到过滤话术，跳过: {0}",
LogWithUserName(headerName, "SendUnreadMessageList", "【回复判断】检测到真实客服回复: {0}",
LogWithUserName(headerName, "SendUnreadMessageList", "【回复判断】用户未被真实回复，标记为未回复状态 (HasReplied = false)");
LogWithUserName(headerName, "SendUnreadMessageList", "【回复判断】用户已被真实回复，标记为已回复状态 (HasReplied = true)");
LogWithUserName(headerName, "SendUnreadMessageList", "【UserNameList】添加用户消息的MessageUserName到UserNameList: '{0}', Role: {1}",
LogWithUserName(headerName, "SendUnreadMessageList", "【UserNameList】添加当前会话用户名到UserNameList: '{0}'", headerName);
LogWithUserName(headerName, "SendUnreadMessageList", "【UserNameList】当前UserNameList总数: {0}, 列表: [{1}]",
LogWithUserNameConsole(headerName, "SendUnreadMessageList", "【欢迎词】已发送欢迎词");
LogWithUserName(headerName, "SendUnreadMessageList", "消息处理完成，待发送消息数量: {0}", collectionResult.MessagesToSend?.Count);
LogWithUserName(headerName, "SendUnreadMessageList", "消息分类和处理失败: {0}", ex.Message);
LogWithUserName(headerName, "SendUnreadMessageList", "【过滤消息汇总】本次共有 {0} 条消息被过滤，详细如下：", collectionResult.FilteredMessages.Count);
LogWithUserName(headerName, "SendUnreadMessageList", filteredEntry);
LogWithUserName(headerName, "SendUnreadMessageList", "超过30分钟，关闭该用户");
LogWithUserName(headerName, "SendUnreadMessageList", "没有找到关闭按钮");
LogWithUserName(headerName, "SendUnreadMessageList", "更新回答时间戳失败: {0}", ex.Message);
LogWithUserName(headerName, "SendUnreadMessageList", "SendUnreadMessageList方法执行失败: {0}", ex.Message);
LogWithUserName(userName, "SendUnreadMessageToWebSocket", "【上报数据准备】准备发送消息到WebSocket");
LogWithUserName(userName, "SendUnreadMessageToWebSocket", "【上报数据准备】会话用户: {0}, 昵称: {1}, EventID: {2}", userName, nickName, eventId);
LogWithUserName(userName, "SendUnreadMessageToWebSocket", "【上报数据准备】消息数量: {0}, 分包信息: {1}/{2}", list?.Count, currentPackage, packageCount);
LogWithUserName(userName, "SendUnreadMessageToWebSocket", "【上报数据准备】历史消息数量: {0}", historyList?.Count ?? 0);
LogWithUserName(userName, "SendUnreadMessageToWebSocket", "【主消息列表】开始打印 {0} 条消息详情:", list.Count);
LogWithUserName(userName, "SendUnreadMessageToWebSocket", "【主消息{0}】UserName: '{1}', Role: {2}, Type: {3}, Timestamp: {4} ({5}), 内容: {6}",
LogWithUserName(userName, "SendUnreadMessageToWebSocket", "【历史消息列表】开始打印 {0} 条历史消息详情:", historyList.Count);
LogWithUserName(userName, "SendUnreadMessageToWebSocket", "【历史消息{0}】UserName: '{1}', Role: {2}, Type: {3}, Timestamp: {4} ({5}), 内容: {6}",
LogWithUserName(userName, "SendUnreadMessageToWebSocket", "【历史消息列表】为空，本次上报不包含历史消息");
LogWithUserName(userName, "SendUnreadMessageToWebSocket", "【上报数据摘要】即将发送的数据包含:");
LogWithUserName(userName, "SendUnreadMessageToWebSocket", "  - Type: {0}", model.Type);
LogWithUserName(userName, "SendUnreadMessageToWebSocket", "  - RequestID: {0}", model.RequestID);
LogWithUserName(userName, "SendUnreadMessageToWebSocket", "  - ConversationId: {0}", unreadMessageParamsRequestModel.ConversationId);
LogWithUserName(userName, "SendUnreadMessageToWebSocket", "  - EventID: {0}", unreadMessageParamsRequestModel.EventID);
LogWithUserName(userName, "SendUnreadMessageToWebSocket", "  - Package: {0}/{1}", currentPackage, packageCount);
LogWithUserName(userName, "SendUnreadMessageToWebSocket", "  - 主消息列表(msg_list): {0}条", list?.Count ?? 0);
LogWithUserName(userName, "SendUnreadMessageToWebSocket", "  - 历史消息列表(last_messages): {0}条", historyList?.Count ?? 0);
LogWithUserName(userName, "SendUnreadMessageToWebSocket", "  - JSON长度: {0} 字符", content?.Length ?? 0);
LogWithUserName(userName, "SendUnreadMessageToWebSocket", "【上报数据发送】开始发送到WebSocket");
LogWithUserName(userName, "SendUnreadMessageToWebSocket", "异常: {0}", ex.Message);
LogWithUserName(userName ?? "未知用户", "SendUnreadMessageList", "记录过滤消息详情失败: {0}", ex.Message);
LogWithUserName(name, "GetUnreadMessageModel", "========== 【客服名称转换开始】 ==========");
LogWithUserName(name, "GetUnreadMessageModel", "【客服名称转换】将Message转换为UnreadMessageModel");
LogWithUserName(name, "GetUnreadMessageModel", "【客服名称转换】message.MessageUserName: '{0}'", message.MessageUserName);
LogWithUserName(name, "GetUnreadMessageModel", "【客服名称转换】unreadMessageModel.UserName: '{0}'", unreadMessageModel.UserName);
LogWithUserName(name, "GetUnreadMessageModel", "【客服名称转换】传入的name参数: '{0}'", name);
LogWithUserName(name, "GetUnreadMessageModel", "【客服名称转换】Role: {0}", message.Role);
LogWithUserName(name, "GetUnreadMessageModel", "【客服名称转换】Timestamp: {0} ({1})", message.Timestamp, messageTime.ToString("yyyy-MM-dd HH:mm:ss"));
LogWithUserName(name, "GetUnreadMessageModel", "【客服名称转换】ContentType: {0}", message.ContentType);
LogWithUserName(name, "GetUnreadMessageModel", "【客服名称转换】isNewUser: {0}", isNewUser);
LogWithUserName(name, "GetUnreadMessageModel", "========== 【客服名称转换完成】 ==========");
LogWithUserName(name, "GetHistoryMessageModel", "【历史消息MessageUserName转换】将Message转换为UnreadMessageModel");
LogWithUserName(name, "GetHistoryMessageModel", "【历史消息MessageUserName转换】message.MessageUserName: '{0}' → unreadMessageModel.UserName: '{1}'",
LogWithUserName(name, "GetHistoryMessageModel", "【历史消息MessageUserName转换】Role: {0}, Timestamp: {1} ({2}), ContentType: {3}, isNewUser: {4}",
LogWithUserName(name, "ClickUser", $"开始点击用户 - name: {name}, nickName: {nickName}, isTraversing: {isTraversing}");
LogWithUserName(name, "ClickUser", "千牛主窗口未初始化，返回 Fail");
LogWithUserName(name, "ClickUser", "nameList is null");
LogWithUserName(name, "ClickUser", "nameList: {0}", sb.ToString());
LogWithUserName(name, "ClickUser", $"第 {retry + 1}/{maxRetries} 次尝试");
LogWithUserName(name, "ClickUser", $"获取对话列表成功，子元素数量: {currentCount}");
LogWithUserName(name, "ClickUser", "GetChild 查找成功，准备点击用户元素");
LogWithUserName(name, "ClickUser", "GetChild 查找失败，未找到用户元素");
LogWithUserName(name ?? "未知用户", "click-处理用户异常：", "元素重绘失败");
LogWithUserName(name, "ClickUser", "等待聊天窗口加载超时，用户: {0}", name);
LogWithUserName(name, "ClickUser", "在对话列表中未找到用户: {0}", name);
LogWithUserName(name, "ClickUser", "无法获取对话列表树控件");
LogWithUserName(name, "ClickUser", "第{0}次尝试失败，用户不在正在接待列表中", retry + 1);
LogWithUserName(name, "TryClickUserWithSortType", "尝试切换\"{0}\"", sortType);
LogWithUserName(name, "TryClickUserWithSortType", "在\"{0}\"模式下找到用户", sortType);
LogWithUserName(name, "TryClickUserWithSortType", "在\"{0}\"模式下未找到用户", sortType);
LogWithUserName(name, "TryClickUserWithSortType", "切换\"{0}\"失败", sortType);
LogWithUserNameConsole(name, "ClickUserRetry", "开始查找用户");
LogWithUserNameConsole(name, "ClickUserRetry", "首次尝试即找到用户");
LogWithUserNameConsole(name, "ClickUserRetry", "首次尝试失败（Fail）");
LogWithUserNameConsole(name, "ClickUserRetry", "首次未找到用户，尝试滚动列表到底部后重试");
LogWithUserNameConsole(name, "ClickUserRetry", "滚动后重试成功找到用户");
LogWithUserNameConsole(name, "ClickUserRetry", "所有重试方式均未找到用户，结果: {0}", retryResult);
LogWithUserNameConsole(name, "ClickUserRetry", "重试查找用户时发生异常: {0}", ex.Message);
LogWithUserName(targetUserName, "FindUserInTree", $"开始查找用户: {targetUserName}");
LogWithUserName(targetUserName, "FindUserInTree", "参数无效，tree 或 targetUserName 为空");
LogWithUserName(targetUserName, "FindUserInTree", "开始精确匹配");
LogWithUserName(targetUserName, "FindUserInTree", $"精确匹配成功，IsOffscreen: {exactMatch.IsOffscreen}");
LogWithUserName(targetUserName, "FindUserInTree", "找到用户元素但处于 offscreen 状态，跳过");
LogWithUserName(targetUserName, "FindUserInTree", "精确匹配成功并返回元素");
LogWithUserName(targetUserName, "FindUserInTree", "精确匹配失败，开始遍历子元素进行省略号匹配");
LogWithUserName(targetUserName, "FindUserInTree", $"找到 {allChildren.Length} 个子元素，开始遍历匹配");
LogWithUserName(targetUserName, "FindUserInTree", $"省略号匹配成功，childName: {childName}, IsOffscreen: {child.IsOffscreen}");
LogWithUserName(targetUserName, "FindUserInTree", $"找到用户元素但处于 offscreen 状态，跳过 - childName: {childName}");
LogWithUserName(targetUserName, "FindUserInTree", $"省略号匹配成功并返回元素 - childName: {childName}");
LogWithUserName(targetUserName, "FindUserInTree", $"遍历完所有 {allChildren.Length} 个子元素，未找到匹配的用户");
LogWithUserName(targetUserName, "FindUserInTree", "tree.FindAllChildren() 返回 null");
LogWithUserName(targetUserName, "FindUserInTree", "查找失败，返回 null");
LogWithUserName(name, "GetChild", $"开始查找用户 - name: {name}, nickName: {nickName}, nameList count: {nameList?.Count ?? 0}");
LogWithUserName(name, "GetChild", "tree 参数为 null，返回 null");
LogWithUserName(name, "GetChild", $"尝试使用主要用户名查找: {name}");
LogWithUserName(name, "GetChild", $"使用主要用户名查找成功: {name}");
LogWithUserName(name, "GetChild", $"使用主要用户名查找失败: {name}");
LogWithUserName(name, "GetChild", "主要用户名为空，跳过");
LogWithUserName(name, "GetChild", $"尝试使用昵称查找: {nickName}");
LogWithUserName(name, "GetChild", $"使用昵称查找成功: {nickName}");
LogWithUserName(name, "GetChild", $"使用昵称查找失败: {nickName}");
LogWithUserName(name, "GetChild", "昵称为空，跳过");
LogWithUserName(name, "GetChild", $"尝试使用名称列表查找，列表长度: {nameList.Count}");
LogWithUserName(name, "GetChild", $"尝试使用名称列表项查找: {userName} (第 {index}/{nameList.Count} 项)");
LogWithUserName(name, "GetChild", $"使用名称列表项查找成功: {userName} (第 {index}/{nameList.Count} 项)");
LogWithUserName(name, "GetChild", $"使用名称列表项查找失败: {userName} (第 {index}/{nameList.Count} 项)");
LogWithUserName(name, "GetChild", $"遍历完所有 {nameList.Count} 个名称列表项，均未找到匹配用户");
LogWithUserName(name, "GetChild", "名称列表为空或为 null，跳过");
LogWithUserName(name, "GetChild", $"所有查找方式均失败，返回 null - name: {name}, nickName: {nickName}");
LogWithUserNameConsole(userName, "ReplyMessageList", "ReplyMessageList 回复用户---- userName: " + userName);
LogWithUserName("未知用户", "ReplyMessageList", "下发的回复指令，userName为空");
LogWithUserName(headerName, "ReplyMessageList", "准备发送，消息数: {0}", model.Data?.MsgList?.Count ?? 0);
LogWithUserName(headerName, "ReplyMessageList", "发送图片，序号: {0}/{1}", i + 1, model.Data?.MsgList?.Count);
LogWithUserName(headerName, "ReplyMessageList", "发送文本，序号: {0}/{1}, 内容: {2}", i + 1, model.Data?.MsgList?.Count, model.Data?.MsgList[i].Content);
LogWithUserName(headerName, "ReplyMessageList", "发送失败，序号: {0}/{1}", i + 1, model.Data?.MsgList?.Count);
LogWithUserName(headerName, "ReplyMessageList", "发送成功，序号: {0}/{1}", i + 1, model.Data?.MsgList?.Count);
LogWithUserName(headerName, "ReplyMessageList", "完成，总数: {0}, 成功: {1}, 失败: {2}",
LogWithUserName(headerName, "ReplyMessageList",
LogWithUserName(headerName, "ReplyMessageList", "标记用户已有有效回复");
LogWithUserName(headerName, "ReplyMessageList", "开始验证，验证消息数: {0}", successMessages.Count);
LogWithUserName(headerName, "ReplyMessageList", "第 {0} 次验证，等待: {1}ms", verifyAttempt + 1, waitTimes[verifyAttempt]);
LogWithUserName(headerName, "ReplyMessageList", "第 {0} 次验证成功", verifyAttempt + 1);
LogWithUserName(headerName, "ReplyMessageList", "第 {0} 次验证失败，失败消息数: {1}", verifyAttempt + 1, verifyFailedMessages?.Count ?? 0);
LogWithUserName(headerName, "ReplyMessageList", "三次验证都失败，重新发送失败消息，失败数: {0}", verifyFailedMessages.Count);
LogWithUserName(headerName, "ReplyMessageList", "重新发送失败消息，序号: {0}/{1}, 内容: {2}", i + 1, verifyFailedMessages.Count, msg.Content);
LogWithUserName(headerName, "ReplyMessageList", "重新发送失败，序号: {0}/{1}", i + 1, verifyFailedMessages.Count);
LogWithUserName(headerName, "ReplyMessageList", "重新发送后开始三次验证");
LogWithUserName(headerName, "ReplyMessageList", "重新发送后第 {0} 次验证，等待: {1}ms", resendVerifyAttempt + 1, waitTimes[resendVerifyAttempt]);
LogWithUserName(headerName, "ReplyMessageList", "重新发送后第 {0} 次验证成功", resendVerifyAttempt + 1);
LogWithUserName(headerName, "ReplyMessageList", "重新发送后第 {0} 次验证失败，失败消息数: {1}", resendVerifyAttempt + 1, finalFailedMessages?.Count ?? 0);
LogWithUserName(headerName, "ReplyMessageList", "Fatal - 最终验证失败，失败数: {0}, 详情: {1}", finalFailedMessages?.Count ?? 0, failedMessagesDetail);
LogWithUserName(headerName, "ReplyMessageList", "消息验证最终失败，准备转人工");
LogWithUserName(headerName, "ReplyMessageList", "重新发送后验证成功");
LogWithUserName(headerName, "ReplyMessageList", "验证消息时发生异常: {0}", verifyEx.Message);
LogWithUserName(headerName, "ReplyMessageList", "消息发送失败，已达最大重试次数");
LogWithUserName(model?.Data?.UserName ?? "未知用户", "ReplyMessageList", $"-----回复消息失败----ex: {ex.Message}");
LogWithUserName(userName, "VerifySentMessages", "没有需要验证的消息");
LogWithUserName(userName, "VerifySentMessages", "获取千牛中心窗口失败，无法验证消息");
LogWithUserName(userName, "VerifySentMessages", "未找到千牛工作台窗口，无法验证消息");
LogWithUserName(userName, "VerifySentMessages", "查找千牛消息聊天控件失败: {0}", ex.Message);
LogWithUserName(userName, "VerifySentMessages", "解析消息列表失败: {0}", ex.Message);
LogWithUserName(userName, "VerifySentMessages", "消息列表为空，无法验证消息");
LogWithUserName(userName, "VerifySentMessages", "未找到任何客服消息");
LogWithUserName(userName, "VerifySentMessages", "========== 开始验证消息 ==========");
LogWithUserName(userName, "VerifySentMessages", "用户: {0}", userName);
LogWithUserName(userName, "VerifySentMessages", "发送消息数: {0}, 客服消息总数: {1}", sentMessages.Count, customerServiceMessages.Count);
LogWithUserName(userName, "VerifySentMessages", "待验证消息 [{0}] 类型: {1}, 内容: {2}",
LogWithUserName(userName, "VerifySentMessages", "客服消息 [{0}] 完整内容: {1}", textMessageCount, msg.Content);
LogWithUserName(userName, "VerifySentMessages", "[{0}/{1}] 跳过非文本消息验证 - 类型: {2}",
LogWithUserName(userName, "VerifySentMessages", "[{0}/{1}] 跳过包含http链接的消息验证 - 内容: {2}",
LogWithUserName(userName, "VerifySentMessages", "[{0}/{1}] 精确匹配失败，尝试模糊匹配", i + 1, sentMessages.Count);
LogWithUserName(userName, "VerifySentMessages", "[{0}/{1}] ✓ 模糊匹配通过 (中文字符顺序匹配)\n发送: {2}\n匹配: {3}",
LogWithUserName(userName, "VerifySentMessages", "消息未在界面中找到（精确和模糊匹配都失败）\n发送内容: {1}", i + 1, sentContent);
LogWithUserName(userName, "VerifySentMessages", "[{0}/{1}] ✓ 精确匹配通过: {2}",
LogWithUserName(userName, "VerifySentMessages", "========== 验证完成 ========== 总数: {0}, 已验证: {1}, 已跳过: {2}, 结果: 全部通过 ✓",
LogWithUserName(userName, "VerifySentMessages", "========== 验证完成 ========== 总数: {0}, 已验证: {1}, 已跳过: {2}, 失败: {3}",
LogWithUserName(userName, "VerifySentMessages", "未找到有效的聊天窗口，无法验证消息");
LogWithUserName(userName, "VerifySentMessages", "验证消息时发生异常: {0}", ex.Message);
LogWithUserName(userName, nameof(GetRecentCustomerServiceMessages),
LogWithUserName(userName, nameof(GetRecentCustomerServiceMessages), "千牛窗口为空");
LogWithUserName(userName, nameof(GetRecentCustomerServiceMessages), "未找到聊天窗口控件");
LogWithUserName(userName, nameof(GetRecentCustomerServiceMessages), "成功读取 {0} 条客服消息", recentMessages.Count);
LogWithUserName(userName, nameof(GetRecentCustomerServiceMessages), "读取消息时发生异常: {0}", ex.Message);
LogWithUserName(userName, "IsDuplicateMessage", "待发送消息为空，跳过检查");
LogWithUserName(userName, "IsDuplicateMessage", "没有找到历史客服消息，允许发送");
LogWithUserName(userName, "IsDuplicateMessage", "开始检查消息重复性，待发送消息: {0}, 阈值: {1}%, 检查最近 {2} 条消息",
LogWithUserName(userName, "IsDuplicateMessage", "第 {0} 条历史消息没有中文字符，跳过", i + 1);
LogWithUserName(userName, "IsDuplicateMessage", "第 {0} 条历史消息相似度: {1:F2}% (LCS:{2}/{3}), 内容: {4}",
LogWithUserName(userName, "IsDuplicateMessage", "检测到重复消息！相似度 {0:F2}% >= 阈值 {1}%，拒绝发送",
LogWithUserName(userName, "IsDuplicateMessage", "待发送: {0}", messageToSend);
LogWithUserName(userName, "IsDuplicateMessage", "历史消息: {0}", historyMessage.Content);
LogWithUserName(userName, "IsDuplicateMessage", "未检测到重复消息，允许发送");
LogWithUserName(userName, "IsDuplicateMessage", "检查消息重复性时发生异常: {0}，默认允许发送", ex.Message);
LogWithUserName(userName, "TransferToPersonAfterVerifyFailed", "消息验证失败，准备转人工 - 原因: {0}", reason);
LogWithUserName(userName, "TransferToPersonAfterVerifyFailed", "开始检查历史转接语并准备转人工");
LogWithUserName(userName, "TransferToPersonAfterVerifyFailed", "✓ 转人工成功");
LogWithUserName(userName, "TransferToPersonAfterVerifyFailed", "✗ 转人工失败");
LogWithUserName(userName, "TransferToPersonAfterVerifyFailed", "标记用户需要转人工 (NeedTransfer = true)");
LogWithUserName(userName, "TransferToPersonAfterVerifyFailed", "转人工时发生异常: {0}", ex.Message);
LogWithUserNameConsole(beforeTransferHeaderName, "AllCustomerTransferToOther", "转人工前尝试发送转接语");
LogWithUserName("操作执行结果事件", "SendRobotOperationResultModel", "发送数据...:{0}", content);
LogWithUserNameConsole(userName, "TransferToOther", "开始转人工 ---- userName: " + userName);
LogWithUserNameConsole("未知用户", "TransferToOther", "下发的转人工指令，userName为空");
LogWithUserName(userName ?? "未知用户", "TransferToOther", "-----转人工失败，参数验证失败----");
LogWithUserName(userName1 ?? "未知用户", "TransferToOther", $"-----转人工失败----ex:{ex.Message}");
LogWithUserName(headerName, "TransferToOther", "【转人工】成功 - 用户: {0}, 转交组: {1}", headerName, transferorPerson);
LogWithUserName(headerName ?? "未知用户", "TransferToOther", "-----首次转人工失败----");
LogWithUserNameConsole(userName ?? "未知用户", "TransferToHasPerson", "-----转人工失败，qianniu中心为null----");
LogWithUserNameConsole(userName ?? "未知用户", "TransferToHasPerson", "-----转给有人的转接组成功----{0}", name);
LogWithUserNameConsole(userName ?? "未知用户", "TransferToHasPerson", "-----转人工失败---- ex:" + ex.Message);
LogWithUserNameConsole(userName ?? "未知用户", "TransferToPerson-处理用户异常：", "元素重绘失败");
LogWithUserNameConsole(userName ?? "未知用户", "TransferToHasPerson", "转人工失败，当前没有正在接待的客服");
LogWithUserNameConsole(userName ?? "未知用户", "TransferToHasPerson", "转人工失败，tree控件为null");
LogWithUserNameConsole(userName ?? "未知用户", "转人工失败，tree控件为null", "元素重绘失败");
LogWithUserNameConsole(userName ?? "未知用户", "TransferToHasPerson", "转人工失败，window窗口为null");
LogWithUserNameConsole(userName ?? "未知用户", "TransferToHasPerson", "转人工失败，buttonControl 为null");
LogWithUserNameConsole(userName ?? "未知用户", "TransferToHasPerson", "-----转人工失败----");
LogWithUserNameConsole(userName ?? "未知用户", "TransferToHasPerson-处理用户异常：", "元素重绘失败");
LogWithUserNameConsole(userName, "TransferToHasPerson", "转发失败， 当前用户:{1}", userName);
LogWithUserNameConsole(userName ?? "未知用户", "TransferToPerson", "-----转人工失败，qianniu中心为null----");
LogWithUserName(userName ?? "未知用户", "TransferToPerson", "robot主动转人工，已关闭result事件上报");
LogWithUserNameConsole(userName ?? "未知用户", "TransferToPerson", emptyMessage);
LogWithUserName(userName ?? "未知用户", "TransferToPerson", "已关闭result事件上报，跳过上报: {0}", emptyMessage);
LogWithUserNameConsole(userName ?? "未知用户", "TransferToPerson", "读取到客服组信息: {0}", groupName);
LogWithUserNameConsole(userName ?? "未知用户", "TransferToPerson", errorMessage);
LogWithUserName(userName ?? "未知用户", "TransferToPerson", "已关闭result事件上报，跳过上报: {0}", errorMessage);
LogWithUserNameConsole(userName ?? "未知用户", "TransferToPerson", "读取客服组Name时出错: {0}", ex.Message);
LogWithUserNameConsole(userName ?? "未知用户", "TransferToPerson", "-----转人工成功----");
LogWithUserNameConsole(userName ?? "未知用户", "TransferToPerson", "转人工失败，当前没有正在接待的客服");
LogWithUserNameConsole(userName ?? "未知用户", "TransferToPerson", "转人工失败，tree控件为null");
LogWithUserNameConsole(userName ?? "未知用户", "TransferToPerson", "转人工失败，edit控件为null");
LogWithUserNameConsole(userName ?? "未知用户", "TransferToPerson", "转人工失败，window窗口为null");
LogWithUserNameConsole(userName ?? "未知用户", "TransferToPerson", "转人工失败，buttonControl 为null");
LogWithUserNameConsole(userName ?? "未知用户", "TransferToPerson", "-----转人工失败----");
LogWithUserNameConsole(userName ?? "未知用户", "TransferToPerson", "-----转人工失败---- ex:" + ex.Message + targetTransferor);
LogWithUserNameConsole(userName, "TransferToPerson", "转发失败，目标: {0}, 当前用户:{1}", targetTransferor, userName);
LogWithUserNameConsole(sidebarUserName, "CheckTopPositionAndTransferIfNeeded", "顶部次数 新用户首次出现，时间: {0}", currentTimestamp);
LogWithUserNameConsole(sidebarUserName, "CheckTopPositionAndTransferIfNeeded", "顶部次数 用户出现在顶部次数: {0}", userState.TopPositionCount);
LogWithUserNameConsole(sidebarUserName, "CheckTopPositionAndTransferIfNeeded", "顶部次数 用户最后一条消息时间戳: {0}", userState.LastUserMessageAt);
LogWithUserNameConsole(sidebarUserName, "CheckTopPositionAndTransferIfNeeded", "顶部次数 距离最后一条消息: {0}ms", timeSinceLastMessage);
LogWithUserNameConsole(sidebarUserName, "CheckTopPositionAndTransferIfNeeded", "顶部次数 用户未被回复: {0}", sidebarUserName);
LogWithUserNameConsole(sidebarUserName, "CheckTopPositionAndTransferIfNeeded", "顶部次数 用户已被回复: {0}", sidebarUserName);
LogWithUserNameConsole(sidebarUserName, "CheckTopPositionAndTransferIfNeeded",
LogWithUserNameConsole(sidebarUserName, "CheckTopPositionAndTransferIfNeeded", "转人工前窗口标题: {0}", beforeTransferHeaderName);
LogWithUserNameConsole(sidebarUserName, "CheckTopPositionAndTransferIfNeeded", "转人工前检查历史转接语并尝试发送");
LogWithUserNameConsole(sidebarUserName, "CheckTopPositionAndTransferIfNeeded", "顶部次数 用户因顶部出现次数超限自动转走成功");
LogWithUserNameConsole(sidebarUserName, "CheckTopPositionAndTransferIfNeeded", "顶部次数 用户因顶部出现次数超限自动转走失败");
LogWithUserNameConsole(sidebarUserName, "CheckTopPositionAndTransferIfNeeded", "顶部次数 检查并转走用户时发生异常: {0}", ex.Message);
LogWithUserNameConsole(userNameNickName, "ConversationCompletedSendMessage", "ConversationCompletedSendMessage 开始关闭会话 ---- userName: " + userNameNickName);
LogWithUserNameConsole("未知用户", "ConversationCompletedSendMessage", "下发的关闭指令，userName为空");
LogWithUserNameConsole(model?.Data?.UserName ?? "未知用户", "ConversationCompletedSendMessage", "-----关闭会话失败，找不到用户----");
LogWithUserNameConsole(userNameNickName, "ConversationCompletedSendMessage", "关闭会话 SendUnreadMessageList 发送未读消息 ---- userName: " + userNameNickName);
LogWithUserNameConsole(userNameNickName, "ConversationCompletedSendMessage", "关闭会话 SendUnreadMessageList 发送未读消息 ---- result: " + result);
LogWithUserNameConsole(model?.Data?.UserName ?? "未知用户", "ConversationCompletedSendMessage", "-----关闭会话成功----");
LogWithUserNameConsole(userName1 ?? "未知用户", "ConversationCompletedSendMessage", $"-----关闭会话失败----ex:{ex.Message}");
LogWithUserName(userName, "ParseMessages", "ParseMessages 开始解析消息");
LogWithUserName(userName, "ParseMessages", "【重试循环】第 {0} 次尝试：千牛中心为空", retry);
LogWithUserName(userName, "ParseMessages", "【返回】千牛中心窗口为空，返回 null - lastTS: {0}, isHistory: {1}, useMessageIndexes: {2}",
LogWithUserName(userName, "ParseMessages", "【返回】消息元素列表为空，返回 null - children: {0}, lastTS: {1}, isHistory: {2}, useMessageIndexes: {3}",
LogWithUserName(userName, "ParseMessages", "【返回】消息元素列表只有一个元素， children: {0}, lastTS: {1}, isHistory: {2}, useMessageIndexes: {3}",
LogWithUserName(userName, "ParseMessages", "【返回】消息元素列表只有一个元素， 内容: {0}, 类型: {1}",
LogWithUserName(userName, "ParseMessages", "【索引】元素数量减少（{0} -> {1}），重置索引为 -1", oldCount, children.Length);
LogWithUserName(userName, "ParseMessages", "【索引】使用已保存的索引，从 {0} 开始解析（LastMessageStartIndex，包含倒数第5条）", startIndex);
LogWithUserName(userName, "ParseMessages", "【索引】索引超出范围，重置为 -1，从 0 开始解析");
LogWithUserName(userName, "ParseMessages", "【索引】索引无效或未初始化，从 0 开始解析");
LogWithUserName(userName, "ParseMessages", "【索引】用户不在服务字典中，从 0 开始解析");
LogWithUserName(userName, "ParseMessages", "【索引】useMessageIndexes=false，不使用索引优化，从 0 开始解析");
LogWithUserName(userName, "ParseMessages", "【索引】isHistory=true，历史消息查询，从 0 开始解析");
LogWithUserName(userName, "ParseMessages", "[索引{0}] RuntimeId为空，跳过此元素", childIndex);
LogWithUserName(userName, "ParseMessages", "[索引{0}] 标题元素时间戳解析失败", childIndex);
LogWithUserName(userName, "ParseMessages", "[索引{0}] currentMsg为空，跳过图片消息处理", childIndex);
LogWithUserName(userName, "ParseMessages", "图片坐标连续两次无变化，跳出循环");
LogWithUserName(userName, "ParseMessages", "[索引{0}] currentMsg为空或StartIndex=-1，跳过菜单处理", childIndex);
LogWithUserName(userName, "ParseMessages", "[索引{0}] Text元素的parentId为空，跳过", childIndex);
LogWithUserName(userName, "ParseMessages", "[索引{0}] Text元素的parentId2为空，跳过", childIndex);
LogWithUserName(userName, "ParseMessages", "[索引{0}] Text元素包含换行符，添加为TEXT类型: {1}", childIndex, text?.Length > 30 ? text.Substring(0, 30) + "..." : text);
LogWithUserName(userName, "ParseMessages", "[索引{0}] Text元素包含'离线留言自动分配'，添加为TEXT类型", childIndex);
LogWithUserName(userName, "ParseMessages", "当前用户来自图片坐标连续两次无变化，跳出循环");
LogWithUserName(userName, "ParseMessages", "[索引{0}] Image元素-表情，添加文本: {1}", childIndex, text?.Length > 30 ? text.Substring(0, 30) + "..." : text);
LogWithUserName(userName, "ParseMessages", "[索引{0}] PropertyNotSupportedException 异常计数: {1}",
LogWithUserName(userName, "ParseMessages", "[索引{0}] 处理元素出错-PropertyNotSupportedException，总长度：{1}, 异常: {2}",
LogWithUserName(userName, "ParseMessages", "[索引{0}] 处理元素出错: {1}",
LogWithUserNameConsole(userName, "ParseMessages", "解析消息时发生严重异常: {0}", ex.Message);
LogWithUserNameConsole(userName, "ParseMessages", "异常堆栈跟踪: {0}", ex.StackTrace);
LogWithUserNameConsole(userName, "ParseMessages", "开始记录所有元素信息用于调试");
LogWithUserNameConsole(userName, "ParseMessages", "元素[{0}] - 类型: {1}, 文本: {2}, 控件类型: {3}",
LogWithUserNameConsole(userName, "ParseMessages", "记录元素信息时也发生异常: {0}", e.Message);
LogWithUserName(userName, "ParseMessages", "【返回】解析异常，返回 null - 异常信息: {0}, isNotSupported: {1}, lastTS: {2}, isHistory: {3}, useMessageIndexes: {4}",
LogWithUserName(userName, "ParseMessages", "【返回】解析完成 - 消息数量: {0}, isNotSupported: {1}, lastTS: {2}, isHistory: {3}, useMessageIndexes: {4}, children总数: {5}, startIndex: {6}",
LogWithUserName(userName, "ParseNameTimestamp", "【箭头处理】分割部分[{0}]: '{1}'", i, nameParts[i]);
LogWithUserName(userName, "ParseNameTimestamp", "【箭头处理】取第一部分作为最终名称: '{0}'", finalName);
LogWithUserName(userName, "ParseNameTimestamp", "【箭头处理】未检测到箭头符号，保持原名称");
LogWithUserName(userName, "ParseNameTimestamp", "【省略号处理】去掉省略号 '{0}' → '{1}'", beforeTrim, finalName);
LogWithUserName(userName, "ParseNameTimestamp", "【省略号处理】未检测到省略号");
LogWithUserName(userName, "ParseNameTimestamp", "【解析成功】最终结果 - 名称: '{0}', 时间戳: {1}, 角色: {2}",
LogWithUserName(userName, "ParseNameTimestamp", "【时间匹配失败】未找到时间格式，输入字符串: '{0}'", cleanInput);
LogWithUserName(userName, "ParseNameTimestamp", "【异常】解析过程中发生异常: {0}", ex.Message);
LogWithUserName(userName, "ParseNameTimestamp", "【异常】异常堆栈: {0}", ex.StackTrace);
LogWithUserName(userName, "ParseNameTimestamp", "【异常】输入字符串: '{0}'", input);
LogWithUserName(userName ?? "未知用户", "SendResultMessageRequestModel", "使用原始请求ID: {0}", model.RequestID);
LogWithUserName(userName ?? "未知用户", "SendResultMessageRequestModel", "警告：未找到原始请求ID，生成新ID: {0}", model1.RequestID);
LogWithUserName(userName ?? "未知用户", "SendResultMessageRequestModel", "发送数据...:{0}", content);
LogWithUserName(userName ?? "未知用户", "SendResultMessageRequestModel", "发送结果消息异常: {0}", ex.Message);
LogWithUserName(userName ?? "未知用户", "SendArtificiallyResultMessageRequestModel", "发送数据...:{0}", content);
LogWithUserName(userName, "SendUserNameCatchErrorMessageRequestModel", "发送用户异常数据...:{0}", content);
LogWithUserName("RPAFunService", "ResolveCenterInServiceList", "用户处理被暂停，已处理 {0}/{1} 个用户", processedUserCount, children.Length);
LogWithUserName(sidebarUserName, "ResolveCenterInServiceList", "处理用户-输入框控件转换为TextBox失败");
LogWithUserName(sidebarUserName, "ResolveCenterInServiceList", "处理用户-输入框已有内容，先清空:{0}", edit.Text);
LogWithUserName(sidebarUserName ?? "未知用户", "ResolveCenterInServiceList-处理用户异常：", userErrorMessage);
LogWithUserName(sidebarUserName ?? "未知用户", "ResolveCenterInServiceList-处理用户异常：", "元素重绘成功");
LogWithUserName("RPAFunService", "ResolveCenterInServiceList", "重绘后--接待中心没有正在接待的用户");
LogWithUserName(sidebarUserName ?? "未知用户", "ResolveCenterInServiceList-处理用户异常：", "元素重绘失败");
