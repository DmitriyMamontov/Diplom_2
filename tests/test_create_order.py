import allure
from order_methods import OrderMethods
from data import Messages

@allure.feature("Создание заказа")
@allure.story("Создание с авторизацией")
def test_create_order_with_auth(auth_token):
    ingredients = OrderMethods.get_ingredients().json()["data"]
    body = {"ingredients": [item["_id"] for item in ingredients[:2]]}
    response = OrderMethods.create_order(body, auth_token)
    assert response.status_code == 200
    assert "order" in response.json()


@allure.feature("Создание заказа")
@allure.story("Создание без авторизации")
def test_create_order_without_auth():
    ingredients = OrderMethods.get_ingredients().json()["data"]
    body = {"ingredients": [item["_id"] for item in ingredients[:2]]}
    response = OrderMethods.create_order(body)
    assert response.status_code == 200


@allure.feature("Создание заказа")
@allure.story("Без ингредиентов")
def test_create_order_without_ingredients(auth_token):
    response = OrderMethods.create_order({}, auth_token)
    assert response.status_code == 400
    assert response.json()["message"] == Messages.NO_INGREDIENTS


@allure.feature("Создание заказа")
@allure.story("С невалидным хешем")
def test_create_order_with_invalid_ingredient_hash(auth_token):
    response = OrderMethods.create_order({"ingredients": ["invalid_id_123"]}, auth_token)
    assert response.status_code == 500
