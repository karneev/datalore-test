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
    sign_up_label = (By.XPATH, "//*[text()='Sign Up']")
    alert_message = (By.CLASS_NAME, "alert_message-error")
    instructions_xpath = "//*[contains(text(),'Check your email')]"
    instructions = (By.XPATH, instructions_xpath)
    password_is_required_alert_xpath = "//*[text()='Password is required']"
    password_is_required_alert = (By.XPATH, password_is_required_alert_xpath)
    email_is_required_alert_xpath = "//*[text()='Email is required']"
    email_is_required_alert = (By.XPATH, email_is_required_alert_xpath)

    landing_title_class = "landing__title"
    landing_subtitle_class = "landing__subtitle"
    landing_title = (By.CLASS_NAME, landing_title_class)
    landing_subtitle = (By.CLASS_NAME, "landing__subtitle")
    landing_link = (By.CLASS_NAME, "landing__link")

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

    def restore_pass_instructions(self):
        instructions = self.driver.find_element(*self.instructions)
        instructions.text()

    def get_landing_title(self):
        title = self.driver.find_element(*self.landing_title)
        return title.text()

    def get_landing_subtitle(self):
        subtitle = self.driver.find_element(*self.landing_title)
        return subtitle.text()

    def get_landing_links(self):
        return self.driver.find_elements(*self.landing_link)


