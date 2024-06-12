import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import *
import allure


class TestOrderPage:

    @allure.title('Оформление заказа')
    @pytest.mark.parametrize('data, num', [(order_data_1, 0),(order_data, 1)])
    def test_order(self, driver,data, num):
        main_page = MainPage(driver)
        main_page_1 = OrderPage(driver)
        main_page.go_to_order_page(num)
        assert main_page_1.data_input(data, num) == 'Посмотреть статус'

