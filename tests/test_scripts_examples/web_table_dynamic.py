import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_web_tables():

    driver = webdriver.Chrome()

    # Web Tables
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()

    # main_menu_search_class_name = "oxd-input--active"
    # main_menu_search_admin = "oxd-main-menu-item"

    driver.find_element(by=By.NAME, value="username").send_keys("Admin")
    time.sleep(3)
    driver.find_element(by=By.NAME, value="password").send_keys("admin123")
    driver.find_element(by=By.XPATH, value="//button[@type=('submit')]").click()
    time.sleep(3)
    driver.find_element(by=By.CLASS_NAME, value="oxd-input--active").send_keys('PIM')
    driver.find_element(by=By.CLASS_NAME, value="oxd-main-menu-item").click()

    time.sleep(5)
    # time.sleep(3)
    # //table[@id='resultTable']
    # total rows in a table
    # //div[@role='table']/div[2]/div[1]/div[1]     PRVI RED
    # //div[@role='table']/div[@role='rowgroup']/div[2]     # Drugi Red
    # //div[@role='table']/div[@role='rowgroup']/div[2]/div[1]/div      Colone u prvom redu
    # //div[@role='table']/div[@role='rowgroup']/div[2]/div[1]/div[1]   Checkbox
    # //div[@role='table']/div[@role='rowgroup']/div[2]/div[1]/div[2]   ID
    # rows = len(driver.find_elements(By.XPATH, "//div[@class='oxd-table-card'][1]//div[@role='cell'][5]//div"))
    # print("total number of rows", rows)
    rows = len(driver.find_elements(By.XPATH, "//div[@role='row']"))
    print("total number of rows", rows-1)

    count = 0
    for r in range(2, rows+1):
        number_of_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))

        # status = driver.find_element(By.XPATH, "//div[@class='oxd-table-card']["+str(r)+"]//div[@role='cell'][5]").text
        if status == "Enabled":
            count = count+1
            print(status)

    # print("Number of Users: ", rows)
    # print("Number of Enabled Users: ", count)
    # print("Number of Enabled Users: ", (rows - count))

    time.sleep(10)
    driver.close()











