import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_date_picker_2():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    # Date of Birth in Dummy Tickets for Visa Application
    driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    driver.maximize_window()

    driver.find_element(By.XPATH, "//input[@id='dob']").click()  # opens date_picker
    date_picker_month = Select(driver.find_element(By.XPATH, "//select[@data-handler='selectMonth']"))  # select month
    date_picker_month.select_by_visible_text("Dec")  # month selected

    date_picker_year = Select(driver.find_element(By.XPATH, "//select[@data-handler='selectYear']"))  # select year
    date_picker_year.select_by_visible_text("1990")  # year selected

    # find all date and search for 25. if 25 then click.
    alldates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

    for date in alldates:
        if date.text == "25":
            date.click()
            break

    time.sleep(5)
