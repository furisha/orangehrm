import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_browser_windows():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()

    driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()  # opening a new window tab
    windows_ids = driver.window_handles

    # Approach 1:
    # parent_window_id = windowsIDs[0]    #CDwindow-78A15AE446C15343DAAAB4A43E634EE4
    # child_window_id = windowsIDs[1]     #CDwindow-95C9E54C38D0DBF100DA0B2C0C5E2C59
    # # print(parent_window_id, child_window_id)
    #
    # driver.switch_to.window(child_window_id)
    # print("Title of the child window: ", driver.title)
    #
    # driver.switch_to.window(parent_window_id)
    # print("Title of the parent window: ", driver.title)

    # Approach 2:
    # for win_id in windowsIDs:
    #     driver.switch_to.window(win_id)
    #     print(driver.title)

    # Approach 3: Close specific browser windows
    for win_id in windows_ids:
        driver.switch_to.window(win_id)
        if driver.title == \
                "OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM" or driver.title == "XYZ":
            driver.close()

    time.sleep(5)
