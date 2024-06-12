import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocator


class OrderPage(BasePage):

    @allure.step("Заказ самоката")
    def data_input(self, text, num):
        locator_m_formatted = self.format_lokators(OrderPageLocator.SELECT_METRO, num)
        locator_s_formatted = self.format_lokators(OrderPageLocator.SROK_1, num)
        locator_c_formatted = self.format_lokators(OrderPageLocator.COLOR, num)
        self.clik_to_element(OrderPageLocator.NAME)
        self.add_text_to_element(OrderPageLocator.NAME, text[0])
        self.clik_to_element(OrderPageLocator.SURNAME)
        self.add_text_to_element(OrderPageLocator.SURNAME, text[1])
        self.clik_to_element(OrderPageLocator.ADRESS)
        self.add_text_to_element(OrderPageLocator.ADRESS, text[2])
        self.clik_to_element(OrderPageLocator.METRO)
        self.clik_to_element(locator_m_formatted)
        self.clik_to_element(OrderPageLocator.TEL)
        self.add_text_to_element(OrderPageLocator.TEL, text[3])
        self.clik_to_element(OrderPageLocator.DALEE)
        self.clik_to_element(OrderPageLocator.KOGDA)
        self.add_text_to_element(OrderPageLocator.KOGDA, text[4])
        self.clik_to_element(OrderPageLocator.SROK)
        self.clik_to_element(locator_s_formatted)
        self.clik_to_element(locator_c_formatted)
        self.clik_to_element(OrderPageLocator.KOM)
        self.add_text_to_element(OrderPageLocator.KOM, text[5])
        self.clik_to_element(OrderPageLocator.ORDER)
        self.clik_to_element(OrderPageLocator.YES)
        return self.get_text_fo_element(OrderPageLocator.ORDER_IN_PASSED)

    @allure.step("Переход в статус заказа")
    def status(self):
        self.clik_to_element(OrderPageLocator.ORDER_IN_PASSED)
