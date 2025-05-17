import unittest
from selenium import webdriver
from automations_and_tests.pom_test_orange_crm.Pages.LoginPage import LoginPage

class DashboardTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    # Test clicking all tabs
    def test_01_click_all_tabs(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login()


    def tearDown(self):
        self.driver.close()

if __name__ == 'main':
    unittest.main()