from selenium.webdriver.common.by import By


class FeedPageLocators:

    # надпись "Лента заказов"
    TITLE_FEED = (By.XPATH, '//h1[text()="Лента заказов"]')

    # номер заказа в работе
    NUMBER_ORDER_IN_PROGRESS = (By.XPATH, '//ul[contains(@class,"orderListReady")]/li[contains(@class,"mb-2")]')

    # номер заказа в ленте заказов
    NUMBER_ORDER_FEED_LIST = (By.XPATH, '//ul[contains(@class,"OrderFeed_list")]//p[contains(text(),"#")]')

    # счётчик количества выполненных заказов за все время
    ALL_TIME_ORDERS = (By.XPATH,
                       '//p[text()="Выполнено за все время:"]/following-sibling::'
                       'p[contains(@class,"OrderFeed_number")]')

    # счётчик количества выполненных заказов за сегодня
    TODAY_ORDERS = (By.XPATH,
                    '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"OrderFeed_number")]')

    # последний заказ
    LAST_ORDER = (By.XPATH, '//a[contains(@href,"/feed/")][1]')

    # идентификатор активного всплывающего окна деталей заказа
    POPUP_ORDER_DETAILS = (By.XPATH, '//section[contains(@class,"Modal_modal_opened__3ISw4 Modal_modal__P3_V5")]')
