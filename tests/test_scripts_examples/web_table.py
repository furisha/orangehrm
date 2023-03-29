import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def test_web_tables():

    driver = webdriver.Chrome()

    # Web Tables
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()

    # 1 Count number of rows in table
    # //table[@name='BookTable']/tbody/tr[3]
    # //table[@name='BookTable']//tr[3]
    # //table[@name='BookTable']//tr

    number_of_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
    number_of_columns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th"))

    print(number_of_rows)
    print(number_of_columns)

    # 2 Read specific row & column data
    # Pointin on Master in Selenium:  //table[@name='BookTable']/tbody/tr[5]/td[1]
    # data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
    # print(data)

    # 3 Read all rows and columns data
    print("printing all the rows and columns data................")

    # for r in range(2, number_of_rows+1):
    #     for c in range(1, number_of_columns+1):
    #         data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
    #         print(data, end='                       ')
    #     print()

    # Read data based on condition (List books name whose author is Mukesh)
    for r in range(2, number_of_rows+1):
        author_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
        if author_name == "Mukesh":
            book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
            price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
            print(book_name, "                 ", author_name, "            ", price)
