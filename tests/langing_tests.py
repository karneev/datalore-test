from selenium.webdriver.common.by import By

from entiites.base_test import BaseTest
from entiites.helpers import wait_for_element
from pages.landing_page import LandingPage


class TestLandingPage(BaseTest):

    def test_main_page_appearance(self):
        landing_page = LandingPage(self.driver)
        landing_page.open()

        landing_title = wait_for_element(self, landing_page.landing_title_class, By.CLASS_NAME).text
        landing_subtitle = wait_for_element(self, landing_page.landing_subtitle_class, By.CLASS_NAME).text

        self.assertIn("Datalore", landing_title,
                      "Корректный тайтл страницы")

        self.assertEqual(landing_subtitle, "Get support",
                         "Корректный сабтайтл страницы")

        self.driver.find_elements(*landing_page.landing_link)[0].text

        self.assertEqual(self.driver.find_elements(*landing_page.landing_link)[0].text, "Support",
                         "Корректная ссылка на поддержку")

        self.assertEqual(self.driver.find_elements(*landing_page.landing_link)[1].text, "Documentation",
                         "Корректная ссылка на документацию")

        self.assertEqual(self.driver.find_elements(*landing_page.landing_link)[2].text, "Community forum",
                         "Корректная ссылка на форум")

        self.assertEqual(self.driver.find_elements(*landing_page.landing_link)[3].text, "Blog",
                         "Корректная ссылка на блог")
