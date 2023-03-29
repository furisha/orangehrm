import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_checkboxes():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://monsterindia.com")
    driver.maximize_window()





    time.sleep(5)