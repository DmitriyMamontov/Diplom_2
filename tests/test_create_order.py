import allure
from order_methods import OrderMethods
from data import Messages

@allure.feature("Создание заказа")
class TestOrderCreation:
    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, auth_token):
        ingredients = OrderMethods.get_ingredients().json()["data"]
        body = {"ingredients": [item["_id"] for item in ingredients[:2]]}
        response = OrderMethods.create_order(body, auth_token)
        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 200
        with allure.step("Проверка сообщения в телe ответа"):
            assert "order" in response.json()

    @allure.title("Создание без авторизации")
    def test_create_order_without_auth(self):
        ingredients = OrderMethods.get_ingredients().json()["data"]
        body = {"ingredients": [item["_id"] for item in ingredients[:2]]}
        response = OrderMethods.create_order(body)
        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 200
        with allure.step("Проверка сообщения в телe ответа"):
            assert "order" in response.json()

    @allure.title("Без ингредиентов")
    def test_create_order_without_ingredients(self, auth_token):
        response = OrderMethods.create_order({}, auth_token)
        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 400
        with allure.step("Проверка сообщения в телe ответа"):
            assert response.json()["message"] == Messages.NO_INGREDIENTS

    @allure.title("С невалидным хешем")
    def test_create_order_with_invalid_ingredient_hash(self, auth_token):
        response = OrderMethods.create_order({"ingredients": ["invalid_id_123"]}, auth_token)
        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 500
        with allure.step("Проверка сообщения в телe ответа"):
            assert Messages.SERVER_ERROR in response.text
