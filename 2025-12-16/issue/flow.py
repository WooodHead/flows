import asyncio
import json
from typing import Any, Dict, List, Union
from urllib.parse import parse_qs, urlparse

from betteryeah import BetterYeah

better_yeah = BetterYeah()

DEFAULT_ISSUE_URL = "https://customer-servhub-api.betteryeah.com/v1/issues/529732775"
RECORDS_URL_TEMPLATE = (
    "https://customer-servhub-api.betteryeah.com/v1/chat/{conversation_id}"
    "/records?page_size=20&current_id=2707336&direction=prev"
)
COMMON_HEADERS = {
    "sec-ch-ua-platform": '"macOS"',
    "Authorization": (
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI0NTAwMCIsImNsaWVudCI6ImFpX2Zs"
        "b3ciLCJleHAiOjE3NjU4OTY1NDd9.WDFDVkTFMU_gCf5iw7o2M0ZwCKzJxJkFECFQldzHuUM"
    ),
    "Referer": "https://customer-servhub.betteryeah.com/",
    "sec-ch-ua": '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
    "DNT": "1",
    "Content-Type": "application/json",
}


def log_error(message: str) -> None:
    """输出统一的错误提示"""
    print(f"[flow-error] {message}")


def resolve_issue_url(raw_issue_url: Any) -> str:
    """将 issue_url 标准化为 API 地址字符串"""

    def _extract(value: Any, depth: int = 0) -> str:
        if depth > 5 or value is None:
            return ""
        if isinstance(value, str):
            return value.strip()
        if isinstance(value, dict):
            for key in ("value", "url", "issue_url", "data"):
                if key in value:
                    nested = _extract(value.get(key), depth + 1)
                    if nested:
                        return nested
            return ""
        return str(value).strip()

    url_text = _extract(raw_issue_url) or ""
    if not url_text:
        return ""

    parsed = urlparse(url_text)

    def _build_api_url(issue_id: str) -> str:
        if not issue_id:
            return ""
        return f"https://customer-servhub-api.betteryeah.com/v1/issues/{issue_id}"

    # 处理前端页面链接，需要转换到 API
    if parsed.netloc.endswith("customer-servhub.betteryeah.com"):
        query_id = parse_qs(parsed.query or "").get("selectedIssue", [None])[0]
        if query_id:
            return _build_api_url(query_id)

        # 试图从 path 中获取 ID，例如 /issues/123456
        path_parts = [part for part in parsed.path.split("/") if part]
        if path_parts:
            candidate = path_parts[-1]
            if candidate.isdigit():
                return _build_api_url(candidate)

    return url_text


def _fetch_json_sync(url: str, headers: Dict[str, str]) -> Union[Dict[str, Any], List[Any]]:
    """Blocking helper that performs a GET request and returns parsed JSON."""
    from urllib.error import HTTPError, URLError
    from urllib.request import Request, urlopen

    request = Request(url, headers=headers, method="GET")

    try:
        with urlopen(request, timeout=15) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            payload = response.read().decode(charset)
            return json.loads(payload)
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="ignore")
        log_error(f"请求失败 {url}: HTTP {exc.code} {detail}")
        raise RuntimeError(f"HTTP {exc.code} when requesting {url}: {detail}") from exc
    except URLError as exc:
        log_error(f"网络不可达 {url}: {exc}")
        raise RuntimeError(f"Failed to reach {url}: {exc}") from exc
    except json.JSONDecodeError as exc:
        log_error(f"解析 JSON 失败 {url}: {exc}")
        raise RuntimeError(f"Invalid JSON from {url}: {exc}") from exc
    except Exception as exc:
        log_error(f"未知错误 {url}: {exc}")
        raise


async def fetch_json(url: str, headers: Dict[str, str]) -> Union[Dict[str, Any], List[Any]]:
    try:
        return await asyncio.to_thread(_fetch_json_sync, url, headers)
    except Exception as exc:
        log_error(f"获取数据异常 {url}: {exc}")
        raise


def extract_user_message_lines(records_response: Union[Dict[str, Any], List[Any]]) -> str:
    """Create newline separated text for user messages, including image URLs."""

    try:
        def _collect_records(source: Union[Dict[str, Any], List[Any]]) -> List[Dict[str, Any]]:
            if isinstance(source, list):
                return [item for item in source if isinstance(item, dict)]
            if isinstance(source, dict):
                for key in ("data", "records", "items"):
                    value = source.get(key)
                    if isinstance(value, list):
                        return [item for item in value if isinstance(item, dict)]
            return []

        def _normalize_images(candidate: Any) -> List[str]:
            if isinstance(candidate, str):
                candidate = candidate.strip()
                return [candidate] if candidate else []

            if isinstance(candidate, (list, tuple, set)):
                normalized = []
                for item in candidate:
                    if isinstance(item, str) and item.strip():
                        normalized.append(item.strip())
                return normalized
            return []

        lines: List[str] = []

        for record in _collect_records(records_response):
            if record.get("role") != "user":
                continue

            context = record.get("context") or {}
            text = ""
            if isinstance(context, dict):
                context_text = context.get("text")
                if isinstance(context_text, str):
                    text = context_text.strip()
                images = _normalize_images(context.get("image")) + _normalize_images(context.get("images"))
            else:
                images = []

            parts = []
            if text:
                parts.append(text)
            if images:
                parts.extend(images)

            if parts:
                lines.append(" ".join(parts))

        return "\n".join(lines)
    except Exception as exc:
        log_error(f"解析聊天记录出错: {exc}")
        return ""


# 必须保证节点中存在一个main函数
# 你的代码应该在main函数中编写
# main函数的返回值为当前节点的返回值
async def main():
    raw_issue_url = globals().get("issue_url", None)
    ISSUE_URL = resolve_issue_url(raw_issue_url)
    if not ISSUE_URL:
        ISSUE_URL = DEFAULT_ISSUE_URL

    try:
        issue_response = await fetch_json(ISSUE_URL, COMMON_HEADERS)
    except Exception:
        log_error("获取工单详情失败")
        raise

    try:
        conversation_id = (
            issue_response.get("data", {}).get("conversation_id")
            if isinstance(issue_response, dict)
            else None
        )
    except Exception as exc:
        log_error(f"解析会话ID失败: {exc}")
        raise

    if not conversation_id:
        log_error("会话ID不存在，无法继续查询聊天记录")
        raise RuntimeError("会话ID不存在，无法继续查询聊天记录")

    records_url = RECORDS_URL_TEMPLATE.format(conversation_id=conversation_id)

    try:
        records_response = await fetch_json(records_url, COMMON_HEADERS)
    except Exception:
        log_error("获取聊天记录失败")
        raise

    try:
        user_message_lines = extract_user_message_lines(records_response)
    except Exception:
        log_error("提取用户消息失败")
        raise

    return {
        "conversation_id": conversation_id,
        "issue": issue_response,
        "records": records_response,
        "user_messages": user_message_lines,
    }
