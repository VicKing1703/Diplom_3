import allure

from locators.account_profile_page_locators import AccountProfilePageLocators as AccProfLocators
from pages.base_page import BasePage


class AccountProfilePage(BasePage):

    @allure.step('Отображение данных профиля')
    def check_display_profile_data(self):
        return self.get_text_from_element(AccProfLocators.PROFILE_TITLE)

    @allure.step('Нажать на кнопку "Выход"')
    def click_to_button_logout(self):
        self.click_to_element(AccProfLocators.KEY_LOGOUT)

    @allure.step('Нажать на кнопку "История заказов"')
    def click_to_button_history_order(self):
        self.click_to_element(AccProfLocators.KEY_HISTORY_ORDER)

    @allure.step('Отображение истории заказов')
    def check_display_history_order(self):
        return self.find_element_with_wait(AccProfLocators.LIST_ACC_ORDER_HISTORY)

    @allure.step('Получить номер последнего заказа')
    def get_number_last_order(self):
        return self.get_text_from_element(AccProfLocators.NUMBER_LAST_ORDER)
