
## 接口说明

## 一、京东试用申请接口

### 1.1 京东试用申请提交（POST）
```bash
# 方式1：使用京东试用专用接口
curl -X POST '/v1/form_application/jd_trial' \
  -H 'Content-Type: application/json' \
  -d '{
    "jd_account": "jd_cs_account",
    "jd_password": "secret",
    "pre_sales_group": "售前转接组A",
    "after_sales_group": "售后转发组B",
    "tech_support_link": "https://ai.example.com/login?type=invite&link_id=xxx"
  }'

**响应示例**：
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "apply_id": "abc123def456"
  }
}
```

### 1.2 获取京东试用申请详情（GET）
```bash
# 方式1：获取当前登录用户的京东试用申请（推荐，无需传参）
curl -X GET '/v1/form_application/jd_trial/current' \
  -H 'Authorization: Bearer YOUR_TOKEN'


### 3.2 管理员获取京东试用申请列表
```bash
curl -X GET '/v1/admin/form_application/jd_trial/list?page=1&page_size=20' \
  -H 'Authorization: Bearer YOUR_TOKEN'
```

**权限说明**：仅 `ADMIN` 或 `SYSTEM_ADMIN` 角色可访问

**响应示例**：
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [
      {
        "id": 123,
        "apply_id": "abc123def456",
        "form_code": "jd_trial_apply",
        "form_name": "京东试用申请",
        "user_id": "user_12345",
        "user_info": {
          "user_id": "user_12345",
          "username": "张三",
          "email": "zhangsan@example.com",
          "phone": "13800000000",
          "enterprise_id": "ent_001"
        },
        "applicant_type": "individual",
        "apply_status": "UnderReview",
        "audit_by": null,
        "audit_remark": null,
        "audit_at": null,
        "form_data": {
          "jd_account": "jd_cs_account",
          "jd_password": "******",
          "pre_sales_group": "售前转接组A",
          "after_sales_group": "售后转发组B",
          "tech_support_link": "https://ai.example.com/login?type=invite&link_id=xxx"
        },
        "created_at": "2025-01-01T10:00:00",
        "updated_at": "2025-01-01T10:00:00"
      }
    ],
    "total": 1,
    "page": 1,
    "page_size": 20
  }
}


curl -X POST 'https://dev-customer-servhub-api.betteryeah.com/v1/form_application/jd_trial' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMDA1OCIsImNsaWVudCI6ImFpX2Zsb3ciLCJleHAiOjM2MDE3NDI4ODI1MDJ9.3eL66kLcg2FHIpQsKQ22Dg-ObvPotAfZ_6SaUtqYeaM' \
  -d '{
    "jd_account": "jd_cs_account",
    "jd_password": "secret",
    "pre_sales_group": "售前转接组A",
    "after_sales_group": "售后转发组B",
    "tech_support_link": "https://ai.example.com/login?type=invite&link_id=xxx"
  }'


 curl -X GET 'https://dev-customer-servhub-api.betteryeah.com/v1/form_application/jd_trial/current' \
>   -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMDA1OCIsImNsaWVudCI6ImFpX2Zsb3ciLCJleHAiOjM2MDE3NDI4ODI1MDJ9.3eL66kLcg2FHIpQsKQ22Dg-ObvPotAfZ_6SaUtqYeaM'


curl -X GET 'https://dev-customer-servhub-api.betteryeah.com/v1/admin/form_application/jd_trial/list?page=1&page_size=20' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMDA1OCIsImNsaWVudCI6ImFpX2Zsb3ciLCJleHAiOjM2MDE3NDI4ODI1MDJ9.3eL66kLcg2FHIpQsKQ22Dg-ObvPotAfZ_6SaUtqYeaM'


