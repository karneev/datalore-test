from time import sleep

from selenium.webdriver.common.by import By
from config.config import login_cookie_value, login_cookie_name
from entities.helpers import wait_for_element, gen_email, gen_password, gen_weak_password
from pages.home_page import HomePage
from pages.landing_page import LandingPage
from entities.base_test import BaseTest
from pages.loading_page import LoadingPage


class TestMainPage(BaseTest):

    def test_login(self):
        landing_page = LandingPage(self.driver)
        landing_page.open()
        landing_page.set_login()
        landing_page.set_password()
        landing_page.submit()

        # Эта проверка на CI может быть хрупкой, если страница быстро прогрузится
        loading_page = LoadingPage(self.driver)
        wait_for_element(self, loading_page.title_class, By.CLASS_NAME).text
        self.assertTrue(loading_page.logo(),
                        "Есть лого на странице загрузки")

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

        landing_page.set_login(gen_email())
        landing_page.set_password(gen_password())
        landing_page.create_account_submit()
        alert = wait_for_element(self, landing_page.alert_class, By.CLASS_NAME)

        self.assertEqual(alert.text, "New account registrations are disabled.",
                         "Корректная ошибка создания аккаунта")

    def test_forgot_password(self):
        landing_page = LandingPage(self.driver)
        landing_page.open()
        email = gen_email()
        landing_page.set_login(email)
        landing_page.forgot_password()

        restore_pass_instructions = wait_for_element(self, landing_page.instructions_xpath).text

        self.assertIn(email, restore_pass_instructions,
                      "Корректно указан email")

    def test_login_no_password(self):
        landing_page = LandingPage(self.driver)
        landing_page.open()
        email = gen_email()
        landing_page.set_login(email)
        landing_page.submit()

        alert = wait_for_element(self, landing_page.password_is_required_alert_xpath)

        self.assertEqual(alert.text, "Password is required",
                         "Ошибка при отсутствии пароля")

    def test_wrong_password(self):
        landing_page = LandingPage(self.driver)
        landing_page.open()
        landing_page.set_login(gen_email())
        landing_page.set_password(gen_password())
        landing_page.submit()
        alert = wait_for_element(self, landing_page.alert_class, By.CLASS_NAME)

        self.assertEqual(alert.text, "One or both of your email/password was incorrect",
                         "Корректная ошибка авторизации")

    def test_no_email_on_forgot(self):
        landing_page = LandingPage(self.driver)
        landing_page.open()
        landing_page.forgot_password()
        alert = wait_for_element(self, landing_page.email_is_required_alert_xpath)

        self.assertEqual(alert.text, "Email is required",
                         "Ошибка при отсутствии email")

    def test_no_data_on_login(self):
        landing_page = LandingPage(self.driver)
        landing_page.open()
        landing_page.submit()
        alert_email = wait_for_element(self, landing_page.email_is_required_alert_xpath)
        alert_password = wait_for_element(self, landing_page.password_is_required_alert_xpath)

        self.assertEqual(alert_email.text, "Email is required",
                         "Ошибка при отсутствии email")

        self.assertEqual(alert_password.text, "Password is required",
                         "Ошибка при отсутствии пароля")

    def test_test_weak_password(self):
        landing_page = LandingPage(self.driver)
        landing_page.open()
        landing_page.create_account()
        landing_page.set_login(gen_email())
        landing_page.set_password(gen_weak_password())
        landing_page.create_account_submit()

        alert = wait_for_element(self, landing_page.weak_password_xpath)
        self.assertEqual(alert.text, "Password strength: Very weak -",
                         "Ошибка слабого пароля")