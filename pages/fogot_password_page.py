import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators, ResetPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step('Отображение надписи "Восстановление пароля"')
    def check_display_title_recover_password(self):
        return self.get_text_from_element(ForgotPasswordPageLocators.TITLE_RECOVER_PASSWORD)

    @allure.step('Ввести email')
    def input_email(self, email):
        self.add_text_to_element(ForgotPasswordPageLocators.FIELD_EMAIL, email)

    @allure.step('Нажать на кнопку "Восстановить"')
    def click_to_button_recover(self):
        self.click_to_element(ForgotPasswordPageLocators.BUTTON_RECOVER)

    @allure.step('Проверить, что есть поле "Ввести код из письма"')
    def check_field_enter_code_from_email(self):
        return self.get_text_from_element(ResetPasswordPageLocators.FIELD_ENTER_CODE_FROM_EMAIL)

    @allure.step('Нажать на кнопку отображения пароля')
    def click_to_button_show_password(self):
        self.click_to_element(ResetPasswordPageLocators.BUTTON_SHOW_PASSWORD)

    @allure.step('Проверить, что поле "Пароль" активно')
    def is_password_field_active(self):
        return self.is_visible(ResetPasswordPageLocators.ACTIVE_PASSWORD_FIELD)
