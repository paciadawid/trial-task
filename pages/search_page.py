import math
import time

from hamcrest import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class SearchPage(BasePage):
    __doctor_card_selector = (By.XPATH, "//div[@data-test-id='result-item']")
    __doctor_specialization_selector = (By.XPATH, "//*[@data-test-id='doctor-specializations']")
    __doctor_address_selector = (By.XPATH, "//div[@data-id='result-address-item']")
    __doctor_calendar_loaded_selector = (By.CSS_SELECTOR, ".dp-calendar-available, .dp-calendar-range-overbooked")
    __doctor_calendar_available_selector = (By.CSS_SELECTOR, ".dp-calendar-available")
    __active_next_days_button_selector = (By.CSS_SELECTOR, ".dp-carousel-nav-next:not([disabled])")

    # dynamic XPATH
    available_slot_selector = "//*[contains(@id,'item{days_offset}')]//button[contains(@class,'calendar-slot-available')]"

    def check_all_doctors_data(self, specialization, city):
        doctor_cards = self.driver.find_elements(*self.__doctor_card_selector)
        for doctor_card in doctor_cards:
            self.__check_doctor_data(specialization, city, doctor_card)

    def find_free_slot(self, offset_days=0):
        calendars = self.driver.find_elements(*self.__doctor_calendar_available_selector)
        next_clicks_number = math.ceil(offset_days / 4)
        for calendar in calendars:
            actions = ActionChains(self.driver)
            actions.move_to_element(calendar).perform()
            for _ in range(next_clicks_number):
                calendar.find_element(*self.__active_next_days_button_selector).click()
            try:
                calendar.find_element(By.XPATH, self.available_slot_selector.format(days_offset=offset_days)).click()
                return True
            except NoSuchElementException:
                pass
        raise NoSuchElementException

    def __check_doctor_data(self, specialization, city, doctor_card: WebElement):
        actions = ActionChains(self.driver)
        actions.move_to_element(doctor_card).perform()
        assert_that(doctor_card.find_element(*self.__doctor_card_selector).text, contains_string(specialization))
        assert_that(doctor_card.find_element(*self.__doctor_address_selector).text, contains_string(city))
        self.wait_until_element_present(self.__doctor_calendar_loaded_selector, doctor_card)
