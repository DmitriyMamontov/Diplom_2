import allure
from user_methods import UserMethods
from data import Messages

@allure.feature("Авторизация пользователя")
class TestLoginUser:
    @allure.title("Логин под существующим пользователем")
    def test_login_registered_user(self, register_user):
        data = register_user
        response = UserMethods.login_user({"email": data["email"], "password": data["password"]})
        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 200
        with allure.step("Проверка сообщения в телe ответа"):
            assert response.json()["success"] is True

    @allure.title("Ошибка при неверном пароле")
    def test_login_with_invalid_credential_password(self, register_user):
        data = register_user
        response = UserMethods.login_user({"email": data["email"], "password": "wrongpass"})
        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 401
        with allure.step("Проверка сообщения в телe ответа"):
            assert response.json()["message"] == Messages.INVALID_CREDENTIALS

    @allure.feature("Авторизация пользователя")
    @allure.title("Ошибка при неверном email")
    def test_login_with_invalid_credential_email(self, register_user):
        data = register_user
        response = UserMethods.login_user({"email": "wrongemail", "password": data["password"]})
        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 401
        with allure.step("Проверка сообщения в телe ответа"):
            assert response.json()["message"] == Messages.INVALID_CREDENTIALS