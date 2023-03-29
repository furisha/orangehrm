# We need to install "requests" package

import requests as requests
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_broken_links_and_print_them():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://deadlinkcity.com/")
    driver.maximize_window()

    all_links = driver.find_elements(By.TAG_NAME, 'a')
    count = 0

    for link in all_links:
        url = link.get_attribute('href')
        try:
            res = requests.head(url)
        except:
            None

        if res.status_code >= 400:
            print(url, "is broken lnk")
            count += 1
        else:
            print(url, " is valid link")

    print("Total number of broken links:", count)
