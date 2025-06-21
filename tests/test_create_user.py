import allure
from user_methods import UserMethods
from data import Messages

@allure.feature("Регистрация пользователя")
class TestRegistrationUser:

    @allure.title("Успешная регистрация нового пользователя")
    def test_create_unique_user(self, user_data):
        response = UserMethods.create_user(user_data)
        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 200
        with allure.step("Проверка сообщения в телe ответа"):
            assert response.json()["success"] is True

    @allure.title("Ошибка при регистрации существующего пользователя")
    def test_create_existing_user(self, register_user):
        second_response = UserMethods.create_user(register_user)
        with allure.step("Проверка статус кода ответа"):
            assert second_response.status_code == 403
        with allure.step("Проверка сообщения в телe ответа"):
            assert second_response.json()["message"] == Messages.USER_EXISTS

    @allure.title("Ошибка при регистрации нового пользователя с не заполненным полем name")
    def test_create_user_empty_name(self, user_data):
        invalid_data = {
            "email": user_data["email"],
            "password": user_data["password"],
            "name": ""
        }
        response = UserMethods.create_user(invalid_data)
        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 403
        with allure.step("Проверка сообщения в телe ответа"):
            assert response.json()["message"] == Messages.REQUIRED_FIELDS

    @allure.title("Ошибка при регистрации нового пользователя с не заполненным полем email")
    def test_create_user_empty_email(self, user_data):
        invalid_data = {
            "email": "",
            "password": user_data["password"],
            "name": user_data["name"]
        }
        response = UserMethods.create_user(invalid_data)
        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 403
        with allure.step("Проверка сообщения в телe ответа"):
            assert response.json()["message"] == Messages.REQUIRED_FIELDS

    @allure.title("Ошибка при регистрации нового пользователя с не заполненным полем password")
    def test_create_user_empty_password(self, user_data):
        invalid_data = {
            "email": user_data["email"],
            "password": "",
            "name": user_data["name"]
        }
        response = UserMethods.create_user(invalid_data)
        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 403
        with allure.step("Проверка сообщения в телe ответа"):
            assert response.json()["message"] == Messages.REQUIRED_FIELDS