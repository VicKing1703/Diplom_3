from selenium.webdriver.common.by import By


class AccountProfilePageLocators:

    KEY_LOGOUT = (By.XPATH, '//button[text()="Выход"]')  # кнопка "Выйти"
    KEY_HISTORY_ORDER = (By.XPATH, '//a[text()="История заказов"]')  # кнопка "История заказов"
    LIST_ACC_ORDER_HISTORY = (By.XPATH, '//div[contains(@class, "OrderHistory")]')  # список истории заказов
    FIELD_ACC_PROFILE = (By.XPATH, '//ul[contains(@class, "Profile")]')  # поля с данными профиля
    PROFILE_TITLE = (By.XPATH, '//a[text()="Профиль"]')  # надпись "Профиль"
    NUMBER_LAST_ORDER = (By.XPATH, '//li[last()]/a[contains(@href, "order-history")]/*/p[1]')  # последний, верхний, заказ
