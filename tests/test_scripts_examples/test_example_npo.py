import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_example_npo():

    driver = webdriver.Chrome()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(2.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    message_title = driver.find_element(by=By.CLASS_NAME, value="display-6")

    value = message.text
    value_message = message_title.text

    assert value_message == "Form submitted"
    assert value == "Received!"

    driver.quit()
