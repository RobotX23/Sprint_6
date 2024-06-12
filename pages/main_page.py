import time

import allure


from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocator


class MainPage(BasePage):

    @allure.step("Получение текста ответа")
    def get_answer_text(self, num):
        locator_q_formatted = self.format_lokators(MainPageLocator.QUESTION, num)
        locator_a_formatted = self.format_lokators(MainPageLocator.ANSWER, num)
        self.scroll_to_element(locator_q_formatted)
        self.clik_to_element(locator_q_formatted)
        return self.get_text_fo_element(locator_a_formatted)

    @allure.step("Переход к странице заказа")
    def go_to_order_page(self, num):
        if num == 0:
            self.scroll_to_element(MainPageLocator.ORDER_1)
            self.clik_to_element(MainPageLocator.ORDER_1)
        else:
            self.scroll_to_element(MainPageLocator.ORDER_2)
            self.clik_to_element(MainPageLocator.ORDER_2)

    @allure.step("Переход на главную страницу")
    def scoter(self):
        self.clik_to_element(MainPageLocator.SCOTER)
        return self.url()

    @allure.step("Переход на страницу Яндекса")
    def yandex(self):
        self.clik_to_element(MainPageLocator.YANDEX)
        self.window()
        time.sleep(10)
        return self.url()