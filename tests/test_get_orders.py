import allure
from order_methods import OrderMethods
from data import Messages

@allure.feature("Получение заказов")
class TestGetOrders:
    @allure.title("Получение с авторизацией")
    def test_get_orders_with_auth(self, auth_token):
        response = OrderMethods.get_orders(auth_token)
        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 200
        with allure.step("Проверка сообщения в телe ответа"):
            assert "orders" in response.json()

    @allure.title("Ошибка без авторизации")
    def test_get_orders_without_auth(self):
        response = OrderMethods.get_orders()
        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 401
        with allure.step("Проверка сообщения в телe ответа"):
            assert response.json()["message"] == Messages.UNAUTHORIZED