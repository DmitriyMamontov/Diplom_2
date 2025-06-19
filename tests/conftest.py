import pytest
import allure
from user_methods import UserMethods
from generators import *

@allure.step("Генерация тестовых данных пользователя")
@pytest.fixture()
def user_data():
    return {
        "email": generate_fake_email(),
        "password": generate_fake_password(),
        "name": generate_fake_name()
    }

@allure.step("Регистрация пользователя через API")
@pytest.fixture
def register_user(user_data):
    UserMethods.create_user(user_data)
    yield user_data

    token = UserMethods.login_user({"email": user_data["email"], "password": user_data["password"]}).json()["accessToken"]
    UserMethods.delete_user(token)

@allure.step("Получение токена авторизации")
@pytest.fixture
def auth_token(register_user):
    user = register_user
    return UserMethods.login_user({
        "email": user["email"],
        "password": user["password"]
    }).json()["accessToken"]