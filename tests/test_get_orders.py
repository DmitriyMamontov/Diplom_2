import allure
from order_methods import OrderMethods
from data import Messages

@allure.feature("Получение заказов")
@allure.story("Получение с авторизацией")
def test_get_orders_with_auth(auth_token):
    response = OrderMethods.get_orders(auth_token)
    assert response.status_code == 200
    assert "orders" in response.json()


@allure.feature("Получение заказов")
@allure.story("Ошибка без авторизации")
def test_get_orders_without_auth():
    response = OrderMethods.get_orders()
    assert response.status_code == 401
    assert response.json()["message"] == Messages.UNAUTHORIZED