from selenium.webdriver.common.by import By


class MainPageLocators:

    # Хедер
    KEY_PERSONAL_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')  # кнопка "Личный кабинет" в хедере
    KEY_CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]')  # кнопка "Конструктор" в хедере
    KEY_LOGO = (By.CSS_SELECTOR, '.AppHeader_header__logo__2D0X2')  # центральная кнопка "Stellar Burgers" в хедере
    KEY_ORDER_HISTORY = (By.XPATH, '//p[text()="Лента Заказов"]')  # кнопка "Лента Заказов" в хедере

    # Кнопки на главной странице
    BUTTON_LOGIN = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # кнопка "Войти в аккаунт" на главной странице
    BUTTON_ORDER = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')  # кнопка "Оформить заказ" на главной странице
    BUN_LIST_HEADER = (By.XPATH, '//h2[contains(text(),"Булки")]')  # заголовок "Булки" в списке булок
    FLUORESCENT_BUN = (By.XPATH, '//ul[@class="BurgerIngredients_ingredients__list__2A-mT"][1]/child::a[1]')  # список булок (не знаю как обойтись тут без индекса)
    LABEL_CREATE_BURGER = (By.XPATH, '//h1[contains(text(),"Соберите бургер")]')  # надпись "Соберите бургер"
    BURGER_CONSTRUCTOR_BASKET = (By.XPATH, '//section[@class="BurgerConstructor_basket__29Cd7 mt-25 "]')  # "Корзина" заказа
    COUNTER_OF_FLUORESCENT_BUN = (By.XPATH, '//ul[@class="BurgerIngredients_ingredients__list__2A-mT"][1]/child::'
                                            'a[1]//p[@class="counter_counter__num__3nue1"]')  # счётчик ингридиента "Флюоресцентная булка R2-D3"

    # Всплывающее окно "Детали ингредиента"
    LABEL_INGREDIENTS_DETAILS = (By.XPATH, '//h2[text()="Детали ингредиента"]')  # надпись "Детали ингредиента" во свплывающем окне
    BUTTON_CLOSE_INGREDIENT_DETAILS = (By.XPATH, '//div[contains(@class, "pt-10")]/following::button[@type="button"]')  # кнопка "Закрыть" во свплывающем окне

    # Всплывающее окно "Идентификатор заказа"
    ORDER_NUMBER = (By.XPATH, '//div[contains(@class, "pt-30")]/child::h2')  # номер заказа во свплывающем окне
    BUTTON_CLOSE_ORDER_COUNTER = (By.XPATH, '//div[contains(@class, "pt-30")]//following::button[@type="button"]')  # кнопка "Закрыть" во свплывающем окне

    POPUP_IDENTIFER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened__3ISw4 Modal_modal__P3_V5")]')  # идентификатор активного всплывающего окна

