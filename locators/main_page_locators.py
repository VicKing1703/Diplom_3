from selenium.webdriver.common.by import By


class MainPageLocators:

    # **Хедер**
    # кнопка "Личный кабинет" в хедере
    KEY_PERSONAL_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')

    # кнопка "Конструктор" в хедере
    KEY_CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]')

    # кнопка "Лента Заказов" в хедере
    KEY_ORDER_HISTORY = (By.XPATH, '//p[text()="Лента Заказов"]')

    # Кнопки на главной странице
    # кнопка "Войти в аккаунт" на главной странице
    BUTTON_LOGIN = (By.XPATH, '//button[text()="Войти в аккаунт"]')

    # кнопка "Оформить заказ" на главной странице
    BUTTON_ORDER = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')

    # заголовок "Булки" в списке булок
    BUN_LIST_HEADER = (By.XPATH, '//h2[contains(text(),"Булки")]')

    # список булок (не знаю как обойтись тут без индекса)
    FLUORESCENT_BUN = (By.XPATH, '//ul[@class="BurgerIngredients_ingredients__list__2A-mT"][1]/child::a[1]')

    # надпись "Соберите бургер"
    LABEL_CREATE_BURGER = (By.XPATH, '//h1[contains(text(),"Соберите бургер")]')

    # "Корзина" заказа
    BURGER_CONSTRUCTOR_BASKET = (By.XPATH, '//section[@class="BurgerConstructor_basket__29Cd7 mt-25 "]')

    # счётчик ингридиента "Флюоресцентная булка R2-D3"
    COUNTER_OF_FLUORESCENT_BUN = (By.XPATH, '//ul[@class="BurgerIngredients_ingredients__list__2A-mT"][1]/child::'
                                            'a[1]//p[@class="counter_counter__num__3nue1"]')

    # **Всплывающее окно "Детали ингредиента"**
    # надпись "Детали ингредиента" во свплывающем окне
    LABEL_INGREDIENTS_DETAILS = (By.XPATH, '//h2[text()="Детали ингредиента"]')

    # кнопка "Закрыть" во свплывающем окне
    BUTTON_CLOSE_INGREDIENT_DETAILS = (By.XPATH, '//div[contains(@class, "pt-10")]/following::button[@type="button"]')

    # **Всплывающее окно "Идентификатор заказа"**
    # номер заказа во свплывающем окне
    ORDER_NUMBER = (By.XPATH, '//div[contains(@class, "pt-30")]/child::h2')

    # кнопка "Закрыть" во свплывающем окне
    BUTTON_CLOSE_ORDER_COUNTER = (By.XPATH, '//div[contains(@class, "pt-30")]//following::button[@type="button"]')

    # идентификатор активного всплывающего окна
    POPUP_IDENTIFIER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened__3ISw4 Modal_modal__P3_V5")]')
