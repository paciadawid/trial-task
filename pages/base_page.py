from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import EXPLICIT_WAIT_TIMEOUT


class BasePage:

    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def wait_until_element_present(self, selector, driver):
        if not driver:
            driver = self.driver
        return WebDriverWait(driver, EXPLICIT_WAIT_TIMEOUT).until(EC.visibility_of_element_located(selector))
