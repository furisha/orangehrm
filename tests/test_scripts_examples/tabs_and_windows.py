import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_tabs_and_windows():
    driver = webdriver.Chrome()
    # driver.get("https://demo.nopcommerce.com/")
    # driver.maximize_window()
    # time.sleep(5)
    # # registration_link = Keys.CONTROL+Keys.RETURN
    # driver.find_element(By.LINK_TEXT, "Register").send_keys(Keys.COMMAND+"t")
    # time.sleep(5)

    # Selenium 4 TAB
    # driver.get("https://demo.nopcommerce.com/")
    # driver.switch_to.new_window('tab')
    # driver.get("https://demo.nopcommerce.com/books")

    # Selenium 4 WINDOW
    driver.get("https://demo.nopcommerce.com/")
    driver.switch_to.new_window('window')
    driver.get("https://demo.nopcommerce.com/books")
    time.sleep(5)
