from selenium.webdriver.common.by import By

from config.config import url, user_login, user_password
from entiites.base_page import BasePage
from entiites.helpers import wait_for_element


class LandingPage(BasePage):
    email_input = (By.XPATH, "//input[@placeholder='Email']")
    password_input = (By.XPATH, "//input[@placeholder='Password']")
    submit_button = (By.XPATH, "//*[text()='Log in']")
    forgot_password_button = (By.XPATH, "//*[text()='Forgot your password?']")
    create_account_button = (By.XPATH, "//*[text()='Create an account']")
    create_account_confirm = (By.XPATH, "//*[text()='Create account']")
    sign_up_label = (By.XPATH, "Sign up")
    alert_message = (By.CLASS_NAME, "alert_message-error")
    support_text = "//*[text()='Get support']"
    alert_class = "alert_message-error"


    def set_login(self, login=user_login):
        email = self.driver.find_element(*self.email_input)
        email.send_keys(login)

    def set_password(self, password_text=user_password):
        password_elem = self.driver.find_element(*self.password_input)
        password_elem.send_keys(password_text)

    def open(self):
        self.driver.get(url)
        wait_for_element(self, self.support_text)

    def submit(self):
        button = self.driver.find_elements(*self.submit_button)[1]
        button.click()

    def forgot_password(self):
        button = self.driver.find_element(*self.forgot_password_button)
        button.click()

    def create_account(self):
        button = self.driver.find_element(*self.create_account_button)
        button.click()

    def create_account_submit(self):
        button = self.driver.find_element(*self.create_account_confirm)
        button.click()

    def alert_message_text(self):
        button = self.driver.find_element(*self.alert_message)
        button.text()
