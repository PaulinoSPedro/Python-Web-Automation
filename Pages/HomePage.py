import time

from selenium.webdriver.common.by import By
from automations_and_tests.pom_test_orange_crm.Locators import Locators

class HomePage:
    def __init__(self, driver):
        self.driver = driver

        self.profile_ul_class_name = Locators.HomeLocators.profile_ul_classname
        self.profile_li_xpath = Locators.HomeLocators.logout_li_xpath

    def click_profile(self):
        self.driver.find_element(By.CLASS_NAME, self.profile_ul_class_name).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.profile_li_xpath).click()
        time.sleep(1)

