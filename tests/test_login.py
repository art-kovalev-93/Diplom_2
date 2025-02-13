import allure
from messages import WRONG_LOGIN_DATA_ERR
from routes.user_api import UserApi
from test_data import USER_DATA, WRONG_LOGIN_DATA
import pytest



class TestLoginApi:
    @pytest.fixture
    def new_user(self):
        user = UserApi()
        response = user.registration(body=USER_DATA)
        yield
        user.delete(access_token=response.json().get('accessToken'))

    @allure.title('Успешный логин пользователя, проверка кода ответа 200 и тела ответа. /api/auth/login. ')
    def test_login_success_200(self, new_user):
        user= UserApi()
        response = user.login(body=USER_DATA)
        assert response.status_code == 200 and 'accessToken' in response.json() and 'refreshToken' in response.json()

    @allure.title('Логин пользователя с ошибкой, проверка кода ответа 401 и тела ответа. /api/auth/login. ')
    @pytest.mark.parametrize('body', WRONG_LOGIN_DATA)
    def test_login_wrong_data_403(self, body):
        user = UserApi()
        response = user.login(body=body)
        assert response.status_code == 401 and response.json() == WRONG_LOGIN_DATA_ERR
