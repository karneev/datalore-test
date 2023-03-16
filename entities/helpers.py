import string
from random import choice

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def wait_for_element(self, elem, by=By.XPATH):
    return WebDriverWait(self.driver, 15).until(
        ec.presence_of_element_located((by, elem))
    )


def gen_email():
    address = ''.join(choice(string.ascii_lowercase) for i in range(7))
    return address + "@test.com"


def gen_password():
    letters = ''.join(choice(string.ascii_lowercase) for i in range(4))
    numbers = ''.join(choice(string.digits) for i in range(2))
    letters_uppercase = ''.join(choice(string.ascii_uppercase) for i in range(2))
    signs = ''.join(choice(string.punctuation) for i in range(2))

    return letters + numbers + letters_uppercase + signs

def gen_weak_password():
    return ''.join(choice("0123456789") for i in range(5))
