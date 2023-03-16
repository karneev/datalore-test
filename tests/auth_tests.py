from selenium.webdriver.common.by import By
from config.config import login_cookie_value, login_cookie_name
from entiites.helpers import wait_for_element
from pages.home_page import HomePage
from pages.landing_page import LandingPage
from tests.base_test import BaseTest


class TestMainPage(BaseTest):

    def test_login(self):
        landing_page = LandingPage(self.driver)
        landing_page.open()
        landing_page.set_login()
        landing_page.set_password()
        landing_page.submit()

        home_page = HomePage(self.driver)
        home_page_title = wait_for_element(self, home_page.title_xpath).text
        current_url = self.driver.current_url
        self.assertIn("notebooks", current_url,
                      "Правильный урл страницы")
        self.assertEqual(home_page_title, "Your notebooks",
                         "Корректный тайтл элемента")

    def test_login_by_cookie(self):
        landing_page = LandingPage(self.driver)
        landing_page.open()
        self.driver.add_cookie({"name": login_cookie_name, "value": login_cookie_value})
        self.driver.refresh()

        home_page = HomePage(self.driver)
        home_page_title = wait_for_element(self, home_page.title_xpath).text
        current_url = self.driver.current_url
        self.assertIn("notebooks", current_url,
                      "Правильный урл страницы")
        self.assertEqual(home_page_title, "Your notebooks",
                         "Корректный тайтл элемента")

    def test_create_account(self):
        landing_page = LandingPage(self.driver)
        landing_page.open()

        landing_page.create_account()
        wait_for_element(self, "//*[text()='Sign up']")

        landing_page.set_login("test@test.ru")
        landing_page.set_password("38$9r8fn483ecd")
        landing_page.create_account_submit()
        alert = wait_for_element(self, landing_page.alert_class, By.CLASS_NAME)

        self.assertEqual(alert.text, "New account registrations are disabled.",
                         "Корректная ошибка создания аккаунта")

    def test_forgot_password(self):
        landing_page = LandingPage(self.driver)
        landing_page.open()

        landing_page.set_login("test@test.ru")
        landing_page.forgot_password()

    def test_login_no_password(self):
        pass

    def test_wrong_password(self):
        pass

    def test_no_email_on_forgot(self):
        pass

    def test_password_eye(self):
        pass
