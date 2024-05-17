from selenium.webdriver.common.by import By


class AccountProfilePageLocators:

    # кнопка "Выйти"
    KEY_LOGOUT = (By.XPATH, '//button[text()="Выход"]')

    # кнопка "История заказов"
    KEY_HISTORY_ORDER = (By.XPATH, '//a[text()="История заказов"]')

    # список истории заказов
    LIST_ACC_ORDER_HISTORY = (By.XPATH, '//div[contains(@class, "OrderHistory")]')

    # надпись "Профиль"
    PROFILE_TITLE = (By.XPATH, '//a[text()="Профиль"]')

    # последний, верхний, заказ
    NUMBER_LAST_ORDER = (By.XPATH, '//li[last()]/a[contains(@href, "order-history")]/*/p[1]')
