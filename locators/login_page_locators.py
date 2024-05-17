from selenium.webdriver.common.by import By


class LoginPageLocators:

    # поле "Email" на экране логина
    INPUT_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input[@type="text"]')

    # поле "Пароль" на экранах логина
    INPUT_PASSWORD = (By.NAME, "Пароль")

    # кнопка "Войти" на эжкране логина
    BUTTON_IN = (By.XPATH, '//button[text()="Войти"]')

    # кнопка "Зарегестрироваться" на экране входа
    KEY_REGISTRATION = (By.XPATH, '//*[@href="/register"]')

    # кнопка "Восстановить пароль" на экране логина
    KEY_RECOVER_PASSWORD = (By.XPATH, '//*[@href="/forgot-password"]')

    # надпись "Вход" на экране логина
    LABEL_LOGIN = (By.XPATH, '//h2[contains(text(),"Вход")]')
