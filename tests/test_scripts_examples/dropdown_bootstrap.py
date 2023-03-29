import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_dropdown_bootstrap():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    driver.maximize_window()

    driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()

    county_lists = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")
    print(len(county_lists))

    for country in county_lists:
        if country.text == "Serbia":
            country.click()
            break

    time.sleep(10)
