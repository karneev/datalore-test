import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
