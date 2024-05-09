from selenium.webdriver.common.by import By
from data import TestAccount


class FeedPageLocators:

    TITLE_FEED = (By.XPATH, '//h1[text()="Лента заказов"]')  # надпись "Лента заказов"
    # NUMBER_ORDER_IN_PROGRESS = (By.XPATH,
    #                             f"//ul[contains(@class, 'orderListReady__1YFem')]/li[contains(@class,'text') and "
    #                             f"contains(text(), '{TestAccount.TEST_NUMBER_ORDER}')]")  # номер заказа в работе по номеру созданного заказа
    NUMBER_ORDER_IN_PROGRESS = (By.XPATH, '//ul[contains(@class,"orderListReady")]/li[contains(@class,"mb-2")]')  # номер заказа в работе
    NUMBER_ORDER_FEED_LIST = (By.XPATH, '//ul[contains(@class,"OrderFeed_list")]//p[contains(text(),"#")]')  # номер заказа в ленте заказов
    ALL_TIME_ORDERS = (By.XPATH,
                       '//p[text()="Выполнено за все время:"]/following-sibling::'
                       'p[contains(@class,"OrderFeed_number")]')  # счётчик количества выполненных заказов за все время
    TODAY_ORDERS = (By.XPATH,
                    '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"OrderFeed_number")]')  # счётчик количества выполненных заказов за сегодня
    ORDER_DETAILS = (By.XPATH, '//section[contains(@class,"modal_opened")]/div/div')  # детали заказа
    LAST_ORDER = (By.XPATH, '//a[contains(@href,"/feed/")][1]')  # последний заказ
    POPUP_ORDER_DETAILS = (By.XPATH, '//section[contains(@class,"Modal_modal_opened__3ISw4 Modal_modal__P3_V5")]')  # идентификатор активного всплывающего окна деталей заказа
