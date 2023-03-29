import time
import pytest
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.custom_logger import LogGen
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.relative_locator import locate_with

from utilities.read_properties import ReadLoginConfig
from utilities.read_properties import ReadMainMenuElements
from utilities.read_properties import ReadUrl

from page_objects.login_page import LoginPage
from page_objects.main_menu import MainMenu


class Test_003_Admin:

    logger = LogGen.loggen()
    login_config = ReadLoginConfig()
    main_menu_elements = ReadMainMenuElements()
    urls = ReadUrl()

    baseURL = login_config.get_login_info('baseURL')
    actualURL = login_config.get_login_info('actualURL')
    username = login_config.get_login_info('username')
    password = login_config.get_login_info('password')
    login_page_title = login_config.get_login_info('login_page_title')
    dashboard_page_url = login_config.get_login_info('dashboardURL')

    main_menu_search_admin = main_menu_elements.get_main_menu_info('txt_main_menu_search_admin')
    main_menu_search_pim = main_menu_elements.get_main_menu_info('txt_main_menu_search_pim')

    admin_page_url = urls.get_url_info('url_admin_page')
    pim_page_url = urls.get_url_info('url_pim_page')


    @pytest.fixture(autouse=True)
    def setup_test_script(self):
        yield
        self.driver.quit()


    def test_admin_page(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.login_user(self.username, self.password)

        self.mm = MainMenu(self.driver)
        self.mm.open_main_menu()

        # Print number of items in main menu
        # Print item names in text format
        main_menu_items_counter = self.driver.find_elements(by=By.CLASS_NAME, value="oxd-main-menu-item--name")
        print(len(main_menu_items_counter))
        for ele in main_menu_items_counter:
            print(ele.text)

        self.mm.main_menu_search_for(self.main_menu_search_admin)

        actual_admin_url = self.driver.current_url
        assert actual_admin_url == self.admin_page_url

        # TestCase: Search - Dropdown - User Role - Select ESS

        # Approach 1: Using position click [0], or [1] in this case
        # dd_menu_filters = self.driver.find_elements(by=By.CLASS_NAME, value="oxd-select-wrapper")
        # dd_menu_filters[0].click()
        # time.sleep(5)

        # Approach 2: Using Relative Locators / Label = Username

        system_user_username_label = self.driver.find_element(By.XPATH, "//label[text()='Username']")
        print("username_label text is: ", system_user_username_label.text)

        dd_menu_filters = self.driver.find_element(locate_with(By.CLASS_NAME, "oxd-select-wrapper").below(system_user_username_label))
        dd_menu_filters.click()
        print("Clicked on User Roles dd_button: ")

        drop_down_below_label_span = self.driver.find_element(locate_with(By.TAG_NAME, "span").below(system_user_username_label))
        print("drop_down_select below username label is: ", drop_down_below_label_span.text)

        drop_down_select_below_admin = self.driver.find_element(locate_with(By.TAG_NAME, "span").below(drop_down_below_label_span))
        print("below admin is: ", drop_down_select_below_admin.text)
        drop_down_select_below_admin.click()

        # TestCase: Search - Dropdown - Status - Select Disabled

        # Approach 1: Using position click [0], or [1] in this case
        # dd_menu_filters = self.driver.find_elements(by=By.CLASS_NAME, value="oxd-select-wrapper")
        # dd_menu_filters[1].click()
        # time.sleep(5)

        # Approach 2: Using Relative Locators / Label = Status

        system_user_status_label = self.driver.find_element(By.XPATH, "//label[text()='Status']")
        print("status_label text is: ", system_user_status_label.text)

        dd_menu_filters = self.driver.find_element(
            locate_with(By.CLASS_NAME, "oxd-select-wrapper").below(system_user_status_label))
        dd_menu_filters.click()
        print("Clicked on Status dd_button: ")

        # dd_tag_name_span_below_status_label
        dd_tag_name_span_below_status_label = self.driver.find_element(
            locate_with(By.TAG_NAME, "span").below(system_user_status_label))
        print("drop_down_select below status label is: ", dd_tag_name_span_below_status_label.text)

        dd_tag_name_span_below_enabled = self.driver.find_element(
            locate_with(By.TAG_NAME, "span").below(dd_tag_name_span_below_status_label))
        print("below enabled is: ", dd_tag_name_span_below_enabled.text)
        dd_tag_name_span_below_enabled.click()

        # time.sleep(1)

        # reset all search filters
        reset_button = self.driver.find_element(By.CLASS_NAME, "oxd-button--ghost")
        print("Reset:", reset_button.text)
        reset_button.click()

        time.sleep(10)

        # Input username
        # search_label = self.driver.find_element(By.XPATH, "//label[contains(normalize-space(),'Username')]")
        search_button_active = self.driver.find_element(By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']/child::div[2]")
        search_button_active.click()
        print("Selected: Username Drop Down")

        search_button_focus = self.driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--focus']")
        search_button_focus.send_keys("Admin")
        print("Inputed: Admin")


        # Select Admin option from User Role dropdown menu # x2
        dd_menu_filters = self.driver.find_elements(by=By.CLASS_NAME, value="oxd-select-wrapper")
        # print(len(user_role))
        dd_menu_filters[0].click()
        time.sleep(2)
        select_text_default = self.driver.find_element(By.XPATH, "//div[@class='oxd-select-option']")
        print("default: ", select_text_default.text)
        role_list_admin = self.driver.find_element(By.XPATH, "//div[@class='oxd-select-option']/child::span[contains(text(), 'Admin')]")
        role_list_admin.click()
        time.sleep(2)


        # input hints
        # // input[contains( @ placeholder, 'Type for hints..')]
        # input_hints = self.driver.find_element(By.XPATH, "//input[contains(@placeholder,'Type for hints..')]")
        # input_hints.send_keys("Paul Collings")
        # time.sleep(5)

        # search filters button
        search_system_users_button = self.driver.find_element(By.CLASS_NAME, "orangehrm-left-space")
        print("Button Text: ", search_system_users_button.text)
        search_system_users_button.click()
        time.sleep(1)

        # status dropdown filter
        dd_menu_filters = self.driver.find_elements(by=By.CLASS_NAME, value="oxd-select-wrapper")
        # print(len(user_role))
        dd_menu_filters[1].click()
        print("STATUS: Menu open")
        time.sleep(10)


