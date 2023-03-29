import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains


def test_right_click():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
    driver.maximize_window()

    # driver.find_element(By.XPATH, "//span[normalize-space()='right click me']")
    button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

    act = ActionChains(driver)

    act.context_click(button).perform()  # perform right click with "context_click"

    time.sleep(5)
    driver.find_element(By.XPATH, "//span[normalize-space()='Copy']").click()  # copy option
    time.sleep(3)
    driver.switch_to.alert.accept()  # close popup/alert
    time.sleep(3)
