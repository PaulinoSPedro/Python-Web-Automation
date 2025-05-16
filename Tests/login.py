import unittest
from selenium import webdriver

from automations_and_tests.pom_test_orange_crm.Pages.HomePage import HomePage
from automations_and_tests.pom_test_orange_crm.Pages.LoginPage import LoginPage


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_01_valid_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php")
        login = LoginPage(driver)
        home = HomePage(driver)
        driver.current_url()
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        home.click_profile()
        home.click_logout()

    def test_02_invalid_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php")
        login = LoginPage(driver)
        home = HomePage(driver)

        login.enter_username("Admin123")
        login.enter_password("admin1234!")

        login.click_login()

        self.assertFalse(home.wait_home_page(), "Invalid login should return FALSE but returned TRUE")



    def tearDown(self):
        self.driver.close()

if __name__ == 'main':
    unittest.main()