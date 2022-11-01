from selenium.webdriver.common.by import By


class TestAuth:

    link = "http://localhost:8000/"
    name = 'admin'
    password = 'admin'

    LOGIN_LINK = (By.XPATH, "//a[@href='/login/']")
    INPUT_NAME = (By.XPATH, "//input[@name='username']")
    INPUT_PASSWORD = (By.XPATH, "//input[@name='password']")
    BUTTON_ENTER = (By.XPATH, "//button[@class='button']")
    CONTROL_ENTER = (By.XPATH, "//a[text()='admin']")

    def test_authorization(self, browser):
        browser.get(self.link)
        browser.find_element(*self.LOGIN_LINK).click()
        browser.find_element(*self.INPUT_NAME).send_keys(self.name)
        browser.find_element(*self.INPUT_PASSWORD).send_keys(self.password)
        browser.find_element(*self.BUTTON_ENTER).click()

        assert browser.find_element(*self.CONTROL_ENTER), "Account login failed"
