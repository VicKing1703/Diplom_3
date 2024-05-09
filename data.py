class Data:
    # Базовая URL
    BASE_URL = "https://stellarburgers.nomoreparties.site"

    LOGIN_URL = f"{BASE_URL}/login"  # URL страницы входа
    FORGOT_PASSWORD_URL = f"{BASE_URL}/forgot-password"  # URL страницы восстановления пароля

    ORDER_HISTORY_URL = f"{BASE_URL}/account/order-history"  # URL истории заказов в личном кабинете
    PROFILE_URL = f"{BASE_URL}/account/profile"  # URL профиля в личном кабинете
    FEED_URL = f"{BASE_URL}/feed"  # URL ленты заказов


class ChromeBrowser:

    WINDOW_SIZE = '--window-size=1920,1080'


class FirefoxBrowser:

    WIDTH = "--width=1920"
    HEIGHT = "--height=1080"


class TestAccount:

    TEST_MAIL = 'VictorKorol6123@yandex.ru'
    TEST_PASSWORD = '123456'
    TEST_NUMBER_ORDER = ''
