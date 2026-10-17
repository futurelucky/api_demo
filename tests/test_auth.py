import allure
import pytest
from config import config


@allure.epic("API 自动化测试")
@allure.feature("登录鉴权")
class TestAuth:

    @allure.story("正常登录")
    @allure.title("正确账号密码登录成功并返回 token")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_login_success(self, api_client):
        with allure.step("发送登录请求"):
            resp = api_client.post("/auth/login", json={
                "username": config.USERNAME,
                "password": config.PASSWORD,
            })
        with allure.step("断言状态码 200"):
            assert resp.status_code == 200
        with allure.step("断言返回 accessToken"):
            data = resp.json()
            assert "accessToken" in data and len(data["accessToken"]) > 10
            assert data["username"] == config.USERNAME

    @allure.story("异常登录")
    @allure.title("密码错误登录失败")
    @pytest.mark.regression
    def test_login_wrong_password(self, api_client):
        resp = api_client.post("/auth/login", json={
            "username": config.USERNAME,
            "password": "wrong_password",
        })
        assert resp.status_code in (400, 401), f"应拒绝: {resp.text}"

    @allure.story("鉴权校验")
    @allure.title("携带有效 token 访问 /auth/me 成功")
    @pytest.mark.smoke
    def test_access_with_token(self, auth_client):
        with allure.step("GET /auth/me"):
            resp = auth_client.get("/auth/me")
        assert resp.status_code == 200
        with allure.step("校验返回用户名一致"):
            assert resp.json()["username"] == config.USERNAME

    @allure.story("鉴权校验")
    @allure.title("无 token 访问受保护接口被拒绝")
    @pytest.mark.regression
    def test_access_without_token(self, api_client):
        api_client.clear_token()
        resp = api_client.get("/auth/me")
        assert resp.status_code in (401, 403)

    @allure.story("鉴权校验")
    @allure.title("伪造 token 被拒绝")
    def test_access_with_bad_token(self, api_client):
        api_client.set_token("this.is.a.fake.token")
        resp = api_client.get("/auth/me")
        assert resp.status_code in (401, 403)
        api_client.clear_token()