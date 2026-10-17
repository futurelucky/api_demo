import requests
from config import config


class APIClient:
    """统一的接口请求封装"""

    def __init__(self, base_url: str = None, timeout: int = None):
        self.base_url = (base_url or config.BASE_URL).rstrip("/")
        self.timeout = timeout or config.TIMEOUT
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    def request(self, method: str, path: str, **kwargs):
        url = f"{self.base_url}/{path.lstrip('/')}"
        kwargs.setdefault("timeout", self.timeout)
        resp = self.session.request(method, url, **kwargs)

        # 打印日志便于排查
        print(f"\n>>> {method} {url}")
        if kwargs.get("json"):
            print(f">>> Body: {kwargs['json']}")
        print(f"<<< Status: {resp.status_code}")
        print(f"<<< Body: {resp.text[:300]}")
        return resp

    def get(self, path, **kw):    return self.request("GET", path, **kw)
    def post(self, path, **kw):   return self.request("POST", path, **kw)
    def put(self, path, **kw):    return self.request("PUT", path, **kw)
    def patch(self, path, **kw):  return self.request("PATCH", path, **kw)
    def delete(self, path, **kw): return self.request("DELETE", path, **kw)

    def close(self):
        self.session.close()