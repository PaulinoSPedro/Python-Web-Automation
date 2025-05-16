from selenium.webdriver.common.by import By
from automations_and_tests.pom_test_orange_crm.Locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.username_input_name = Locators.LoginLocators.username_input_name
        self.password_input_name = Locators.LoginLocators.password_input_name
        self.login_button_xpath  = Locators.LoginLocators.login_button_xpath


    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.username_input_name).clear()
        self.driver.find_element(By.NAME, self.username_input_name).send_keys(username)


    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_input_name).clear()
        self.driver.find_element(By.NAME, self.password_input_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
