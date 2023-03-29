import time
import pytest
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select

from utilities.custom_logger import LogGen
# from utilities.custom_logger import LogGenError

from utilities.read_properties import ReadLoginConfig
from utilities.read_properties import ReadMainMenuElements
from utilities.read_properties import ReadAdminConfigItems
from utilities.read_properties import ReadUrl

from page_objects.login_page.login import Login
from page_objects.main_menu import MainMenu
from page_objects.admin_page import AdminPage


class TestAdmin:
    # logger_error = LogGenError.logger_error()
    logger = LogGen.loggen()
    admin_config = ReadAdminConfigItems()
    login_config = ReadLoginConfig()
    main_menu_elements = ReadMainMenuElements()

    base_url = login_config.get_login_info('base_url')
    username_text = login_config.get_login_info('username_text')
    password_text = login_config.get_login_info('password_text')

    txt_main_menu_admin = main_menu_elements.get_main_menu_info("txt_main_menu_admin")
    txt_main_menu_my_info = main_menu_elements.get_main_menu_info("txt_main_menu_my_info")

    select_user_role_ess = admin_config.get_admin_info("select_user_role_ess")
    select_user_role_admin = admin_config.get_admin_info("select_user_role_admin")
    select_status_enabled = admin_config.get_admin_info("select_status_enabled")
    select_status_disabled = admin_config.get_admin_info("select_status_disabled")
    txt_input_username = admin_config.get_admin_info("txt_input_username")
    txt_input_employee_name = admin_config.get_admin_info("txt_input_employee_name")
    txt_input_username_admin = admin_config.get_admin_info("txt_input_username_admin")

    @pytest.fixture(autouse=False)
    def setup_test_script(self):
        yield
        self.driver.quit()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_admin_page_search(self, setup):
        self.logger.info("********************* START test_admin_page *********************")
        self.driver = setup
        self.driver.get(self.base_url)

        self.lp = LoginPage(self.driver)
        self.li.input_username(self.txt_admin_username)
        self.li.input_password(self.txt_admin_password)
        self.lp.click_login_button()

        self.mm = MainMenu(self.driver)
        self.mm.open_main_menu()
        self.mm.search_main_menu(self.txt_main_menu_admin)  # Insert text in search field
        # self.mm.search_main_menu_empty()
        self.mm.select_from_main_menu(self.txt_main_menu_admin)  # Click on Item from main menu

        self.ap = AdminPage(self.driver)
        self.ap.check_url()

        self.ap.test_table_records()

        self.ap.username(self.txt_input_username)
        self.ap.user_role(self.select_user_role_admin)
        # self.ap.employee(self.txt_input_employee_name)
        self.ap.status(self.select_status_enabled)
        self.ap.search_button()
        self.ap.table_row_user(self.txt_input_username_admin)
        # self.ap.table_row_user("Aaliyah.Haq")
        #
        self.ap.reset_button()
        #
        # Invalid message
        self.ap.username(self.txt_input_username)
        self.ap.user_role(self.select_user_role_ess)
        self.ap.random_employee()
        self.ap.status(self.select_status_enabled)
        self.ap.search_button()
        self.ap.employee_invalid_message()

        self.ap.reset_button()

        # Assert popup: Invalid Parameters
        self.ap.username(self.txt_input_username_admin)
        self.ap.user_role(self.select_user_role_admin)
        self.ap.status(self.select_status_disabled)
        self.ap.search_button()
        error = self.driver.find_element(By.ID, "oxd-toaster_1").text
        print(error)
        assert error == "Error\nInvalid Parameter\n×"
        # Assert empty table
        self.ap.table_row_empty()
        self.logger.info("********************* FINISH test_admin_page *********************")
        self.driver.quit()
