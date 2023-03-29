import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys


def test_keyboard_actions():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://text-compare.com/")
    driver.maximize_window()

    input1 = driver.find_element(By.XPATH, "//textarea[@placeholder='Paste one version of a text here.']")
    # input2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

    input1.send_keys("welcome to selenium")
    time.sleep(3)

    act = ActionChains(driver)
    time.sleep(3)

    # Ctrl+A
    act.key_down(Keys.CONTROL)
    act.send_keys('a')
    act.key_up(Keys.CONTROL)
    act.key_down(Keys.DELETE)
    act.perform()

    # Ctrl+C
    act.key_down(Keys.CONTROL)
    act.send_keys('c')
    act.key_up(Keys.CONTROL)
    act.perform()

    # Press Tab key to navigate to other box
    act.send_keys(Keys.TAB).perform()
    time.sleep(3)

    # Ctrl+V
    act.key_down(Keys.CONTROL)
    act.send_keys('a')
    act.key_up(Keys.CONTROL)
    act.perform()

    time.sleep(3)
