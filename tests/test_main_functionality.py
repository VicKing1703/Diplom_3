import allure

from data import Data
from pages.feed_page import FeedPage
from pages.main_page import MainPage


class TestMainFunctionality:

    @allure.title('Переход по клику на "Конструктор"')
    @allure.description('Проверка перехода на главный экран по клику на "Конструктор" с экрана логина')
    def test_open_constructor(self, driver):
        driver.get(Data.LOGIN_URL)
        main_page = MainPage(driver)
        main_page.click_to_key_constructor()
        assert "Соберите бургер" in main_page.check_display_title_burger(), 'На странице нет надписи "Соберите бургер"'

    @allure.title('Переход по клику на "Лента заказов"')
    @allure.description('Проверка перехода в ленту заказов по клику на "Лента заказов" с главного экрана')
    def test_open_order_history(self, driver):
        driver.get(Data.BASE_URL)
        main_page = MainPage(driver)
        main_page.click_to_button_order_history()
        feed_page = FeedPage(driver)
        assert "Лента заказов" in feed_page.check_display_title_feed(), 'На странице нет надписи "Лента заказов"'

    @allure.title('При нажатии на ингридиент, появляется всплывающее окно с деталями')
    def test_open_ingredient_details_popup(self, driver):
        driver.get(Data.BASE_URL)
        main_page = MainPage(driver)
        main_page.click_to_ingredient_fluorescent_bun()
        assert "Детали ингредиента" in main_page.check_display_title_ingredient_details(), \
            'Не открылось всплывающее окно с деталями ингредиента или в окне нет заголовка "Детали ингредиента"'

    @allure.title('Закрыть всплывающее окно с деталями ингредиента')
    def test_close_ingredient_details_popup(self, driver):
        driver.get(Data.BASE_URL)
        main_page = MainPage(driver)
        main_page.click_to_ingredient_fluorescent_bun()
        main_page.close_ingredient_details_popup()
        assert main_page.check_display_ingredient_details_popup() is False, \
            'Не закрылось всплывающее окно с деталями ингредиента'

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    @allure.description('При добавлении флюоресцентной булки в заказ счётчик этого ингредиента увеличивается на 2')
    def test_increase_counter_ingredient_after_add_fluorescent_bun_in_basket(self, driver):
        driver.get(Data.BASE_URL)
        main_page = MainPage(driver)
        main_page.drag_and_drop_fluorescent_bun_in_basket()
        assert main_page.get_count_ingredient() == '2', 'Счётчик ингредиента не увеличился'

    @allure.title('Залогиненый пользоватедль может оформить заказ')
    def test_login_user_can_order(self, login, driver):
        driver = login
        main_page = MainPage(driver)
        main_page.drag_and_drop_fluorescent_bun_in_basket()
        main_page.click_to_button_order()
        assert main_page.get_order_number() != '9999', 'Окно с номером заказа не открылось или номер заказа равен 9999'
