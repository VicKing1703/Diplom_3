import allure

from data import Data, TestAccount
from pages.login_page import LoginPage
from pages.fogot_password_page import ForgotPasswordPage


class TestRecoveryPassword:

    @allure.title('Переход на страницу восстановления пароля')
    @allure.description('Проверка при переходе на страницу восстановления пароля, '
                        'отображения заголовок "Восстановление пароля"')
    def test_recovery_password_title(self, driver):
        driver.get(Data.LOGIN_URL)
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        login_page.click_to_button_recover_password()
        assert 'Восстановление пароля' in forgot_password_page.check_display_title_recover_password(), \
            'Не отображается надпись "Восстановление пароля"'

    @allure.title('Ввод email и кликнуть на кнопку "Восстановить"')
    @allure.description('Проверка ввода email, нажатия на кнопку "Восстановить" '
                        'для перехода на страницу восстановления пароля')
    def test_add_email_and_click_to_button_recover(self, driver):
        driver.get(Data.FORGOT_PASSWORD_URL)
        forgot_password_page = ForgotPasswordPage(driver)

        forgot_password_page.input_email(TestAccount.TEST_MAIL)
        forgot_password_page.click_to_button_recover()
        assert forgot_password_page.check_field_enter_code_from_email() == 'Введите код из письма', \
            'Нет поля или плейсхолдера "Ввести код из письма"'

    @allure.title('Нажать на кнопку "Отображать пароль" делает поле активным')
    @allure.description('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_to_button_show_password(self, driver):
        driver.get(Data.FORGOT_PASSWORD_URL)
        forgot_password_page = ForgotPasswordPage(driver)

        forgot_password_page.input_email(TestAccount.TEST_MAIL)
        forgot_password_page.click_to_button_recover()
        forgot_password_page.click_to_button_show_password()
        assert forgot_password_page.is_password_field_active(), 'Поле "Пароль" не подсвечивается'
