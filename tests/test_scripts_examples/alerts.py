import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_alerts():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    # Alert 1
    # driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    # driver.find_element(by=By.XPATH, value="//button[normalize-space()='Click for JS Prompt']").click()
    # time.sleep(3)
    # alert_window = driver.switch_to.alert
    # print(alert_window.text)
    # alert_window.send_keys("Welcome")
    # alert_window.accept()  # OK button
    # # alert_window.dismiss()  # Cancel Button
    # time.sleep(3)

    # Alert 2
    driver.get("https://mypage.rediff.com/login/dologin")
    time.sleep(3)
    driver.find_element(by=By.XPATH, value="//input[@value='Login']").click()
    time.sleep(3)
    driver.switch_to.alert.accept()
    time.sleep(5)
    # Alert 3 Authenticated Popup
    # driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    # time.sleep(5)

    driver.close()
