import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver import Keys


def test_cookies():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://demo.nopcommerce.com/")
    driver.maximize_window()

    # capture cookies
    cookies = driver.get_cookies()
    print("Size of cookies", len(cookies))  # return 3

    # print details of all cookies
    for c in cookies:
        print(c)
        print(c.get('name'), ":", c.get('value'))

    # add new cookies to the browser
    driver.add_cookie({"name": "MyCookie", "value": "123456"})
    driver.add_cookie({"name": "test1", "value": "cookie1"})
    driver.add_cookie({"name": "test2", "value": "cookie2"})
    cookies = driver.get_cookies()
    print("Size of cookies after adding new one: ", len(cookies))  # return 6

    # delete specific cookie from the browser
    driver.delete_cookie("MyCookie")
    cookies = driver.get_cookies()
    print("Size of cookies after deleting new one: ", len(cookies))  # 5

    # delete all cookies
    driver.delete_all_cookies()
    cookies = driver.get_cookies()
    print("Size of cookies after deleting all cookies: ", len(cookies))  # 0

    driver.close()
