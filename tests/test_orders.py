import allure
from messages import UNAUTH_ERR
from receipt_generator import Generator
from routes.order_api import OrderApi
from routes.user_api import UserApi
from test_data import USER_DATA
import pytest



class TestOrdersApi:
    @pytest.fixture
    def new_user(self):
        user = UserApi()
        response = user.registration(body=USER_DATA)
        yield response
        user.delete(access_token=response.json().get('accessToken'))

    @allure.title('Получение списка ингредиентов, проверка кода ответа 200 и проверка тела ответа.')
    def test_get_ingredients_success_200(self):
        order = OrderApi()
        response = order.get_orders()
        assert response.status_code == 200 and response.json().get('success') == True

    @allure.title('Создание нового заказа, авторизированный пользователь, код ответа 200 и тело ответа success..')
    def test_create_order_success_200(self, new_user):
        order = OrderApi()
        response = order.create_order(access_token=new_user.json().get('accessToken'), ingredients=Generator.get_receipt())
        assert response.status_code == 200 and response.json().get('success') == True

    @allure.title('Создание нового заказа, НЕ авторизированный пользователь, код ответа 200 и  тело ответа success..')
    def test_create_order_success_no_auth_200(self):
        order = OrderApi()
        response = order.create_order(access_token='', ingredients=Generator.get_receipt())
        assert response.status_code == 200 and response.json().get('success') == True

    @allure.title('Создание нового заказа без ингредиентов, авторизированный пользователь, код ответа 400 и тело ответа success.')
    def test_create_order_fail_no_ingredients_400(self, new_user):
        order = OrderApi()
        response = order.create_order(access_token=new_user.json().get('accessToken'), ingredients=[])
        assert response.status_code == 400 and response.json().get('success') == False

    @allure.title('Создание нового заказа с неверным id ингредиентов, авторизированный пользователь, код ответа 500 Error.')
    def test_create_order_fail_wrong_id_ingredient_500(self, new_user):
        order = OrderApi()
        response = order.create_order(access_token=new_user.json().get('accessToken'), ingredients=["6123456"])
        assert response.status_code == 500 and 'Error' in response.text

    @allure.title('Получение списка заказов пользователя, авторизированный пользователь, код ответа 200, тело ответа Success и кол-во заказов..')
    def test_get_user_order_success_200(self, new_user):
        order = OrderApi()
        order.create_order(access_token=new_user.json().get('accessToken'), ingredients=Generator.get_receipt())
        response = order.get_user_orders(access_token=new_user.json().get('accessToken'))
        assert response.status_code == 200 and response.json().get('success') == True and len(response.json().get('orders')) == 1

    @allure.title('Получение списка заказов пользователя, не авторизированный пользователь, код ответа 401 и тело ответа Success.')
    def test_get_user_order_fail_401(self, new_user):
        order = OrderApi()
        order.create_order(access_token=new_user.json().get('accessToken'), ingredients=Generator.get_receipt())
        response = order.get_user_orders(access_token='')
        assert response.status_code == 401 and response.json() == UNAUTH_ERR
