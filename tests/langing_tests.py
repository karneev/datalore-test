import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

from pages.landing_page import LandingPage
from tests.base_test import BaseTest


class TestMainPage(BaseTest):

    def test_mainpage_appearance(self):
        pass