from selenium.webdriver.common.by import By

from entities.base_page import BasePage


class HomePage(BasePage):
    title_xpath = "//*[text()='Your notebooks']"
    title = (By.XPATH, title_xpath)

    def title(self):
        return self.driver.find_element(self.title)
