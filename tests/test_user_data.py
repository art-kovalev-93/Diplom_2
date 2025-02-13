import allure
from messages import SUCCESS_LOGIN, UNAUTH_ERR
from routes.user_api import UserApi
from test_data import USER_DATA, PATCH_DATA
import pytest



class TestUserDataApi:
    @pytest.fixture
    def new_user(self):
        user = UserApi()
        response = user.registration(body=USER_DATA)
        yield response
        user.delete(access_token=response.json().get('accessToken'))

    @allure.title('Получение данных пользователя, проверка кода ответа 200, проверка тела ответа.')
    def test_get_user_data_success_200(self, new_user):
        user = UserApi()
        response = user.get_user_data(access_token=new_user.json().get('accessToken'))
        assert response.status_code == 200 and response.json() == SUCCESS_LOGIN

    @allure.title('Изменение данных пользователя, проверка кода ответа 200, проверка тела ответа.')
    @pytest.mark.parametrize('body', PATCH_DATA)
    def test_patch_user_data_success_200(self, new_user, body):
        user = UserApi()
        value = next(iter(body.values()))
        response = user.patch_user_data(access_token=new_user.json().get('accessToken'), body=body)
        assert response.status_code == 200 and (value in response.json()['user']['email'] or value in response.json()['user']['name'])

    @allure.title('Изменение данных пользователя без авторизации, проверка кода ответа 401, проверка тела ответа.')
    @pytest.mark.parametrize('body', PATCH_DATA)
    def test_patch_user_data_no_auth_401(self, new_user, body):
        user = UserApi()
        response = user.patch_user_data(access_token='', body=body)
        assert response.status_code == 401 and response.json() == UNAUTH_ERR
