import pytest

from selenium import webdriver
from data import Data, ChromeBrowser, FirefoxBrowser, TestAccount
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = ChromeOptions()
        options.add_argument(ChromeBrowser.WINDOW_SIZE)
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = FirefoxOptions()
        options.add_argument(FirefoxBrowser.WIDTH)
        options.add_argument(FirefoxBrowser.HEIGHT)
        driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.get(Data.BASE_URL)
    main_page = MainPage(driver)
    main_page.click_to_button_login()
    login_page = LoginPage(driver)
    login_page.input_email(TestAccount.TEST_MAIL)
    login_page.input_password(TestAccount.TEST_PASSWORD)
    login_page.click_to_button_in()
    return driver
