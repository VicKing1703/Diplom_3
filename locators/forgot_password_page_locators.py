from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

    TITLE_RECOVER_PASSWORD = (By.XPATH, '//h2[text()="Восстановление пароля"]')  # надпись "Восстановление пароля"
    FIELD_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # поле "Email"
    BUTTON_RECOVER = (By.XPATH, '//button[text()="Восстановить"]')  # кнопка "Восстановить" на экране восстановления пароля
    KEY_INSERT_REC = (By.XPATH, '//a[@href="/login"]')  # кнопка "Войти" на экране восстановления пароля (одинаковый локатор в паролем на экране входа и восстановления пароля, но вынес отдельно)


class ResetPasswordPageLocators:

    FIELD_ENTER_CODE_FROM_EMAIL = (By.XPATH, '//label[text()="Введите код из письма"]')  # плейсхолдер поля "Ввести код из письма"
    BUTTON_SHOW_PASSWORD = (By.CSS_SELECTOR, '.input__icon-action > svg')  # кнопка "Показать пароль"
    ACTIVE_PASSWORD_FIELD = (By.XPATH, '//label[contains(@class,"input__placeholder-focused")]')  # поле "Пароль" активное состояние
