import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Отображение надписи "Вход"')
    def check_display_title_login(self):
        return self.get_text_from_element(LoginPageLocators.LABEL_LOGIN)

    @allure.step('Ввести email')
    def input_email(self, email):
        self.add_text_to_element(LoginPageLocators.INPUT_EMAIL, email)

    @allure.step('Ввести пароль')
    def input_password(self, password):
        self.add_text_to_element(LoginPageLocators.INPUT_PASSWORD, password)

    @allure.step('Нажать на кнопку "Войти"')
    def click_to_button_in(self):
        self.click_to_element(LoginPageLocators.BUTTON_IN)

    @allure.step('Нажать на кнопку "Восстановить пароль"')
    def click_to_button_recover_password(self):
        self.click_to_element(LoginPageLocators.KEY_RECOVER_PASSWORD)
