from selenium.webdriver.common.by import By

from config.config import url,  user_login, user_password


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def set_login(self):
        email = self.driver.find_element(By.XPATH, "//input[@placeholder='Email']")
        email.send_keys(user_login)

    def set_password(self):
        password = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password.send_keys(user_password)

    def open(self):
        self.driver.get(url)

    def submit(self):
        button = self.driver.find_element(By.CLASS_NAME, "wt-button_align-icon_left")
        button.click()

    def forgot_password(self):
        button = self.driver.find_element(By.CLASS_NAME, "wt-button_align-icon_left")
        button.click()

