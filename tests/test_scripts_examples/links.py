import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_checkboxes_number_of_links_print():

    driver = webdriver.Chrome()

    driver.get("https://demo.nopcommerce.com/")
    driver.maximize_window()

    # Click on link
    # driver.find_element(By.LINK_TEXT, "Digital downloads").click()
    # driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()

    # Find number of links in the page
    # links = driver.find_elements(By.TAG_NAME, 'a')
    links = driver.find_elements(By.XPATH, '//a')
    print(len(links))

    # Print all the link names
    for link in links:
        print(link.text)
