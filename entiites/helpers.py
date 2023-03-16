from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def wait_for_element(self, elem, by=By.XPATH):
    return WebDriverWait(self.driver, 15).until(
        ec.presence_of_element_located((by, elem))
    )
