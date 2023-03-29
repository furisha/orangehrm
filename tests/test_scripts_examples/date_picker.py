import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_date_picker():
    driver = webdriver.Chrome()
    driver.get("https:/jqueryui.com/datepicker/")
    driver.maximize_window()
    driver.switch_to.frame(0)
    # driver.find_element(By.XPATH, "//*[@id='datepicker']").send_keys("05/30/2022")

    month = "March"
    year = "2023"
    date = "30"

    driver.find_element(By.XPATH, "//*[@id='datepicker']").click()  # open date_picker

    # select month and year
    while True:
        mo = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
        yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

        if mo == month and yr == year:
            break
        else:
            time.sleep(1)
            driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()  # next arrow
            # driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click()  # prev arrow

    # select date
    dates = driver.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[1]/a")

    for ele in dates:
        if ele.text == date:
            time.sleep(1)
            ele.click()
            break

    time.sleep(5)


