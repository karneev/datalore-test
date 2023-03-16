from selenium.webdriver.common.by import By

from entities.base_page import BasePage


class LoadingPage(BasePage):

    title_class = "loading-page__title"

    def title(self):
        return self.driver.find_element(By.CLASS_NAME, self.title_class)

    def logo(self):
        return self.driver.find_element(By.CLASS_NAME, "logo")


