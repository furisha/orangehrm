import pytest
import time
import random
import string
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilities.read_properties import ReadAdminConfigItems
from utilities.read_properties import ReadLabelsConfig
from selenium.webdriver.support.relative_locator import locate_with
from utilities.custom_logger import LogGen


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class AdminPage:

    admin_config = ReadAdminConfigItems()
    label_config = ReadLabelsConfig()

    logger = LogGen.loggen()

    url_admin_actual = admin_config.get_admin_info('url_admin_actual')
    button_search_xpath = admin_config.get_admin_info('button_search_xpath')
    button_reset_class_name = admin_config.get_admin_info('button_reset_class_name')

    label_username_xpath = label_config.get_labels_info('label_username_xpath')
    label_user_role_xpath = label_config.get_labels_info('label_user_role_xpath')
    label_status_xpath = label_config.get_labels_info('label_status_xpath')
    # label_employee_xpath = label_config.get_labels_info('label_employee_name_xpath')
    label_employee_name_xpath = label_config.get_labels_info('label_employee_name_xpath')

    dropdown_select_class_name = admin_config.get_admin_info('dropdown_select_class_name')
    dropdown_items_xpath = admin_config.get_admin_info('dropdown_items_xpath')
    select_user_role_ess = admin_config.get_admin_info('select_user_role_ess')
    select_user_role_admin = admin_config.get_admin_info('select_user_role_admin')
    select_status_enabled = admin_config.get_admin_info('select_status_enabled')
    select_status_disabled = admin_config.get_admin_info('select_status_disabled')
    records_found_xpath = admin_config.get_admin_info('records_found_xpath')
    # table_row_first_xpath = admin_config.get_admin_info('table_row_first_xpath')
    # table_cell_username_first_xpath = admin_config.get_admin_info('table_cell_username_first_xpath')
    # table_row_all_xpath = admin_config.get_admin_info('table_row_all_xpath')
    # table_admin_xpath = admin_config.get_admin_info('table_admin_xpath')
    # table_row_first_xpath_card = admin_config.get_admin_info('table_row_first_xpath_card')

    # Create Constructor
    def __init__(self, driver):
        self.driver = driver

    def check_url(self):
        login_url = self.driver.current_url
        assert login_url == self.url_admin_actual
        print("login url is: ", login_url)

    def username(self, input_username):
        username_label = self.driver.find_element(By.XPATH, self.label_username_xpath)
        assert username_label.is_displayed()
        self.logger.info("label username: " + username_label.text + " *** PASS ***")
        username_input = self.driver.find_element(
            locate_with(By.TAG_NAME, "input").below(username_label))
        assert username_input.is_displayed()
        username_input.send_keys(input_username)

    def random_username(self):
        random_input = random_generator()
        username_label = self.driver.find_element(By.XPATH, self.label_username_xpath)
        self.logger.info("label username: " + username_label.text + " *** PASS ***")
        assert username_label.is_displayed()
        username_input = self.driver.find_element(
            locate_with(By.TAG_NAME, "input").below(username_label))
        assert username_input.is_displayed()
        username_input.send_keys(random_input)

    def user_role(self, user_role):
        user_role_label = self.driver.find_element(By.XPATH, self.label_username_xpath)
        assert user_role_label.is_displayed()
        # time.sleep(10)
        dropdown_user_role_options = self.driver.find_element(
            locate_with(By.CLASS_NAME, self.dropdown_select_class_name).below(user_role_label))
        # time.sleep(10)
        dropdown_user_role_options.click()

        assert dropdown_user_role_options.is_displayed()

        user_roles_items_counter = self.driver.find_elements(By.XPATH, self.dropdown_items_xpath)
        for user_roles_items in user_roles_items_counter:
            if user_roles_items.text == user_role:
                assert user_roles_items.is_displayed()
                user_roles_items.click()
                break

    def employee(self, input_employee):
        employee_name_label = self.driver.find_element(By.XPATH, self.label_employee_name_xpath)
        assert employee_name_label.is_displayed()
        employee_name = self.driver.find_element(
            locate_with(By.TAG_NAME, "input").below(employee_name_label))
        assert employee_name.is_displayed()
        employee_name.send_keys(input_employee)

    def random_employee(self):
        random_input = random_generator()
        # input employee name
        employee_name_label = self.driver.find_element(By.XPATH, self.label_employee_name_xpath)
        assert employee_name_label.is_displayed()
        employee_name = self.driver.find_element(
            locate_with(By.TAG_NAME, "input").below(employee_name_label))
        assert employee_name.is_displayed()
        employee_name.send_keys(random_input)

    def status(self, select_status):
        user_status_label = self.driver.find_element(By.XPATH, self.label_status_xpath)
        assert user_status_label.is_displayed()
        dropdown_status_options = self.driver.find_element(
            locate_with(By.CLASS_NAME, self.dropdown_select_class_name).below(user_status_label))
        dropdown_status_options.click()
        assert dropdown_status_options.is_displayed()
        status_items_counter = self.driver.find_elements(By.XPATH, self.dropdown_items_xpath)
        for status_items in status_items_counter:
            if status_items.text == select_status:
                assert status_items.is_displayed()
                status_items.click()
                break

    def reset_button(self):
        reset_button = self.driver.find_element(By.CLASS_NAME, self.button_reset_class_name)
        assert reset_button.is_displayed()
        reset_button.click()
        time.sleep(1)

    def search_button(self):
        try:
            button_search = self.driver.find_element(By.XPATH, self.button_search_xpath)
            assert button_search.is_displayed()
            button_search.click()
            time.sleep(1)
        except Exception as e:
            self.logger.error("button_search is not visible", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

    def employee_invalid_message(self):
        employee_name_label = self.driver.find_element(By.XPATH, self.label_employee_name_xpath)
        assert employee_name_label.is_displayed()
        invalid_message = self.driver.find_element(
            locate_with(By.TAG_NAME, "span").below(employee_name_label))
        assert invalid_message.is_displayed()

    def test_table_records(self):
        time.sleep(1)
        all_rows_in_table_page_1 = len(self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']"))
        print(all_rows_in_table_page_1)

        if all_rows_in_table_page_1 == 50:
            print("there is more than 1 page", all_rows_in_table_page_1)

            # Click on pagination 2 button
            pagination_2_button = self.driver.find_element(By.XPATH, "//ul[@class='oxd-pagination__ul']//li[2]").click()
            print("Pagination button 2 is clicked", pagination_2_button)

            # Count number of rows on page 2
            all_rows_in_table_page_2 = len(self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']"))
            print(all_rows_in_table_page_2)

            # Total number of rows 1 + 2
            all_rows_total = all_rows_in_table_page_1 + all_rows_in_table_page_2
            print("Rows numbers PAGE 1 + PAGE 2 = ", all_rows_total)

            # Click on pagination 1 button (back)
            pagination_1_button = self.driver.find_element(By.XPATH, "//ul[@class='oxd-pagination__ul']//li[1]").click()
            print("Pagination button 1 is clicked", pagination_1_button)

            # self.driver.find_element(By.XPATH, "//ul[@class='oxd-pagination__ul']//li[1]").click()
            table_records_found_text = self.driver.find_element(By.XPATH, self.records_found_xpath).text
            table_records_found_number = re.sub(r"\D", '', table_records_found_text)
            print("table_records_found_number", table_records_found_number)

            assert str(all_rows_total) == table_records_found_number
            print(all_rows_total)
        else:
            print("there is only 1 page", all_rows_in_table_page_1)

            table_records_found_text = self.driver.find_element(By.XPATH, self.records_found_xpath).text
            table_records_found_number = re.sub(r"\D", '', table_records_found_text)
            print("table_records_found_number", table_records_found_number)

            assert str(all_rows_in_table_page_1) == table_records_found_number
            print("record founds number and number of rows are equal")

        time.sleep(3)

    def table_row_user(self, table_username):
        all_rows_in_table_page_1 = len(self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']"))
        try:
            table_row = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.table_cell_username_first_xpath)))
            assert table_row.text == table_username
        except Exception as e:
            self.logger.error("table_row is not visible", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

    def table_row_empty(self):

        all_rows_in_table_page_1 = len(self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']"))

        if all_rows_in_table_page_1 == 0:
            print("no rows")
            assert True
        else:
            print("row exists")
            assert False
