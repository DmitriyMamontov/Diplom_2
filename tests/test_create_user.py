import allure
from user_methods import UserMethods
from data import Messages

@allure.feature("Регистрация пользователя")
@allure.story("Успешная регистрация нового пользователя")
def test_create_unique_user(user_data):
    response = UserMethods.create_user(user_data)
    assert response.status_code == 200
    assert response.json()["success"] is True


@allure.feature("Регистрация пользователя")
@allure.story("Ошибка при регистрации существующего пользователя")
def test_create_existing_user(user_data):
    UserMethods.create_user(user_data)
    second_response = UserMethods.create_user(user_data)
    assert second_response.status_code == 403
    assert second_response.json()["message"] == Messages.USER_EXISTS

@allure.feature("Регистрация пользователя")
@allure.story("Ошибка при регистрации нового пользователя с не заполненным полем name")
def test_create_user_empty_name(user_data):
    invalid_data = {
        "email": user_data["email"],
        "password": user_data["password"],
        "name": ""
    }
    response = UserMethods.create_user(invalid_data)

    assert response.status_code == 403
    assert response.json()["message"] == Messages.REQUIRED_FIELDS

@allure.feature("Регистрация пользователя")
@allure.story("Ошибка при регистрации нового пользователя с не заполненным полем email")
def test_create_user_empty_email(user_data):
    invalid_data = {
        "email": "",
        "password": user_data["password"],
        "name": user_data["name"]
    }
    response = UserMethods.create_user(invalid_data)

    assert response.status_code == 403
    assert response.json()["message"] == Messages.REQUIRED_FIELDS

@allure.feature("Регистрация пользователя")
@allure.story("Ошибка при регистрации нового пользователя с не заполненным полем password")
def test_create_user_empty_password(user_data):
    invalid_data = {
        "email": user_data["email"],
        "password": "",
        "name": user_data["name"]
    }
    response = UserMethods.create_user(invalid_data)

    assert response.status_code == 403
    assert response.json()["message"] == Messages.REQUIRED_FIELDS