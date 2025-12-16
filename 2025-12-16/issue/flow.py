import asyncio
import json
from typing import Any, Dict, List, Union

from betteryeah import BetterYeah

better_yeah = BetterYeah()

ISSUE_URL = "https://customer-servhub-api.betteryeah.com/v1/issues/529732775"
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
        raise RuntimeError(f"HTTP {exc.code} when requesting {url}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"Failed to reach {url}: {exc}") from exc


async def fetch_json(url: str, headers: Dict[str, str]) -> Union[Dict[str, Any], List[Any]]:
    return await asyncio.to_thread(_fetch_json_sync, url, headers)


def extract_user_message_lines(records_response: Union[Dict[str, Any], List[Any]]) -> str:
    """Create newline separated text for user messages, including image URLs."""

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


# 必须保证节点中存在一个main函数
# 你的代码应该在main函数中编写
# main函数的返回值为当前节点的返回值
async def main():
    issue_response = await fetch_json(ISSUE_URL, COMMON_HEADERS)

    conversation_id = (
        issue_response.get("data", {}).get("conversation_id")
        if isinstance(issue_response, dict)
        else None
    )

    if not conversation_id:
        raise RuntimeError("会话ID不存在，无法继续查询聊天记录")

    records_url = RECORDS_URL_TEMPLATE.format(conversation_id=conversation_id)
    records_response = await fetch_json(records_url, COMMON_HEADERS)
    user_message_lines = extract_user_message_lines(records_response)

    return {
        "conversation_id": conversation_id,
        "issue": issue_response,
        "records": records_response,
        "user_messages": user_message_lines,
    }
