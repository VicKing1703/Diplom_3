from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

    # надпись "Восстановление пароля"
    TITLE_RECOVER_PASSWORD = (By.XPATH, '//h2[text()="Восстановление пароля"]')

    # поле "Email"
    FIELD_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')

    # кнопка "Восстановить" на экране восстановления пароля
    BUTTON_RECOVER = (By.XPATH, '//button[text()="Восстановить"]')


class ResetPasswordPageLocators:

    # поле "Ввести код из письма"
    FIELD_ENTER_CODE_FROM_EMAIL = (By.XPATH, '//label[text()="Введите код из письма"]')

    # кнопка "Показать пароль"
    BUTTON_SHOW_PASSWORD = (By.CSS_SELECTOR, '.input__icon-action > svg')

    # поле "Пароль" активное состояние
    ACTIVE_PASSWORD_FIELD = (By.XPATH, '//label[contains(@class,"input__placeholder-focused")]')
