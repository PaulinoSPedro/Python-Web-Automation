import unittest
from selenium import webdriver
from automations_and_tests.pom_test_orange_crm.Pages.LoginPage import LoginPage
from automations_and_tests.pom_test_orange_crm.Pages.HomePage import HomePage
from automations_and_tests.pom_test_orange_crm.Locators.Locators import HomeLocators

class DashboardTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    # Test clicking all tabs
    def test_01_click_all_tabs(self):
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_locators = HomeLocators

        self.login_page.login()

        self.home_page.click(locator=self.home_locators.admin_li_xpath)
        self.home_page.screenshot(test_folder="dashboard_test", name="admin_page")

        self.home_page.click(locator=self.home_locators.pim_li_xpath)
        self.home_page.screenshot(test_folder="dashboard_test", name="pim_page")

        self.home_page.click(locator=self.home_locators.leave_li_xpath)
        self.home_page.screenshot(test_folder="dashboard_test", name="leave_page")

        self.home_page.click(locator=self.home_locators.time_li_xpath)
        self.home_page.screenshot(test_folder="dashboard_test", name="time_page")

        self.home_page.click(locator=self.home_locators.recruitment_li_xpath)
        self.home_page.screenshot(test_folder="dashboard_test", name="recruitment_page")

        self.home_page.click(locator=self.home_locators.info_li_xpath)
        self.home_page.screenshot(test_folder="dashboard_test", name="info_page")

        self.home_page.click(locator=self.home_locators.performance_li_xpath)
        self.home_page.screenshot(test_folder="dashboard_test", name="performance_page")

        self.home_page.click(locator=self.home_locators.dashboard_li_xpath)
        self.home_page.screenshot(test_folder="dashboard_test", name="dashboard_page")

        self.home_page.click(locator=self.home_locators.directory_li_xpath)
        self.home_page.screenshot(test_folder="dashboard_test", name="directory_page")

        self.home_page.click(locator=self.home_locators.maintenance_li_xpath)
        self.home_page.screenshot(test_folder="dashboard_test", name="maintenance_page")
        self.driver.back()

        self.home_page.click(locator=self.home_locators.claim_li_xpath)
        self.home_page.screenshot(test_folder="dashboard_test", name="claim_page")

        self.home_page.click(locator=self.home_locators.buzz_li_xpath)
        self.home_page.screenshot(test_folder="dashboard_test", name="buzz_page")

    def tearDown(self):
        self.driver.close()

if __name__ == 'main':
    unittest.main()