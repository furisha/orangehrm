import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def headless_chrome():
    driver = webdriver.Chrome()
    ops = webdriver.ChromeOptions()
    ops.headless = True
    return driver

def headless_firefox():
    driver = webdriver.Firefox()
    ops = webdriver.FirefoxOptions()
    ops.headless = True
    return driver

# driver = headless_firefox()
driver = headless_chrome()

driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()
