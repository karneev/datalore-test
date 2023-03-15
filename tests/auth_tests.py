import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

from pages.landing_page import MainPage


class TestMainPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        landing_page = MainPage(self.driver)

        landing_page.open()
        landing_page.set_login()
        landing_page.set_password()
        landing_page.submit()

    def test_create_account(self):
        pass

    def test_forgot_password(self):
        pass

    def test_login_no_password(self):
        pass

    def test_wrong_password(self):
        pass

    def test_no_email_on_forgot(self):
        pass

    def test_password_eye(self):
        pass

    def tearDown(self):
        self.driver.close()
