import allure

from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):

    @allure.step('Отображение заголовка "Лента заказов"')
    def check_display_title_feed(self):
        return self.get_text_from_element(FeedPageLocators.TITLE_FEED)

    @allure.step('Получить количество выполненных заказов за всё время')
    def get_all_time_orders(self):
        return self.get_text_from_element(FeedPageLocators.ALL_TIME_ORDERS)

    @allure.step('Получить количество выполненных заказов за сегодня')
    def get_today_orders(self):
        return self.get_text_from_element(FeedPageLocators.TODAY_ORDERS)

    @allure.step('Получить детали заказа')
    def get_order_details(self):
        return self.find_element_with_wait(FeedPageLocators.POPUP_ORDER_DETAILS)

    @allure.step('Получить номер заказов в ленте заказов')
    def get_number_order_feed_list(self):
        return self.get_text_from_element(FeedPageLocators.NUMBER_ORDER_FEED_LIST)

    @allure.step('Нажать на последний заказ')
    def click_to_last_order(self):
        return self.click_to_element(FeedPageLocators.LAST_ORDER)

    @allure.step('Получить номер заказа, как он появится в списке')
    def get_updated_order_number_in_list_in_progress(self):
        return self.get_updated_text_from_element(FeedPageLocators.NUMBER_ORDER_IN_PROGRESS)
