class Url:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"
    CREATE_USER = "/auth/register"
    LOGIN_USER = "/auth/login"
    UPDATE_USER = "/auth/user"
    CREATE_ORDER = "/orders"
    GET_ORDERS = "/orders"
    INGREDIENTS = "/ingredients"

class Messages:
    USER_EXISTS = "User already exists"
    INVALID_CREDENTIALS = "email or password are incorrect"
    REQUIRED_FIELDS = "Email, password and name are required fields"
    NO_INGREDIENTS = "Ingredient ids must be provided"
    INVALID_INGREDIENT = "invalid"
    UNAUTHORIZED = "You should be authorised"
