from selenium.webdriver.common.by import By


class OrderPageLocator:
    NAME = By.XPATH, ".//input[@placeholder='* Имя']"
    SURNAME = By.XPATH, ".//input[@placeholder='* Фамилия']"
    ADRESS = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO = By.XPATH, ".//input[@placeholder='* Станция метро']"
    SELECT_METRO = By.XPATH, ".//li[@data-index='{}']"
    TEL = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    DALEE = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    KOGDA = By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"
    SROK = By.XPATH, ".//span[@class='Dropdown-arrow']"
    SROK_1 = By.XPATH, ".//div[@class='Dropdown-option']"
    COLOR = By.XPATH, ".//input[@class='Checkbox_Input__14A2w']"
    KOM = By.XPATH, ".//input[@placeholder='Комментарий для курьера']"
    ORDER = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    YES = By.XPATH, ".//button[(@class='Button_Button__ra12g Button_Middle__1CSJM') and text()='Да']"
    ORDER_IN_PASSED = By.XPATH, ".//div[@class='Order_NextButton__1_rCA']/button[@class='Button_Button__ra12g Button_Middle__1CSJM']"


