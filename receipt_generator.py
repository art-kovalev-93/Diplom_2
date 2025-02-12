from random import random
import random
from routes.order_api import OrderApi


class Generator:
    @staticmethod
    def ingredients():
        order = OrderApi()
        response = order.get_ingredients()
        return response

    @staticmethod
    def get_buns_list():
        ingredients = Generator.ingredients()
        buns_list=[]
        ingredients_json = ingredients.json()['data']
        for ingredient in ingredients_json:
            if ingredient.get('type') == 'bun':
                buns_list.append(ingredient.get('_id'))
        return buns_list

    @staticmethod
    def get_main_list():
        ingredients = Generator.ingredients()
        main_list = []
        ingredients_json = ingredients.json()['data']
        for ingredient in ingredients_json:
            if ingredient.get('type') == 'main':
                main_list.append(ingredient.get('_id'))
        return main_list

    @staticmethod
    def get_sauce_list():
        ingredients = Generator.ingredients()
        sauce_list = []
        ingredients_json = ingredients.json()['data']
        for ingredient in ingredients_json:
            if ingredient.get('type') == 'sauce':
                sauce_list.append(ingredient.get('_id'))
        return sauce_list

    @staticmethod
    def get_receipt():
        receipt = []
        buns = Generator.get_buns_list()
        main = Generator.get_main_list()
        sauce = Generator.get_sauce_list()
        receipt.append(random.choice(buns))
        receipt.append(random.choice(main))
        receipt.append(random.choice(sauce))
        return receipt
