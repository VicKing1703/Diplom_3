import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Нажать на кнопку "Личный кабинет"')
    def click_to_key_personal_account(self):
        self.click_to_element(MainPageLocators.KEY_PERSONAL_ACCOUNT)

    @allure.step('Отображается ингридиент "Булка"')
    def check_display_bun(self):
        return self.is_visible(MainPageLocators.BUN_LIST_HEADER)

    @allure.step('Нажать на кнопку "Конструктор"')
    def click_to_key_constructor(self):
        self.click_to_element(MainPageLocators.KEY_CONSTRUCTOR)

    @allure.step('Отображение заголовка "Соберите бургер"')
    def check_display_title_burger(self):
        return self.get_text_from_element(MainPageLocators.LABEL_CREATE_BURGER)

    @allure.step('Нажать на кнопку "Войти в аккаунт"')
    def click_to_button_login(self):
        self.click_to_element(MainPageLocators.BUTTON_LOGIN)

    @allure.step('Нажать на кнопку "Оформить заказ"')
    def click_to_button_order(self):
        self.click_to_element(MainPageLocators.BUTTON_ORDER)

    @allure.step('Нажать на кнопку "Лента заказов"')
    def click_to_button_order_history(self):
        self.click_to_element(MainPageLocators.KEY_ORDER_HISTORY)

    @allure.step('Нажать на  ингредиент "Флюоресцентная булка R2-D3"')
    def click_to_ingredient_fluorescent_bun(self):
        self.click_to_element(MainPageLocators.FLUORESCENT_BUN)

    @allure.step('Показать счётчик ингредиента из булок')
    def get_count_ingredient(self):
        return self.get_text_from_element(MainPageLocators.COUNTER_OF_FLUORESCENT_BUN)

    @allure.step('Отображение заголовка всплывающего окна "Детали ингредиента"')
    def check_display_title_ingredient_details(self):
        return self.get_text_from_element(MainPageLocators.LABEL_INGREDIENTS_DETAILS)

    @allure.step('Закрыть всплывающее окно "Детали ингредиента"')
    def close_ingredient_details_popup(self):
        self.click_to_element(MainPageLocators.BUTTON_CLOSE_INGREDIENT_DETAILS)

    @allure.step('Окно деталей ингредиента не отображается')
    def check_display_ingredient_details_popup(self):
        return self.is_visible(MainPageLocators.POPUP_IDENTIFER)

    @allure.step('Перетаскивание ингредиента в правую часть экрана')
    def drag_and_drop_fluorescent_bun_in_basket(self):
        self.driver.implicitly_wait(3)  # неявное ожидание(костыль)
        self.drag_and_drop(MainPageLocators.FLUORESCENT_BUN,
                           MainPageLocators.BURGER_CONSTRUCTOR_BASKET)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        return self.get_updated_text_from_element(MainPageLocators.ORDER_NUMBER, 3)

    # Не превратил в статичный метод как будто это реальный проект и кнопка может понадобится для других тестов :)
    @allure.step('Закрыть всплывающее окно с номером заказа')
    def close_order_number_popup(self):
        self.click_to_element(MainPageLocators.BUTTON_CLOSE_ORDER_COUNTER)

    @allure.step('Создание заказа')
    def create_order(self):
        self.drag_and_drop_fluorescent_bun_in_basket()
        self.click_to_button_order()
        order_number = self.get_order_number()
        self.close_order_number_popup()
        return order_number
