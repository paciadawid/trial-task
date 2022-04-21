from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config import IMPLICIT_WAIT_TIMEOUT


def create_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(IMPLICIT_WAIT_TIMEOUT)
    return driver
