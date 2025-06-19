import allure
from user_methods import UserMethods
from data import Messages
from generators import *


@allure.feature("Изменение данных пользователя")
@allure.story("Изменение с авторизацией имени")
def test_update_user_with_auth(auth_token, register_user):
    new_name = generate_fake_name()
    register_user["name"] = new_name
    response = UserMethods.update_user({"name": new_name}, auth_token)
    assert response.status_code == 200
    assert response.json()["user"]["name"] == new_name

@allure.feature("Изменение данных пользователя")
@allure.story("Изменение с авторизацией email")
def test_update_email_with_auth(auth_token, register_user):
    new_email = generate_fake_email()
    register_user["email"] = new_email
    response = UserMethods.update_user({"email": new_email}, auth_token)
    assert response.status_code == 200
    assert response.json()["user"]["email"] == new_email

@allure.feature("Изменение данных пользователя")
@allure.story("Ошибка без авторизации при смене имени")
def test_update_user_without_auth(register_user):
    new_name = generate_fake_name()
    response = UserMethods.update_user({"name": new_name}, token=None)
    assert response.status_code == 401
    assert response.json()["message"] == Messages.UNAUTHORIZED

@allure.feature("Изменение данных пользователя")
@allure.story("Ошибка без авторизации при смене email")
def test_update_email_without_auth(register_user):
    new_email = generate_fake_email()
    response = UserMethods.update_user({"email": new_email}, token=None)
    assert response.status_code == 401
    assert response.json()["message"] == Messages.UNAUTHORIZED