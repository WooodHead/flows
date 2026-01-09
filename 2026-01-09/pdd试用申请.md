
 * ▗ ▗   ▖ ▖ *   Claude Code v2.0.76
*             *  Opus 4.5 · API Usage Billing
 *   ▘▘ ▝▝   *   ~/work/customer-servhub-api

  Welcome to Opus 4.5

> @routers/form_application/ 添加跟京东一样的拼多多试用申请相关接口 
  ⎿  Listed directory routers/form_application/

⏺ 我来帮你添加拼多多试用申请相关接口。首先让我了解一下京东试用申请的现有实现。

⏺ Explore(探索京东试用申请代码结构)
  ⎿  Done (0 tool uses · 0 tokens · 2m 57s)                                

⏺ 好的，让我直接查看代码结构。

⏺ Bash(find /Users/scott/work/customer-servhub-api/routers/form_application
      -type f -name "*.py" | head -20)
  ⎿ /Users/scott/work/customer-servhub-api/routers/form_application/request
    s/form_application_request.py
    /Users/scott/work/customer-servhub-api/routers/form_application/api/for
    m_application_router.py



⏺ Search(pattern: "**/form_application/**/*.py")
  ⎿  Found 3 files (ctrl+o to expand)

⏺ 让我读取这些文件来了解京东试用申请的实现：

⏺ Read(routers/form_application/api/form_application_router.py)
  ⎿  Read 131 lines

⏺ Read(routers/form_application/requests/form_application_request.py)
  ⎿  Read 29 lines

⏺ Read(services/form_application/form_application_service.py)
  ⎿  Read 629 lines

⏺ 我已经了解了京东试用申请的实现模式。现在我来添加拼多多试用申请相关接口，参照京东的实现方式。

⏺ 首先添加拼多多试用申请的请求模型：

⏺ Update(routers/form_application/requests/form_application_request.py)
  ⎿  Added 9 lines                                                       
      21      tech_support_link: Optional[str] = Field(default=None, desc
          ription="邀请技术支持链接")
      22  
      23  
      24 +class PddTrialApplyRequest(BaseModel):                         
      25 +    """拼多多试用申请请求"""                                   
      26 +    pdd_account: str = Field(..., description="拼多多客服账号")
      27 +    pdd_password: str = Field(..., description="拼多多客服密码"
         +)                                                              
      28 +    pre_sales_group: Optional[str] = Field(default=None, descri
         +ption="售前转接组")                                            
      29 +    after_sales_group: Optional[str] = Field(default=None, desc
         +ription="售后转发组")                                          
      30 +    tech_support_link: Optional[str] = Field(default=None, desc
         +ription="邀请技术支持链接")                                    
      31 +                                                               
      32 +                                                               
      33  class FormApplicationAuditRequest(BaseModel):
      34      apply_id: str = Field(..., description="申请ID")
      35      apply_status: str = Field(..., description="审核状态")

⏺ 现在添加拼多多相关的常量和校验函数到 service 文件：

⏺ Update(services/form_application/form_application_service.py)
  ⎿  Added 4 lines, removed 1 line                                       
      18  DINGTALK_CONFIG_KEY = "form_apply_webhook"
      19  JD_TRIAL_FORM_CODE = "jd_trial_apply"
      20  JD_TRIAL_FORM_NAME = "京东试用"
      21 +PDD_TRIAL_FORM_CODE = "pdd_trial_apply"                        
      22 +PDD_TRIAL_FORM_NAME = "拼多多试用"                             
      23  DEFAULT_APPLY_STATUS = FormApplicationStatus.UNDER_REVIEW.value
      22 -SENSITIVE_KEYS = {"password", "jd_password"}                   
      24 +SENSITIVE_KEYS = {"password", "jd_password", "pdd_password"}   
      25  FORM_WEBHOOK_KEY_MAP = {
      26      JD_TRIAL_FORM_CODE: "jd_trial_dingtalk_webhook",
      27 +    PDD_TRIAL_FORM_CODE: "pdd_trial_dingtalk_webhook",         
      28  }
      29  
      30  

⏺ 现在添加拼多多表单校验函数和更新 _resolve_form_name 函数：

⏺ Update(services/form_application/form_application_service.py)
  ⎿  Added 8 lines                                                       
      78          raise BusinessException(f"缺少必填字段: {', '.join(miss
          ing_keys)}")
      79  
      80  
      81 +def _validate_pdd_trial_form(form_data: Dict[str, Any]) -> None
         +:                                                              
      82 +    """校验拼多多试用申请表单必填项"""                         
      83 +    required_keys = ["pdd_account", "pdd_password"]            
      84 +    missing_keys = [key for key in required_keys if not form_da
         +ta.get(key)]                                                   
      85 +    if missing_keys:                                           
      86 +        raise BusinessException(f"缺少必填字段: {', '.join(miss
         +ing_keys)}")                                                   
      87 +                                                               
      88 +                                                               
      89  def _validate_apply_status(apply_status: str) -> None:
      90      """校验审批状态是否合法"""
      91      valid_statuses = {status.value for status in FormApplicatio
          nStatus}

⏺ 现在更新 _resolve_form_name 函数以支持拼多多：

⏺ Update(services/form_application/form_application_service.py)
  ⎿  Added 2 lines                                                       
       99          return form_name
      100      if form_code == JD_TRIAL_FORM_CODE:
      101          return JD_TRIAL_FORM_NAME
      102 +    if form_code == PDD_TRIAL_FORM_CODE:                      
      103 +        return PDD_TRIAL_FORM_NAME                            
      104      return None
      105  
      106  

