import os
import time
import unittest

from config import LOCALE
from pages.booking_page import BookingPage
from pages.main_page import MainPage
from pages.search_page import SearchPage
from utils.api_handler import get_locales
from utils.helpers import create_driver


class TestSearch(unittest.TestCase):

    def setUp(self) -> None:
        # file_location = os.path.join(os.getcwd(), "locales_data.json")
        base_url, self.specialization, self.city = get_locales(LOCALE)
        self.driver = create_driver()
        self.driver.get(base_url)
        self.main_page, self.search_page, self.booking_page = MainPage(self.driver), SearchPage(
            self.driver), BookingPage(self.driver)

    def test_test(self):
        self.main_page.accept_cookies()
        self.main_page.perform_search(self.specialization, self.city)
        self.search_page.check_all_doctors_data(self.specialization, self.city)
        self.search_page.find_free_slot(7)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
