from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # Метод для ожидания появления элемента
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    # Метод для нажатия на элемент
    def click_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        ActionChains(self.driver).click(element).perform()

    # Метод для ввода текста
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    # Метод для получения текста
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    # Метод для получения обновлённого текста (для полей с обновляемыми значениями)
    def get_updated_text_from_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)

        # Ожидаем, пока элемент не станет видимым
        element = wait.until(EC.visibility_of_element_located(locator))

        try:
            # Получаем текст элемента перед ожиданием
            current_text = element.text

            # Ожидаем изменения текста элемента
            wait.until(lambda driver: element.text != current_text)
        except TimeoutException:
            pass  # Просто проигнорируем TimeoutException и вернем текущий текст

        # Получаем и возвращаем обновленный текст элемента
        updated_text = element.text
        return updated_text

    # Метод перетаскивания элемента
    # данный метод не работает в Firefox. Причину понять не смог, убил на это очень много времени...
    def drag_and_drop(self, source_locator, target_locator):
        source_element = self.find_element_with_wait(source_locator)
        target_element = self.find_element_with_wait(target_locator)

        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_element)
        action.perform()

    # Метод для проверки видимости элемента
    def is_visible(self, locator):
        result = True
        try:
            WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            result = False
        return result