⏺ 现在更新 submit_form_application 函数中的校验逻辑，添加拼多多表单校验：

⏺ Read(services/form_application/form_application_service.py)
  ⎿  Read 30 lines

⏺ 现在添加拼多多表单校验逻辑：

⏺ Update(services/form_application/form_application_service.py)
  ⎿  Added 3 lines                                                       
      300      if request.form_code == JD_TRIAL_FORM_CODE:
      301          # 京东试用申请必须包含账号和密码
      302          _validate_jd_trial_form(form_data)
      303 +    elif request.form_code == PDD_TRIAL_FORM_CODE:            
      304 +        # 拼多多试用申请必须包含账号和密码                    
      305 +        _validate_pdd_trial_form(form_data)                   
      306  
      307      form_name = _resolve_form_name(request.form_code, request.
           form_name)
      308      apply_id = uuid.uuid4().hex

⏺ 现在更新 todo 并添加拼多多查询方法。先查看文件末尾的京东查询方法：

⏺ 现在在 service 文件末尾添加拼多多查询方法。先查看文件末尾：

⏺ Read(services/form_application/form_application_service.py)
  ⎿  Read 76 lines

⏺ 现在在文件末尾添加拼多多相关的查询方法：

⏺ Update(services/form_application/form_application_service.py)
  ⎿  Added 90 lines                                                      
      642          page_size,
      643      )
      644      return payload
      645 +                                                              
      646 +                                                              
      647 +async def get_user_latest_pdd_trial_application(user_id: str) 
          +-> Optional[Dict[str, Any]]:                                  
      648 +    """                                                       
      649 +    获取指定用户最新的拼多多试用申请                          
      650 +                                                              
      651 +    Args:                                                     
      652 +        user_id: 用户ID                                       
      653 +                                                              
      654 +    Returns:                                                  
      655 +        最新的拼多多试用申请详情，不存在返回None              
      656 +    """                                                       
      657 +    if not user_id:                                           
      658 +        raise BusinessException("user_id 不能为空")           
      659 +                                                              
      660 +    logger.info("[表单申请] 获取用户最新拼多多试用申请: user_i
          +d=%s", user_id)                                               
      661 +                                                              
      662 +    form_application_dao = FormApplicationDao()               
      663 +    record = await form_application_dao.get_latest_user_applic
          +ation_by_form_code(user_id, PDD_TRIAL_FORM_CODE)              
      664 +                                                              
      665 +    if not record:                                            
      666 +        logger.info("[表单申请] 用户暂无拼多多试用申请记录: us
          +er_id=%s", user_id)                                           
      667 +        return None                                           
      668 +                                                              
      669 +    result = _build_application_payload(record)               
      670 +                                                              
      671 +    logger.info(                                              
      672 +        "[表单申请] 用户最新拼多多试用申请查询成功: user_id=%s
          +, apply_id=%s, apply_status=%s",                              
      673 +        user_id,                                              
      674 +        record.apply_id,                                      
      675 +        record.apply_status,                                  
      676 +    )                                                         
      677 +    return result                                             
      678 +                                                              
      679 +                                                              
      680 +async def get_current_user_pdd_trial_application() -> Optional
          +[Dict[str, Any]]:                                             
      681 +    """                                                       
      682 +    获取当前登录用户的拼多多试用申请（无需传参）              
      683 +                                                              
      684 +    Returns:                                                  
      685 +        当前用户的拼多多试用申请详情，不存在返回None          
      686 +    """                                                       
      687 +    current_user = user_info.get()                            
      688 +                                                              
      689 +    if not current_user or current_user.isAnonymous:          
      690 +        raise BusinessException("请先登录")                   
      691 +                                                              
      692 +    user_id = str(current_user.ucUserId)                      
      693 +    logger.info("[表单申请] 获取当前用户拼多多试用申请: user_i
          +d=%s", user_id)                                               
      694 +                                                              
      695 +    return await get_user_latest_pdd_trial_application(user_id
          +)                                                             
      696 +                                                              
      697 +                                                              
      698 +async def list_pdd_trial_applications_admin(page: int, page_si
          +ze: int) -> Dict[str, Any]:                                   
      699 +    """                                                       
      700 +    管理员分页获取拼多多试用申请列表                          
      701 +                                                              
      702 +    Args:                                                     
      703 +        page: 页码                                            
      704 +        page_size: 每页大小                                   
      705 +                                                              
      706 +    Returns:                                                  
      707 +        包含 items/total/page/page_size 的分页结果            
      708 +    """                                                       
      709 +    if page <= 0:                                             
      710 +        raise BusinessException("page 必须大于 0")            
      711 +    if page_size <= 0:                                        
      712 +        raise BusinessException("page_size 必须大于 0")       
      713 +                                                              
      714 +    logger.info("[表单申请] 管理员查询拼多多试用申请列表: page
          +=%s, page_size=%s", page, page_size)                          
      715 +                                                              
      716 +    form_application_dao = FormApplicationDao()               
      717 +    records, total = await form_application_dao.list_applicati
          +ons_by_form_code(PDD_TRIAL_FORM_CODE, page, page_size)        
      718 +                                                              
      719 +    items = [_build_application_payload(record) for record in 
          +records]                                                      
      720 +    payload = {                                               
      721 +        "items": items,                                       
      722 +        "total": total,                                       
      723 +        "page": page,                                         
      724 +        "page_size": page_size,                               
      725 +    }                                                         
      726 +                                                              
      727 +    logger.info(                                              
      728 +        "[表单申请] 管理员拼多多试用申请列表查询完成: total=%s
          +, returned=%s, page=%s, page_size=%s",                        
      729 +        total,                                                
      730 +        len(items),                                           
      731 +        page,                                                 
      732 +        page_size,                                            
      733 +    )                                                         
      734 +    return payload                                            

⏺ 现在更新 todo 并添加路由接口：

⏺ 现在添加拼多多试用申请的路由接口。先更新 import 部分：

⏺ Update(routers/form_application/api/form_application_router.py)
  ⎿  Added 5 lines                                                       
      10      FormApplicationAuditRequest,
      11      FormApplicationSubmitRequest,
      12      JdTrialApplyRequest,
      13 +    PddTrialApplyRequest,                                      
      14  )
      15  from services.form_application.form_application_service import 
          (
      16      JD_TRIAL_FORM_CODE,
      17      JD_TRIAL_FORM_NAME,
      18 +    PDD_TRIAL_FORM_CODE,                                       
      19 +    PDD_TRIAL_FORM_NAME,                                       
      20      audit_form_application,
      21      get_application_detail,
      22      get_current_user_jd_trial_application,
      23 +    get_current_user_pdd_trial_application,                    
      24      get_user_latest_jd_trial_application,
      25 +    get_user_latest_pdd_trial_application,                     
      26      submit_form_application,
      27  )
      28  

⏺ 现在在路由文件中添加拼多多试用申请的接口。先查看当前文件的完整内容：

⏺ Read(routers/form_application/api/form_application_router.py)
  ⎿  Read 136 lines

⏺ 现在在京东试用申请接口后面添加拼多多试用申请接口：

⏺ Update(routers/form_application/api/form_application_router.py)
  ⎿  Added 31 lines                                                      
       72      return success_response(data={"apply_id": apply_id})
       73  
       74  
       75 +@router.post("/form_application/pdd_trial", summary="拼多多试 
          +用申请提交")                                                  
       76 +@log_request_as_curl                                          
       77 +async def submit_pdd_trial_application_api(request: Request, p
          +arams: PddTrialApplyRequest):                                 
       78 +    """                                                       
       79 +    拼多多试用申请提交接口                                    
       80 +                                                              
       81 +    参数:                                                     
       82 +        pdd_account: 拼多多客服账号（必填）                   
       83 +        pdd_password: 拼多多客服密码（必填）                  
       84 +        pre_sales_group: 售前转接组（可选）                   
       85 +        after_sales_group: 售后转发组（可选）                 
       86 +        tech_support_link: 邀请技术支持链接（可选）           
       87 +                                                              
       88 +    返回:                                                     
       89 +        apply_id: 申请ID                                      
       90 +    """                                                       
       91 +    client_ip = _get_client_ip(request)                       
       92 +    logger.info("[表单申请] 收到拼多多试用申请请求: client_ip=
          +%s", client_ip)                                               
       93 +                                                              
       94 +    submit_request = FormApplicationSubmitRequest(            
       95 +        form_code=PDD_TRIAL_FORM_CODE,                        
       96 +        form_name=None,                                       
       97 +        applicant_name=None,                                  
       98 +        applicant_phone=None,                                 
       99 +        applicant_email=None,                                 
      100 +        form_data=params.model_dump(),                        
      101 +    )                                                         
      102 +    apply_id = await submit_form_application(request=submit_re
          +quest, client_ip=client_ip, type_name=PDD_TRIAL_FORM_NAME)    
      103 +    return success_response(data={"apply_id": apply_id})      
      104 +                                                              
      105 +                                                              
      106  @router.get("/form_application/detail/{apply_id}", summary="获
           取申请详情")
      107  async def get_application_detail_api(request: Request, apply_i
           d: str):
      108      """

⏺ 现在添加拼多多试用申请的查询接口。先读取当前文件末尾：

⏺ Read(routers/form_application/api/form_application_router.py)
  ⎿  Read 53 lines

⏺ 现在在京东试用申请查询接口后面添加拼多多试用申请查询接口：

⏺ Update(routers/form_application/api/form_application_router.py)
  ⎿  Added 29 lines                                                      
      148      return success_response(data=result)
      149  
      150  
      151 +@router.get("/form_application/pdd_trial/current", summary="获
          +取当前用户拼多多试用申请")                                    
      152 +async def get_current_user_pdd_trial_api(request: Request):   
      153 +    """                                                       
      154 +    获取当前登录用户的拼多多试用申请（无需传参）              
      155 +                                                              
      156 +    返回:                                                     
      157 +        当前用户的拼多多试用申请详情，不存在返回 None         
      158 +    """                                                       
      159 +    logger.info("[表单申请] 收到获取当前用户拼多多试用申请请求
          +")                                                            
      160 +    result = await get_current_user_pdd_trial_application()   
      161 +    return success_response(data=result)                      
      162 +                                                              
      163 +                                                              
      164 +@router.get("/form_application/user/{user_id}/pdd_trial/latest
          +", summary="获取用户最新拼多多试用申请")                      
      165 +async def get_user_latest_pdd_trial_api(request: Request, user
          +_id: str):                                                    
      166 +    """                                                       
      167 +    获取用户最新的拼多多试用申请                              
      168 +                                                              
      169 +    参数:                                                     
      170 +        user_id: 用户ID                                       
      171 +                                                              
      172 +    返回:                                                     
      173 +        最新的拼多多试用申请详情，不存在返回 None             
      174 +    """                                                       
      175 +    logger.info("[表单申请] 收到获取用户最新拼多多试用申请请求
          +: user_id=%s", user_id)                                       
      176 +    result = await get_user_latest_pdd_trial_application(user_
          +id)                                                           
      177 +    return success_response(data=result)                      
      178 +                                                              
      179 +                                                              
      180  @router.post("/operate_back/form_application/audit", summary="
           运营后台表单申请审核")
      181  @log_request_as_curl
      182  async def audit_form_application_api(request: Request, params:
            FormApplicationAuditRequest):

⏺ 路由接口已添加完成。现在更新 todo 并添加接口文档：

⏺ 现在添加接口文档。先查看 docs 目录下是否有现有的表单申请文档：

⏺ Search(pattern: "docs/**/*form*")
  ⎿  Found 1 file (ctrl+o to expand)

⏺ Search(pattern: "docs/**/*trial*")
  ⎿  Found 0 files 

⏺ 让我查看现有的表单申请文档：

⏺ Read(docs/form_application.md)
  ⎿  Read 391 lines

⏺ 现在我在文档中添加拼多多试用申请接口的说明。在京东试用申请接口后面添加拼多多试用申请接口文档：

⏺ Update(docs/form_application.md)
  ⎿  Added 103 lines, removed 1 line                                     
      141  
      142  ---
      143  
      144 -## 二、通用表单接口                                           
      144 +## 二、拼多多试用申请接口                                     
      145  
      146 +### 2.1 拼多多试用申请提交（POST）                            
      147 +```bash                                                       
      148 +# 方式1：使用拼多多试用专用接口                               
      149 +curl -X POST 'https://your-domain.com/{API_VERSION}/form_appli
          +cation/pdd_trial' \                                           
      150 +  -H 'Content-Type: application/json' \                       
      151 +  -d '{                                                       
      152 +    "pdd_account": "pdd_cs_account",                          
      153 +    "pdd_password": "secret",                                 
      154 +    "pre_sales_group": "售前转接组A",                         
      155 +    "after_sales_group": "售后转发组B",                       
      156 +    "tech_support_link": "https://ai.example.com/login?type=in
          +vite&link_id=xxx"                                             
      157 +  }'                                                          
      158 +                                                              
      159 +# 方式2：使用通用表单提交接口                                 
      160 +curl -X POST 'https://your-domain.com/{API_VERSION}/form_appli
          +cation/submit' \                                              
      161 +  -H 'Content-Type: application/json' \                       
      162 +  -H 'Authorization: Bearer YOUR_TOKEN' \                     
      163 +  -d '{                                                       
      164 +    "form_code": "pdd_trial_apply",                           
      165 +    "form_name": "拼多多试用申请",                            
      166 +    "applicant_type": "individual",                           
      167 +    "form_data": {                                            
      168 +      "pdd_account": "pdd_cs_account",                        
      169 +      "pdd_password": "secret",                               
      170 +      "pre_sales_group": "售前转接组A",                       
      171 +      "after_sales_group": "售后转发组B",                     
      172 +      "tech_support_link": "https://ai.example.com/login?type=
          +invite&link_id=xxx"                                           
      173 +    }                                                         
      174 +  }'                                                          
      175 +```                                                           
      176 +                                                              
      177 +**响应示例**：                                                
      178 +```json                                                       
      179 +{                                                             
      180 +  "code": 0,                                                  
      181 +  "message": "success",                                       
      182 +  "data": {                                                   
      183 +    "apply_id": "abc123def456"                                
      184 +  }                                                           
      185 +}                                                             
      186 +```                                                           
      187 +                                                              
      188 +### 2.2 获取拼多多试用申请详情（GET）                         
      189 +```bash                                                       
      190 +# 方式1：获取当前登录用户的拼多多试用申请（推荐，无需传参）   
      191 +curl -X GET 'https://your-domain.com/{API_VERSION}/form_applic
          +ation/pdd_trial/current' \                                    
      192 +  -H 'Authorization: Bearer YOUR_TOKEN'                       
      193 +                                                              
      194 +# 方式2：通过 user_id 获取用户最新的拼多多试用申请（专用接口）
      195 +curl -X GET 'https://your-domain.com/{API_VERSION}/form_applic
          +ation/user/user_12345/pdd_trial/latest'                       
      196 +                                                              
      197 +# 方式3：通过 apply_id 获取申请详情（通用接口）               
      198 +curl -X GET 'https://your-domain.com/{API_VERSION}/form_applic
          +ation/detail/abc123def456'                                    
      199 +```                                                           
      200 +                                                              
      201 +**响应示例**：                                                
      202 +```json                                                       
      203 +{                                                             
      204 +  "code": 0,                                                  
      205 +  "message": "success",                                       
      206 +  "data": {                                                   
      207 +    "id": 124,                                                
      208 +    "apply_id": "def456abc789",                               
      209 +    "form_code": "pdd_trial_apply",                           
      210 +    "form_name": "拼多多试用",                                
      211 +    "user_id": "user_12345",                                  
      212 +    "user_info": {                                            
      213 +      "user_id": "user_12345",                                
      214 +      "username": "张三",                                     
      215 +      "email": "zhangsan@example.com",                        
      216 +      "phone": "13800000000",                                 
      217 +      "enterprise_id": "ent_001"                              
      218 +    },                                                        
      219 +    "applicant_type": "individual",                           
      220 +    "apply_status": "Approved",                               
      221 +    "audit_by": "管理员A",                                    
      222 +    "audit_remark": "审核通过",                               
      223 +    "audit_at": "2025-01-01T11:00:00",                        
      224 +    "form_data": {                                            
      225 +      "pdd_account": "pdd_cs_account",                        
      226 +      "pdd_password": "******",                               
      227 +      "pre_sales_group": "售前转接组A",                       
      228 +      "after_sales_group": "售后转发组B",                     
      229 +      "tech_support_link": "https://ai.example.com/login?type=
          +invite&link_id=xxx"                                           
      230 +    },                                                        
      231 +    "created_at": "2025-01-01T10:00:00",                      
      232 +    "updated_at": "2025-01-01T11:00:00"                       
      233 +  }                                                           
      234 +}                                                             
      235 +```                                                           
      236 +                                                              
      237 +**字段说明**：                                                
      238 +- **pdd_account**（必填）：拼多多客服账号                     
      239 +- **pdd_password**（必填）：拼多多客服密码（查询时会自动脱敏为
          + `******`）                                                   
      240 +- **pre_sales_group**（可选）：售前转接组名称                 
      241 +- **after_sales_group**（可选）：售后转发组名称               
      242 +- **tech_support_link**（可选）：邀请技术支持的链接           
      243 +                                                              
      244 +---                                                           
      245 +                                                              
      246 +## 三、通用表单接口                                           
      247 +                                                              
      248  ### 2.1 通用表单提交（POST）
      249  
      250  #### 个人申请示例

⏺ 我需要修复文档中的章节编号问题（通用表单接口应该是第三章，子章节编号也需要更新）：

⏺ Update(docs/form_application.md)
  ⎿  Added 1 line, removed 1 line                                        
      245  
      246  ## 三、通用表单接口
      247  
      248 -### 2.1 通用表单提交（POST）                                  
      248 +### 3.1 通用表单提交（POST）                                  
      249  
      250  #### 个人申请示例
      251  ```bash

⏺ 现在继续修复文档中的其他章节编号。让我查看并修复：

⏺ Read(docs/form_application.md)
  ⎿  Read 194 lines

⏺ 我需要修复文档中的章节编号问题。让我逐步修复：

⏺ Update(docs/form_application.md)
  ⎿  Added 1 line, removed 1 line                                        
      305  - `user_id` 和 `user_info` 由后端根据 Authorization Token 自动
           补全，无需在请求中提交
      306  - 请求必须携带有效的 `Authorization` 头，格式为 `Bearer YOUR_T
           OKEN`
      307  
      308 -### 2.2 获取申请详情（通用接口）                              
      308 +### 3.2 获取申请详情（通用接口）                              
      309  ```bash
      310  curl -X GET 'https://your-domain.com/{API_VERSION}/form_applic
           ation/detail/{apply_id}'
      311  ```

⏺ 现在继续修复后续章节编号：

⏺ Update(docs/form_application.md)
  ⎿  Added 2 lines, removed 2 lines                                      
      353  
      354  ---
      355  
      356 -## 三、运营后台接口                                           
      356 +## 四、运营后台接口                                           
      357  
      358 -### 3.1 表单申请审核                                          
      358 +### 4.1 表单申请审核                                          
      359  ```bash
      360  curl -X POST 'https://your-domain.com/{API_VERSION}/operate_ba
           ck/form_application/audit' \
      361    -H 'Content-Type: application/json' \

⏺ 继续修复剩余的章节编号：

⏺ Update(docs/form_application.md)
  ⎿  Added 1 line, removed 1 line                                        
      367    }'
      368  ```
      369  
      370 -### 3.2 管理员获取京东试用申请列表                            
      370 +### 4.2 管理员获取京东试用申请列表                            
      371  ```bash
      372  curl -X GET 'https://your-domain.com/{API_VERSION}/admin/form_
           application/jd_trial/list?page=1&page_size=20' \
      373    -H 'Authorization: Bearer YOUR_TOKEN'

⏺ 继续修复剩余的章节编号：

⏺ Update(docs/form_application.md)
  ⎿  Added 2 lines, removed 2 lines                                      
      420  
      421  ---
      422  
      423 -## 四、配置说明                                               
      423 +## 五、配置说明                                               
      424  
      425 -### 4.1 申请状态枚举                                          
      425 +### 5.1 申请状态枚举                                          
      426  - `UnderReview`：审核中
      427  - `Approved`：审核通过
      428  - `Reject`：审核拒绝

⏺ 继续修复剩余的章节编号：

⏺ Update(docs/form_application.md)
  ⎿  Added 3 lines, removed 2 lines                                      
      427  - `Approved`：审核通过
      428  - `Reject`：审核拒绝
      429  
      430 -### 4.2 钉钉 Webhook 配置（system_config）                    
      430 +### 5.2 钉钉 Webhook 配置（system_config）                    
      431  ```json
      432  {
      433    "form_apply_webhook": {
      434 -    "jd_trial_dingtalk_webhook": "https://oapi.dingtalk.com/ro
          -bot/send?access_token=xxx"                                    
      434 +    "jd_trial_dingtalk_webhook": "https://oapi.dingtalk.com/ro
          +bot/send?access_token=xxx",                                   
      435 +    "pdd_trial_dingtalk_webhook": "https://oapi.dingtalk.com/r
          +obot/send?access_token=yyy"                                   
      436    }
      437  }
      438  ```

⏺ 继续修复最后的章节编号：

⏺ Update(docs/form_application.md)
  ⎿  Added 2 lines, removed 2 lines                                      
      439  
      440  ---
      441  
      442 -## 五、数据库迁移 SQL                                         
      442 +## 六、数据库迁移 SQL                                         
      443  
      444 -### 5.1 添加 user_id、user_info 和 applicant_type 字段        
      444 +### 6.1 添加 user_id、user_info 和 applicant_type 字段        
      445  ```sql
      446  -- 添加 user_id 字段
      447  ALTER TABLE form_application ADD COLUMN IF NOT EXISTS user_id 
           VARCHAR(100);

⏺ 继续修复剩余的章节编号：

⏺ Update(docs/form_application.md)
  ⎿  Added 1 line, removed 1 line                                        
      462  COMMENT ON COLUMN form_application.form_data IS '表单扩展字段(
           包含申请人信息和其他业务数据)';
      463  ```
      464  
      465 -### 5.2 迁移旧数据：将 applicant_name/phone/email 迁移到 form_
          -data                                                          
      465 +### 6.2 迁移旧数据：将 applicant_name/phone/email 迁移到 form_
          +data                                                          
      466  ```sql
      467  -- 将现有的 applicant_name, applicant_phone, applicant_email 
           数据直接迁移到 form_data 顶层
      468  UPDATE form_application

⏺ Update(docs/form_application.md)
  ⎿  Added 1 line, removed 1 line                                        
      483    AND (applicant_name IS NOT NULL OR applicant_phone IS NOT NU
           LL OR applicant_email IS NOT NULL);
      484  ```
      485  
      486 -### 5.3 删除旧字段（可选，建议先备份数据）                    
      486 +### 6.3 删除旧字段（可选，建议先备份数据）                    
      487  ```sql
      488  -- 删除旧的 applicant 字段
      489  -- 注意：执行前请确保数据已经迁移完成，并且做好备份

⏺ 文档已更新完成。现在让我更新 todo 列表并运行代码检查确保没有语法错误：

⏺ 让我运行代码检查确保没有语法错误：

⏺ Bash(python -m py_compile
      routers/form_application/requests/form_application_request.py
      routers/form_application/api/form_application_router.py
      services/form_applica…)
  ⎿  语法检查通过

⏺ 拼多多试用申请相关接口已添加完成。以下是修改摘要：

  修改内容

  1. 请求模型 (routers/form_application/requests/form_application_request.py)

  - 新增 PddTrialApplyRequest 类，包含字段：
    - pdd_account（必填）：拼多多客服账号
    - pdd_password（必填）：拼多多客服密码
    - pre_sales_group（可选）：售前转接组
    - after_sales_group（可选）：售后转发组
    - tech_support_link（可选）：邀请技术支持链接

  2. 服务层 (services/form_application/form_application_service.py)

  - 新增常量：PDD_TRIAL_FORM_CODE、PDD_TRIAL_FORM_NAME
  - 新增敏感字段：pdd_password
  - 新增钉钉 webhook 映射：pdd_trial_dingtalk_webhook
  - 新增校验函数：_validate_pdd_trial_form()
  - 新增查询方法：
    - get_user_latest_pdd_trial_application()
    - get_current_user_pdd_trial_application()
    - list_pdd_trial_applications_admin()

  3. 路由接口 (routers/form_application/api/form_application_router.py)

  - POST /form_application/pdd_trial - 拼多多试用申请提交
  - GET /form_application/pdd_trial/current - 获取当前用户拼多多试用申请
  - GET /form_application/user/{user_id}/pdd_trial/latest - 获取用户最新拼多多试用申请

  4. 文档 (docs/form_application.md)

  - 新增第二章：拼多多试用申请接口说明
  - 更新钉钉 webhook 配置示例

> curl 'https://customer-servhub-api.betteryeah.com/v1/chat/e064362bd8ae4eda
bdaf3f56418b9079/records?page_size=50&direction=prev' \
  -H 'accept: application/json' \
  -H 'accept-language: 
en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7,ko;q=0.6,ja;q=0.5,vi;q=0.4,de;q=0.3' \
  -H 'authorization: 
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI0NTAwMCIsImNsaWVudCI6ImFpX2Z
sb3ciLCJleHAiOjE3Njg0OTExMzN9.jC_wy7ESeEVmneMWry3BBkUAHqGeYpt-cY_15SX1PFc' \
  -H 'content-type: application/json' \
  -H 'dnt: 1' \
  -H 'origin: https://customer-servhub.betteryeah.com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://customer-servhub.betteryeah.com/' \
  -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not 
A(Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) 
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' 
使用这里的域名和token，构造拼多多接口的 所有curl用于测试 

⏺ 我来为你构造拼多多试用申请相关接口的测试 curl 命令。

  拼多多试用申请接口测试 curl

  1. 提交拼多多试用申请

  curl -X POST 'https://customer-servhub-api.betteryeah.com/v1/form_application/pdd_trial' \
    -H 'accept: application/json' \
    -H 'content-type: application/json' \
    -H 'authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI0NTAwMCIsImNsaWVudCI6ImFpX2Zsb3ciLCJleHAiOjE3Njg0OTExMzN9.jC_wy7ESeEVmneMWry3BBkUAHqGeYpt-cY_15SX1PFc' \
    -H 'origin: https://customer-servhub.betteryeah.com' \
    -d '{
      "pdd_account": "test_pdd_account",
      "pdd_password": "test_password_123",
      "pre_sales_group": "售前转接组A",
      "after_sales_group": "售后转发组B",
      "tech_support_link": "https://ai.example.com/login?type=invite&link_id=xxx"
    }'

  2. 获取当前用户拼多多试用申请

  curl -X GET 'https://customer-servhub-api.betteryeah.com/v1/form_application/pdd_trial/current' \
    -H 'accept: application/json' \
    -H 'content-type: application/json' \
    -H 'authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI0NTAwMCIsImNsaWVudCI6ImFpX2Zsb3ciLCJleHAiOjE3Njg0OTExMzN9.jC_wy7ESeEVmneMWry3BBkUAHqGeYpt-cY_15SX1PFc' \
    -H 'origin: https://customer-servhub.betteryeah.com'

  3. 通过 user_id 获取用户最新拼多多试用申请

  curl -X GET 'https://customer-servhub-api.betteryeah.com/v1/form_application/user/45000/pdd_trial/latest' \
    -H 'accept: application/json' \
    -H 'content-type: application/json' \
    -H 'authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI0NTAwMCIsImNsaWVudCI6ImFpX2Zsb3ciLCJleHAiOjE3Njg0OTExMzN9.jC_wy7ESeEVmneMWry3BBkUAHqGeYpt-cY_15SX1PFc' \
    -H 'origin: https://customer-servhub.betteryeah.com'

  4. 通过 apply_id 获取申请详情（通用接口）

  # 注意：需要将 {apply_id} 替换为实际的申请ID（从提交接口返回）
  curl -X GET 'https://customer-servhub-api.betteryeah.com/v1/form_application/detail/{apply_id}' \
    -H 'accept: application/json' \
    -H 'content-type: application/json' \
    -H 'authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI0NTAwMCIsImNsaWVudCI6ImFpX2Zsb3ciLCJleHAiOjE3Njg0OTExMzN9.jC_wy7ESeEVmneMWry3BBkUAHqGeYpt-cY_15SX1PFc' \
    -H 'origin: https://customer-servhub.betteryeah.com'

  5. 使用通用表单接口提交拼多多试用申请

  curl -X POST 'https://customer-servhub-api.betteryeah.com/v1/form_application/submit' \
    -H 'accept: application/json' \
    -H 'content-type: application/json' \
    -H 'authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI0NTAwMCIsImNsaWVudCI6ImFpX2Zsb3ciLCJleHAiOjE3Njg0OTExMzN9.jC_wy7ESeEVmneMWry3BBkUAHqGeYpt-cY_15SX1PFc' \
    -H 'origin: https://customer-servhub.betteryeah.com' \
    -d '{
      "form_code": "pdd_trial_apply",
      "form_name": "拼多多试用申请",
      "applicant_type": "individual",
      "form_data": {
        "pdd_account": "test_pdd_account",
        "pdd_password": "test_password_123",
        "pre_sales_group": "售前转接组A",
        "after_sales_group": "售后转发组B",
        "tech_support_link": "https://ai.example.com/login?type=invite&link_id=xxx"
      }
    }'

  ---
  测试建议：
  1. 先执行接口 1 或 5 提交申请，获取返回的 apply_id
  2. 然后用接口 2、3、4 查询申请详情
  3. user_id 从 token 中解析为 45000

> 用这个 curl 
'https://dev-customer-servhub-api.betteryeah.com/v1/customer-agent/list?page
=1&page_size=100&workspace_id=dc52759f093848c19cc8e24d0a5895e5' \
  -H 'accept: application/json' \
  -H 'accept-language: 
en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7,ko;q=0.6,ja;q=0.5,vi;q=0.4,de;q=0.3' \
  -H 'authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMDA1OC
IsImNsaWVudCI6ImFpX2Zsb3ciLCJleHAiOjM2MDE3NDI4ODI1MDJ9.3eL66kLcg2FHIpQsKQ22D
g-ObvPotAfZ_6SaUtqYeaM' \
  -H 'content-type: application/json' \
  -H 'dnt: 1' \
  -H 'origin: https://dev-customer-servhub.betteryeah.com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://dev-customer-servhub.betteryeah.com/' \
  -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not 
A(Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) 
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
  -H 'workspace-id: dc52759f093848c19cc8e24d0a5895e5' 构造curl 

⏺ 好的，我用 dev 环境的域名和 token 构造拼多多试用申请接口的测试 curl：

  拼多多试用申请接口测试 curl (dev 环境)

  1. 提交拼多多试用申请

  curl -X POST 'https://dev-customer-servhub-api.betteryeah.com/v1/form_application/pdd_trial' \
    -H 'accept: application/json' \
    -H 'content-type: application/json' \
    -H 'authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMDA1OCIsImNsaWVudCI6ImFpX2Zsb3ciLCJleHAiOjM2MDE3NDI4ODI1MDJ9.3eL66kLcg2FHIpQsKQ22Dg-ObvPotAfZ_6SaUtqYeaM' \
    -H 'origin: https://dev-customer-servhub.betteryeah.com' \
    -d '{
      "pdd_account": "test_pdd_account",
      "pdd_password": "test_password_123",
      "pre_sales_group": "售前转接组A",
      "after_sales_group": "售后转发组B",
      "tech_support_link": "https://ai.example.com/login?type=invite&link_id=xxx"
    }'


  curl -X POST 'http://localhost:8011/v1/form_application/pdd_trial' \
    -H 'accept: application/json' \
    -H 'content-type: application/json' \
    -H 'authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMDA1OCIsImNsaWVudCI6ImFpX2Zsb3ciLCJleHAiOjM2MDE3NDI4ODI1MDJ9.3eL66kLcg2FHIpQsKQ22Dg-ObvPotAfZ_6SaUtqYeaM' \
    -H 'origin: https://dev-customer-servhub.betteryeah.com' \
    -d '{
      "pdd_account": "test_pdd_account",
      "pdd_password": "test_password_123",
      "pre_sales_group": "售前转接组A",
      "after_sales_group": "售后转发组B",
      "tech_support_link": "https://ai.example.com/login?type=invite&link_id=xxx"
    }'

```json
{
  "code": 200,
  "success": true,
  "message": "SUCCESS",
  "data": {
    "apply_id": "00ac68e733a941078f84b387408daf48"
  },
  "request_id": "38068bdb7eff0ded40a5798c6e4b8b2c",
  "now_time": 1767929528
}


```


  2. 获取当前用户拼多多试用申请

  curl -X GET 'https://dev-customer-servhub-api.betteryeah.com/v1/form_application/pdd_trial/current' \
    -H 'accept: application/json' \
    -H 'content-type: application/json' \
    -H 'authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMDA1OCIsImNsaWVudCI6ImFpX2Zsb3ciLCJleHAiOjM2MDE3NDI4ODI1MDJ9.3eL66kLcg2FHIpQsKQ22Dg-ObvPotAfZ_6SaUtqYeaM' \
    -H 'origin: https://dev-customer-servhub.betteryeah.com'


  curl -X GET 'http://localhost:8011/v1/form_application/pdd_trial/current' \
    -H 'accept: application/json' \
    -H 'content-type: application/json' \
    -H 'authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMDA1OCIsImNsaWVudCI6ImFpX2Zsb3ciLCJleHAiOjM2MDE3NDI4ODI1MDJ9.3eL66kLcg2FHIpQsKQ22Dg-ObvPotAfZ_6SaUtqYeaM' \
    -H 'origin: https://dev-customer-servhub.betteryeah.com'

```json
{
  "code": 200,
  "success": true,
  "message": "SUCCESS",
  "data": {
    "id": 8,
    "apply_id": "00ac68e733a941078f84b387408daf48",
    "form_code": "pdd_trial_apply",
    "form_name": "拼多多试用",
    "user_id": "10058",
    "user_info": {
      "email": null,
      "phone": "13120272376",
      "user_id": "10058",
      "username": "夕谷",
      "enterprise_id": null
    },
    "applicant_type": null,
    "apply_status": "UnderReview",
    "audit_by": null,
    "audit_remark": null,
    "audit_at": null,
    "form_data": {
      "pdd_account": "test_pdd_account",
      "pdd_password": "******",
      "pre_sales_group": "售前转接组A",
      "after_sales_group": "售后转发组B",
      "tech_support_link": "https://ai.example.com/login?type=invite&link_id=xxx"
    },
    "created_at": "2026-01-09T11:32:08.546209",
    "updated_at": "2026-01-09T11:32:08.546210"
  },
  "request_id": "2c05a4606ab9d364b74e4c871f8d639e",
  "now_time": 1767929567
}

```


  3. 通过 user_id 获取用户最新拼多多试用申请

  curl -X GET 'https://dev-customer-servhub-api.betteryeah.com/v1/form_application/user/10058/pdd_trial/latest' \
    -H 'accept: application/json' \
    -H 'content-type: application/json' \
    -H 'authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMDA1OCIsImNsaWVudCI6ImFpX2Zsb3ciLCJleHAiOjM2MDE3NDI4ODI1MDJ9.3eL66kLcg2FHIpQsKQ22Dg-ObvPotAfZ_6SaUtqYeaM' \
    -H 'origin: https://dev-customer-servhub.betteryeah.com'

  4. 通过 apply_id 获取申请详情

  # 将 {apply_id} 替换为提交接口返回的实际申请ID
  curl -X GET 'https://dev-customer-servhub-api.betteryeah.com/v1/form_application/detail/{apply_id}' \
    -H 'accept: application/json' \
    -H 'content-type: application/json' \
    -H 'authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMDA1OCIsImNsaWVudCI6ImFpX2Zsb3ciLCJleHAiOjM2MDE3NDI4ODI1MDJ9.3eL66kLcg2FHIpQsKQ22Dg-ObvPotAfZ_6SaUtqYeaM' \
    -H 'origin: https://dev-customer-servhub.betteryeah.com'

  5. 通用表单接口提交

  curl -X POST 'https://dev-customer-servhub-api.betteryeah.com/v1/form_application/submit' \
    -H 'accept: application/json' \
    -H 'content-type: application/json' \
    -H 'authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMDA1OCIsImNsaWVudCI6ImFpX2Zsb3ciLCJleHAiOjM2MDE3NDI4ODI1MDJ9.3eL66kLcg2FHIpQsKQ22Dg-ObvPotAfZ_6SaUtqYeaM' \
    -H 'origin: https://dev-customer-servhub.betteryeah.com' \
    -d '{
      "form_code": "pdd_trial_apply",
      "form_data": {
        "pdd_account": "test_pdd_account",
        "pdd_password": "test_password_123"
      }
    }'

  ---
  说明：user_id 从 token 解析为 10058



