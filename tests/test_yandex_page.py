from pages.main_page import MainPage
import allure

class TestYandexPage:

    @allure.title('Переход на страницу Яндекса')
    def test_yandex(self, driver):
        main_page = MainPage(driver)
        assert main_page.yandex() == 'https://dzen.ru/?yredirect=true'