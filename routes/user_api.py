import requests
import allure
from env import API_URL


class UserApi:

    @allure.step('Метод post /api/auth/register, регистрация пользователя')
    def registration(self, body):
        try:
            response = requests.post(f'{API_URL}/api/auth/register', data=body)
            return response
        except Exception as e:
            print(f'Ошибка при запросе /api/auth/register: {e}')


    @allure.step('Метод delete /api/auth/user, удаление пользователя')
    def delete(self, access_token):
        try:
            headers = {
                'Authorization': f'{access_token}'
            }
            response = requests.delete(f'{API_URL}/api/auth/user', headers=headers)
            return response
        except Exception as e:
            print(f'Ошибка при запросе /api/auth/user: {e}')

    @allure.step('Метод post /api/auth/login, логин пользователя')
    def login(self, body):
        try:
            response = requests.post(f'{API_URL}/api/auth/login', data=body)
            return response
        except Exception as e:
            print(f'Ошибка при запросе /api/auth/login: {e}')

    @allure.step('Метод get /api/auth/user, логин пользователя')
    def get_user_data(self, access_token):
        try:
            headers = {
                'Authorization': f'{access_token}'
            }
            response = requests.get(f'{API_URL}/api/auth/user', headers=headers)
            return response
        except Exception as e:
            print(f'Ошибка при запросе /api/auth/user: {e}')

    @allure.step('Метод patch /api/auth/user, изменение данных пользователя')
    def patch_user_data(self, access_token, body):
        try:
            headers = {
                'Authorization': f'{access_token}'
            }
            response = requests.patch(f'{API_URL}/api/auth/user', headers=headers, data=body)
            return  response
        except Exception as e:
            print(f'Ошибка при запросе /api/auth/user: {e}')


