import allure
from messages import USER_EXISTS_ERR, EMPTY_PARAM_ERR
from routes.user_api import UserApi
from test_data import USER_DATA, DATA_WITH_1_EMPTY_PARAM
import pytest



class TestRegistrationApi:
    @pytest.fixture
    def new_user(self):
        user = UserApi()
        response = user.registration(body=USER_DATA)
        yield response
        user.delete(access_token=response.json().get('accessToken'))

    @allure.title('Успешная регистрация пользователя, проверка кода ответа 200.')
    def test_registration_success_200(self, new_user):
        assert new_user.status_code == 200

    @allure.title('Успешная регистрация пользователя, проверка тела ответа accessToken и refreshToken.')
    def test_registration_success_body(self, new_user):
        assert 'accessToken' in new_user.json() and 'refreshToken' in new_user.json()

    @allure.title('Успешное удаление пользователя, проверка кода ответа 202.')
    def test_delete_user_success_202(self):
        user = UserApi()
        response = user.registration(body=USER_DATA)
        response = user.delete(access_token=response.json().get('accessToken'))
        assert response.status_code == 202

    @allure.title('Регистрация пользователя с повторяющейся почтой, проверка кода ответа 403.')
    def test_registration_exists_user_403(self, new_user):
        user = UserApi()
        response = user.registration(body=USER_DATA)
        assert response.status_code == 403

    @allure.title('Регистрация пользователя с повторяющейся почтой, проверка тела ответа.')
    def test_registration_exists_user_body(self, new_user):
        user = UserApi()
        response = user.registration(body=USER_DATA)
        assert response.json() == USER_EXISTS_ERR

    @allure.title('Регистрация пользователя с не полными данными, проверка кода ответа 403.')
    @pytest.mark.parametrize('body', DATA_WITH_1_EMPTY_PARAM)
    def test_registration_with_empty_param_403(self, body):
        user = UserApi()
        response = user.registration(body=body)
        assert response.status_code == 403

    @allure.title('Регистрация пользователя с не полными данными, проверка тела ответа ошибки.')
    @pytest.mark.parametrize('body', DATA_WITH_1_EMPTY_PARAM)
    def test_registration_with_empty_param_body(self, body):
        user = UserApi()
        response = user.registration(body=body)
        assert response.json() == EMPTY_PARAM_ERR
