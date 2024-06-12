import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import *
import allure


class TestScoterPage:
    @allure.title('Выход на домашную страницу')
    @pytest.mark.parametrize('data, num', [(order_data_1, 0)])
    def test_home_page(self, driver, data, num):
        main_page = MainPage(driver)
        main_page_1 = OrderPage(driver)
        main_page.go_to_order_page(num)
        main_page_1.data_input(data, num)
        main_page_1.status()
        assert main_page.scoter() == "https://qa-scooter.praktikum-services.ru/"