import allure

from data import Data
from pages.account_profile_page import AccountProfilePage
from pages.feed_page import FeedPage
from pages.main_page import MainPage


class TestOrderFeed:

    @allure.title('При клике на заказ, открывается всплывающее окно с деталями')
    def test_open_order_details_popup(self, driver):
        driver.get(Data.FEED_URL)
        feed_page = FeedPage(driver)

        feed_page.click_to_last_order()
        assert feed_page.get_order_details(), 'Не открылось всплывающее окно с деталями заказа'

    # Проаерка всех заказов пользователя не целесообразна, т.к. страница заказов показывает только 50 последних заказов,
    # а у тестового пользователя несколько заказов может быть сделано давно и тест заведомо провалится.
    # В данном случае создадим заказ, возмём его номер из личного кабинета и проверим его присутствие в ленте заказов.
    # Но в случае с firefox, где не работает drag_and_drop, может отработать
    @allure.title('Заказы пользователя из раздела "История заказов" отображаются на странице "Лента заказов"')
    def test_in_order_history_have_order_user(self, login, driver):
        driver = login
        main_page = MainPage(driver)
        account_profile_page = AccountProfilePage(driver)
        feed_page = FeedPage(driver)

        # костыль для прогрузки страницы, без неё не нажимется кнопки (чтобы не использовать sleep)
        main_page.check_display_bun()
        main_page.create_order()
        main_page.click_to_key_personal_account()
        account_profile_page.click_to_button_history_order()
        number_last_order = account_profile_page.get_number_last_order()
        main_page.click_to_button_order_history()

        assert number_last_order in feed_page.get_number_order_feed_list(), 'Заказа нет в ленте заказов'

    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_increase_counter_order_for_all_time(self, login, driver):
        driver = login
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        # костыль для прогрузки страницы, без неё не нажимется кнопки (чтобы не использовать sleep)
        main_page.check_display_bun()
        main_page.click_to_button_order_history()
        counter_order_all_time = feed_page.get_all_time_orders()
        main_page.click_to_key_constructor()
        main_page.create_order()
        main_page.click_to_button_order_history()
        counter_order_all_time_new = feed_page.get_all_time_orders()
        assert counter_order_all_time_new > counter_order_all_time, 'Счётчик "Выполнено за всё время" не увеличился'

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_increase_counter_order_for_today(self, login, driver):
        driver = login
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        # костыль для прогрузки страницы, без неё не нажимется кнопки (чтобы не использовать sleep)
        main_page.check_display_bun()
        main_page.click_to_button_order_history()
        counter_order_today = feed_page.get_today_orders()
        main_page.click_to_key_constructor()
        main_page.create_order()
        main_page.click_to_button_order_history()
        counter_order_today_new = feed_page.get_today_orders()
        assert counter_order_today_new > counter_order_today, 'Счётчик "Выполнено за сегодня" не увеличился'

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_order_number_appears_in_work(self, login, driver):
        driver = login
        feed_page = FeedPage(driver)
        main_page = MainPage(driver)

        # костыль для прогрузки страницы, без неё не нажимется кнопки (чтобы не использовать sleep)
        main_page.check_display_bun()
        number_order = main_page.create_order()
        main_page.click_to_button_order_history()
        numbers_order_in_progress = feed_page.get_updated_order_number_in_list_in_progress()
        assert number_order in numbers_order_in_progress, \
            'Номер заказа не появился в разделе "В работе"'
