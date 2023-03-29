import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_dropdown():
    driver = webdriver.Chrome()

    driver.get("https://demowebshop.tricentis.com/desktops")

    time.sleep(1)
    # With Select
    dropdown_sort_by_ele = Select(driver.find_element(by=By.ID, value="products-orderby"))
    # method by visible text
    # dropdown_sort_by_ele.select_by_visible_text("Created on")
    # method by value
    # dropdown_sort_by_ele.select_by_value("https://demowebshop.tricentis.com/desktops?orderby=5")
    # method by index
    # dropdown_sort_by_ele.select_by_index(5)

    # capture all the options and print them
    alloptions = dropdown_sort_by_ele.options
    print("total numer of options are: ", len(alloptions))

    for opt in alloptions:
        print(opt.text)

    # select option from dropdown without using build-in-method
    # for opt in alloptions:
    #     if opt.text == "Price: High to Low":
    #         opt.click()
    #         break

    # Without select
    all_options = driver.find_elements(By.XPATH, '//*[@id="products-orderby"]/option')
    print(len(all_options))
