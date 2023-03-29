import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

location = os.getcwd()


def chrome_setup():
    driver = webdriver.Chrome()

    # download files in desired location
    preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally": True}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)
    # ops.add_experimental_option("prefs", preferences)

    return driver


driver = chrome_setup()
# driver = firefox_setup()

driver.implicitly_wait(20)
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")  # pdf

driver.maximize_window()
# time.sleep(5)
driver.execute_script("window.scrollBy(0, 500)", "")
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='table-files']/tbody/tr[3]/td[5]/a").click()
time.sleep(15)
