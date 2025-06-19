import requests
from data import Url

class OrderMethods:
    @staticmethod
    def get_ingredients():
        return requests.get(f"{Url.BASE_URL}/ingredients")

    @staticmethod
    def create_order(body, token=None):
        headers = {}
        if token:
            headers["Authorization"] = token
        return requests.post(f"{Url.BASE_URL}{Url.CREATE_ORDER}", json=body, headers=headers)

    @staticmethod
    def get_orders(token=None):
        headers = {}
        if token:
            headers["Authorization"] = token
        return requests.get(f"{Url.BASE_URL}{Url.GET_ORDERS}", headers=headers)