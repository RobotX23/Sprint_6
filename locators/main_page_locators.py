from selenium.webdriver.common.by import By

class MainPageLocator:
    QUESTION = By.XPATH, ".//div[@id='accordion__heading-{}']"
    ANSWER = By.XPATH, ".//div[@id='accordion__panel-{}']"
    ORDER_1 = By.XPATH, ".//button[@class='Button_Button__ra12g']"
    ORDER_2 = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    SCOTER = By.XPATH, ".//img[@alt='Scooter']"
    YANDEX = By.XPATH, ".//img[@alt='Yandex']"
    DZEN = By.XPATH, ".//a[@title='Установить']"