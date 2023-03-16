from selenium.webdriver.common.by import By

from entiites.base_page import BasePage

class LoadingPage(BasePage):

    def title(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Log in']")
