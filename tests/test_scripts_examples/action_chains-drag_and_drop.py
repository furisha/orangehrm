import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


def test_drag_and_drop():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
    driver.maximize_window()

    act = ActionChains(driver)
    rome_ele = driver.find_element(by=By.ID, value="box6")
    italy_ele = driver.find_element(by=By.ID, value="box106")
    act.drag_and_drop(rome_ele, italy_ele).perform()    # drag and drop

    time.sleep(3)
