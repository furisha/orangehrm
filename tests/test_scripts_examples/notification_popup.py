import time

from selenium import webdriver
from selenium.webdriver.common.by import By

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")


def test_notification_popup():
    driver = webdriver.Chrome(options=ops)

    # Frame
    driver.get("https://whatmylocation.com/")
    time.sleep(5)
    driver.maximize_window()

    time.sleep(5)
