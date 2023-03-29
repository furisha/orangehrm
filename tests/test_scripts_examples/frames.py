import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_frames():
    driver = webdriver.Chrome()

    # Frame
    driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
    driver.maximize_window()

    driver.switch_to.frame("packageListFrame")  # This is Selenium 4 only!
    driver.find_element(by=By.LINK_TEXT, value="org.openqa.selenium").click()
    driver.switch_to.default_content()  # go back to main page

    driver.switch_to.frame("packageFrame")
    driver.find_element(By.LINK_TEXT, "WebDriver").click()
    driver.switch_to.default_content()

    driver.switch_to.frame("classFrame")
    driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[2]/ul[1]/li[1]/a").click()

    time.sleep(5)
