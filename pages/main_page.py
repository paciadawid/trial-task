from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    # static locators
    __specialization_field_selector = (By.XPATH, "//input[@data-id='autocomplete-search']")
    __location_field_selector = (By.XPATH, "//input[@data-id='autocomplete-location']")
    __onetrust_accept_button_selector = (By.ID, "onetrust-accept-btn-handler")
    __search_button_selector = (By.CSS_SELECTOR, ".search-button")

    # dynamic XPATH locators
    __specialization_row_selector = "//div[@data-test-id='name' and contains(text(), '{specialization}')]"
    __city_row_selector = "//div[@data-test-id='location-dropdown']//span[contains(text(),'{city}')]"

    def accept_cookies(self):
        self.driver.find_element(*self.__onetrust_accept_button_selector).click()

    def select_specialization(self, specialization):
        self.driver.find_element(*self.__specialization_field_selector).click()
        self.driver.find_element(By.XPATH,
                                 self.__specialization_row_selector.format(specialization=specialization[1:])).click()

    def select_city(self, city):
        self.driver.find_element(*self.__location_field_selector).click()
        self.driver.find_element(By.XPATH, self.__city_row_selector.format(city=city)).click()

    def perform_search(self, specialization, city):
        self.select_specialization(specialization)
        self.select_city(city)
        self.driver.find_element(*self.__search_button_selector).click()
