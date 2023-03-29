import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# IMPORTANT NOTE: for, if, range, len


def test_checkboxes():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://itera-qa.azurewebsites.net/home/automation")
    driver.maximize_window()

    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
    print(len(checkboxes))

    # APPROACH 1 - Select all checkboxes
    # for i in range(len(checkboxes)):
    #     checkboxes[i].click()

    # APPROACH 2 - Select all checkboxes
    for checkbox in checkboxes:
        checkbox.click()

    # APPROACH 3 - Select multiple checkboxes (ec. Monday and Saturday) by choice
    # for checkbox in checkboxes:
    #     weekname = checkbox.get_attribute('id')
    #     if weekname == 'monday' or weekname == 'sunday':
    #         checkbox.click()

    # APPROACH 4 - Select last 2 checkboxes (totalnumer of checkboxes - 2 =  starting index)
    # for i in range(len(checkboxes)-2, len(checkboxes)):
    #     checkboxes[i].click()
    # time.sleep(10)

    # APPROACH 5 - Select first 2 checkboxes
    # for i in range(len(checkboxes)):
    #     if i<2:
    #         checkboxes[i].click()

    # APPROACH 6 - Unselect all checkboxes
    for checkbox in checkboxes:
        if checkbox.is_selected():
            checkbox.click()

    time.sleep(5)
