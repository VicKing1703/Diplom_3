from selenium.webdriver.common.by import By


class LoginPageLocators:

    INPUT_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input[@type="text"]')  # поле "Email" на экране логина
    INPUT_PASSWORD = (By.NAME, "Пароль")  # поле "Пароль" на экранах логина
    BUTTON_IN = (By.XPATH, '//button[text()="Войти"]')  # кнопка "Войти" на эжкране логина
    KEY_REGISTRATION = (By.XPATH, '//*[@href="/register"]')  # кнопка "Зарегестрироваться" на экране входа
    KEY_RECOVER_PASSWORD = (By.XPATH, '//*[@href="/forgot-password"]')  # кнопка "Восстановить пароль" на экране логина
    LABLE_LOGIN = (By.XPATH, '//h2[contains(text(),"Вход")]')  # надпись "Вход" на экране логина
