import allure

from pages.account_profile_page import AccountProfilePage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestPersonalAccount:

    @allure.title('Переход на страницу личного кабинета')
    def test_open_personal_account(self, login, driver):
        driver = login
        main_page = MainPage(driver)
        account_profile_page = AccountProfilePage(driver)

        # костыль для прогрузки страницы, без неё не нажимется кнопки (чтобы не использовать sleep)
        main_page.check_display_bun()
        main_page.click_to_key_personal_account()
        assert 'Профиль' in account_profile_page.check_display_profile_data(), 'Не отображаются данные профиля'

    @allure.title('Переход в раздел "История заказов"')
    def test_open_history_order(self, login, driver):
        driver = login
        main_page = MainPage(driver)
        account_profile_page = AccountProfilePage(driver)

        # костыль для прогрузки страницы, без неё не нажимется кнопки (чтобы не использовать sleep)
        main_page.check_display_bun()
        main_page.click_to_key_personal_account()
        account_profile_page.click_to_button_history_order()
        assert account_profile_page.check_display_history_order(), \
            'Не отображается история заказов'

    @allure.title('Выход из аккаунта')
    def test_logout(self, login, driver):
        driver = login
        main_page = MainPage(driver)
        account_profile_page = AccountProfilePage(driver)
        login_page = LoginPage(driver)

        # костыль для прогрузки страницы, без неё не нажимется кнопки (чтобы не использовать sleep)
        main_page.check_display_bun()
        main_page.click_to_key_personal_account()
        account_profile_page.click_to_button_logout()
        assert 'Вход' in login_page.check_display_title_login(), 'Не отображается надпись "Вход"'
