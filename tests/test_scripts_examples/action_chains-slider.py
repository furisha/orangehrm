import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains


def test_slider():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
    driver.maximize_window()

    min_slider = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[1]")
    max_slider = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[2]")

    print("Location of sliders before moving")
    print(min_slider.location)  # {'x': 59, 'y': 251}
    print(max_slider.location)  # {'x': 604, 'y': 251}

    act = ActionChains(driver)

    act.drag_and_drop_by_offset(min_slider, 100, 0).perform()
    act.drag_and_drop_by_offset(max_slider, -40, 0).perform()

    print("Location of sliders after moving")
    print(min_slider.location)
    print(max_slider.location)
