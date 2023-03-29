import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


def test_mouse_hover():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()

    top_menu_computers = driver.find_element(by=By.XPATH, value="/html/body/div[4]/div[1]/div[2]/ul[1]/li[2]/a")
    top_menu_computers_notebooks = driver.find_element(by=By.XPATH, value="/html/body/div[4]/div[1]/div[2]/ul[1]/li[2]/ul/li[2]/a")
    time.sleep(1)

    act = ActionChains(driver)
    act.move_to_element(top_menu_computers).move_to_element(top_menu_computers_notebooks).click().perform()