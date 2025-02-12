import requests
import allure
from env import API_URL



class OrderApi:

    @allure.step('Метод get /api/orders/all, получить все заказы')
    def get_orders(self):
        try:
            response = requests.get(f'{API_URL}/api/orders/all')
            return response
        except Exception as e:
            print(f'Ошибка при запросе /api/orders/all: {e}')

    @allure.step('Метод get /api/orders, получить заказы пользователя')
    def get_user_orders(self, access_token):
        try:
            headers = {
                'Authorization': f'{access_token}'
            }
            response = requests.get(f'{API_URL}/api/orders', headers=headers)
            return response
        except Exception as e:
            print(f'Ошибка при запросе /api/orders: {e}')

    @allure.step('Метод get /api/ingredients, получить список ингредиентов')
    def get_ingredients(self):
        try:
            response = requests.get(f'{API_URL}/api/ingredients')
            return response
        except Exception as e:
            print(f'Ошибка при запросе /api/ingredients: {e}')

    @allure.step('Метод post /api/orders, Оформление заказа')
    def create_order(self, access_token, ingredients):
        try:
            headers = {
                'Authorization': f'{access_token}'
            }
            ingredients_json = {
                'ingredients': ingredients
            }
            response = requests.post(f'{API_URL}/api/orders', headers=headers, json=ingredients_json)
            return response
        except Exception as e:
            print(f'Ошибка при запросе /api/orders: {e}')