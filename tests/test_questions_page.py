import pytest

from pages.main_page import MainPage
from data import *
import allure

class TestMainPage:

    @allure.title('Открытие вопросов')
    @pytest.mark.parametrize('num, result', [(0, helpers[0]), (1, helpers[1]), (2, helpers[2]), (3, helpers[3]), (4, helpers[4]), (5, helpers[5]), (6, helpers[6]), (7, helpers[7])])
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        assert main_page.get_answer_text(num) == result