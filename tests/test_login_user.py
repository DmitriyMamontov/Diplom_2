import allure
from user_methods import UserMethods
from data import Messages

@allure.feature("Авторизация пользователя")
@allure.story("Логин под существующим пользователем")
def test_login_registered_user(register_user):
    data = register_user
    response = UserMethods.login_user({"email": data["email"], "password": data["password"]})
    assert response.status_code == 200
    assert response.json()["success"] is True

@allure.feature("Авторизация пользователя")
@allure.story("Ошибка при неверном пароле")
def test_login_with_invalid_credential_password(register_user):
    data = register_user
    response = UserMethods.login_user({"email": data["email"], "password": "wrongpass"})
    assert response.status_code == 401
    assert response.json()["message"] == Messages.INVALID_CREDENTIALS

@allure.feature("Авторизация пользователя")
@allure.story("Ошибка при неверном email")
def test_login_with_invalid_credential_email(register_user):
    data = register_user
    response = UserMethods.login_user({"email": "wrongemail", "password": data["password"]})
    assert response.status_code == 401
    assert response.json()["message"] == Messages.INVALID_CREDENTIALS