import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


def test_double_click():

    driver = webdriver.Chrome()
    driver.get("https://seleniumbase.io/w3schools/double_click")
    driver.maximize_window()
    driver.switch_to.frame("iframeResult")

    button = driver.find_element(by=By.XPATH, value="//html/body/p[1]")

    act = ActionChains(driver)
    act.double_click(button).perform()

    time.sleep(3)
