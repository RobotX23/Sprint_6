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
