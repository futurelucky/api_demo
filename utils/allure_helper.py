import json
import allure


def attach_response(resp, max_len=3000):
    """把请求/响应附加到 Allure 报告"""
    try:
        allure.attach(
            f"{resp.request.method} {resp.request.url}",
            name="Request",
            attachment_type=allure.attachment_type.TEXT,
        )
        if resp.request.body:
            body = resp.request.body
            if isinstance(body, bytes):
                body = body.decode("utf-8", errors="ignore")
            allure.attach(str(body)[:max_len], name="Request Body",
                          attachment_type=allure.attachment_type.TEXT)

        allure.attach(str(resp.status_code), name="Status Code",
                      attachment_type=allure.attachment_type.TEXT)

        try:
            pretty = json.dumps(resp.json(), ensure_ascii=False, indent=2)
        except Exception:
            pretty = resp.text
        allure.attach(pretty[:max_len], name="Response",
                      attachment_type=allure.attachment_type.JSON)
    except Exception:
        # 附加失败不影响用例
        pass


def attach_text(content, name="info"):
    allure.attach(str(content), name=name,
                  attachment_type=allure.attachment_type.TEXT)