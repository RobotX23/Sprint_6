from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def clik_to_element(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_key(text)

    def get_text_fo_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_lokators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)