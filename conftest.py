import pytest
from clients.api_client import APIClient


@pytest.fixture(scope="session")
def client():
    """全局唯一 client，复用 TCP 连接"""
    c = APIClient()
    yield c
    c.close()


@pytest.fixture
def posts_api(client):
    """帖子资源 API 的封装（更贴近业务）"""
    class PostsAPI:
        def list(self, **params):
            return client.get("/posts", params=params)

        def detail(self, post_id):
            return client.get(f"/posts/{post_id}")

        def create(self, payload):
            return client.post("/posts", json=payload)

        def update(self, post_id, payload):
            return client.put(f"/posts/{post_id}", json=payload)

        def delete(self, post_id):
            return client.delete(f"/posts/{post_id}")

    return PostsAPI()

@pytest.fixture(scope="session")
def auth_client(auth_token):
    """带 token 的客户端，复用 session"""
    c = APIClient(token=auth_token)
    yield c
    c.close()