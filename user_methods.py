import requests
from urls import Url

class UserMethods:
    @staticmethod
    def create_user(body):
        return requests.post(f"{Url.BASE_URL}{Url.CREATE_USER}", json=body)

    @staticmethod
    def login_user(body):
        return requests.post(f"{Url.BASE_URL}{Url.LOGIN_USER}", json=body)

    @staticmethod
    def update_user(body, token):
        headers = {"Authorization": token}
        return requests.patch(f"{Url.BASE_URL}{Url.UPDATE_USER}", json=body, headers=headers)

    @staticmethod
    def delete_user(token):
        headers = {"Authorization": token}
        return requests.delete(f"{Url.BASE_URL}{Url.UPDATE_USER}", headers=headers)