import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


def test_scroll():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
    driver.maximize_window()

    # 1 Approach - Scroll down by pixels
    # driver.execute_script("window.scrollBy(0, 3000)", "")
    # value = driver.execute_script("return window.pageYOffset;")
    # print("Number of pixels moved:", value)  # 3000

    # 2 Approach - Scroll down till the element is visible
    # flag = driver.find_element(By.XPATH, "//img[@alt='Flag of Sri Lanka']")
    # driver.execute_script("arguments[0].scrollIntoView();", flag)
    #
    # value = driver.execute_script("return window.pageYOffset;")
    # print("Number of pixels moved:", value)  # 4284

    # 3 Approach scroll down page till ends
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    value = driver.execute_script("return window.pageYOffset;")
    print("Number of pixels moved:", value)  # 5966.5
    time.sleep(5)

    driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
    print("Number of pixels moved:", value)  # 5966.5
    time.sleep(5)
