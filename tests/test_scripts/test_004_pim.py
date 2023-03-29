

import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.custom_logger import LogGen
from selenium.webdriver.support.select import Select

from utilities.read_properties import ReadLoginConfig
from utilities.read_properties import ReadMainMenuElements
from utilities.read_properties import ReadTopBarConfig
from utilities.read_properties import ReadPimElements
from utilities.read_properties import ReadMyInfoConfig

from page_objects.login_page.login import Login
from page_objects.main_menu import MainMenu
from page_objects.topbar import TopBar
from page_objects.pim_page.pim_page_visibility import PIMPageVisibility
from page_objects.pim_page.pim_add_employee_page_visibility import PIMAddEmployeePageVisibility
from page_objects.pim_page.pim_add_employee import PIMAddEmployee
from page_objects.pim_page.pim_page_search_employee import PIMPageSearchEmployee
from page_objects.pim_page.pim_add_employee_page_error_messages import PIMAddEmployeeErrorMessages
from page_objects.my_info_page import MyInfoPage
import os


class TestPIM:

    logger = LogGen.loggen()

    login_config = ReadLoginConfig()
    main_menu_elements = ReadMainMenuElements()
    topbar_config = ReadTopBarConfig()
    my_info_config = ReadMyInfoConfig()

    base_url = login_config.get_login_info('base_url')

    txt_admin_username = login_config.get_login_info('txt_admin_username')
    txt_admin_password = login_config.get_login_info('txt_admin_password')

    txt_topbar_user_dropdown_menu_item_logout = topbar_config.get_topbar_info('txt_topbar_user_dropdown_menu_item_logout')
    txt_main_menu_pim = main_menu_elements.get_main_menu_info('txt_main_menu_pim')

    txt_employee_first_name = my_info_config.get_my_info_info('txt_employee_first_name')
    txt_employee_middle_name = my_info_config.get_my_info_info('txt_employee_middle_name')
    txt_employee_last_name = my_info_config.get_my_info_info('txt_employee_last_name')
    txt_employee_id = my_info_config.get_my_info_info('txt_employee_id')
    txt_employee_username = my_info_config.get_my_info_info('txt_employee_username')
    txt_employee_password = my_info_config.get_my_info_info('txt_employee_password')



    @pytest.fixture(autouse=False)
    def setup_test_script(self):
        yield
        self.driver.quit()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_pim_page_visibility(self, setup):

        self.logger.info("********************* START test_pim_page_visibility")
        self.driver = setup
        self.driver.get(self.base_url)

        self.li = Login(self.driver)
        self.tb = TopBar(self.driver)
        self.mm = MainMenu(self.driver)
        self.ppv = PIMPageVisibility(self.driver)

        self.tb.logout_if_not()

        self.li.input_username(self.txt_admin_username)
        self.li.input_password(self.txt_admin_password)
        self.li.click_login_button()

        self.mm.open_main_menu()
        self.mm.select_from_main_menu(self.txt_main_menu_pim)

        self.ppv.pim_page_visibility()
        self.logger.info("********************* END test_pim_page_visibility")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_pim_page_error_messages(self, setup):
        self.logger.info("********************* START test_pim_page_error_messages")
        self.driver = setup
        self.driver.get(self.base_url)

        self.li = Login(self.driver)
        self.tb = TopBar(self.driver)
        self.mm = MainMenu(self.driver)

        self.tb.logout_if_not()

        self.li.input_username(self.txt_admin_username)
        self.li.input_password(self.txt_admin_password)
        self.li.click_login_button()

        self.mm.open_main_menu()
        self.mm.select_from_main_menu(self.txt_main_menu_pim)

        # Under Construction

        self.logger.info("********************* END test_pim_page_error_messages")

    @pytest.mark.regression
    def test_pim_add_employee_page_visibility(self, setup):
        self.logger.info("********************* START test_pim_add_employee_page_visibility")
        self.driver = setup
        self.driver.get(self.base_url)

        self.li = Login(self.driver)
        self.tb = TopBar(self.driver)
        self.mm = MainMenu(self.driver)
        self.pim_aepv = PIMAddEmployeePageVisibility(self.driver)
        self.pim_ae = PIMAddEmployee(self.driver)

        self.tb.logout_if_not()

        self.li.input_username(self.txt_admin_username)
        self.li.input_password(self.txt_admin_password)
        self.li.click_login_button()

        self.mm.open_main_menu()
        self.mm.select_from_main_menu(self.txt_main_menu_pim)

        self.pim_ae.click_add_button()
        self.pim_aepv.add_employee_page_visibility()
        self.logger.info("********************* END test_pim_add_employee_page_visibility")

    @pytest.mark.regression
    def test_pim_add_employee_page_error_messages(self, setup):
        self.logger.info("********************* START test_pim_add_employee_page_error_messages")
        self.driver = setup
        self.driver.get(self.base_url)

        self.li = Login(self.driver)
        self.tb = TopBar(self.driver)
        self.mm = MainMenu(self.driver)
        self.pim_aepv = PIMAddEmployeePageVisibility(self.driver)
        self.pim_ae = PIMAddEmployee(self.driver)
        self.pim_em = PIMAddEmployeeErrorMessages(self.driver)

        self.tb.logout_if_not()

        self.li.input_username(self.txt_admin_username)
        self.li.input_password(self.txt_admin_password)
        self.li.click_login_button()

        self.mm.open_main_menu()
        self.mm.select_from_main_menu(self.txt_main_menu_pim)

        self.pim_ae.click_add_button()
        self.pim_ae.checkbox_create_login_details_on()
        self.pim_ae.click_save_button()

        self.pim_em.required_error_message_first_name()
        self.pim_em.required_error_message_lastname()
        self.pim_em.required_error_message_username()
        self.pim_em.required_error_message_password()
        self.pim_em.required_error_message_confirm_password()
        # self.pp.click_cancel_button()

        # Under construction
        # Add other error messages

        self.logger.info("********************* END test_pim_add_employee_page_error_messages")

    @pytest.mark.regression
    def test_pim_add_employee(self, setup):
        self.logger.info("********************* START test_pim_add_employee")
        self.driver = setup
        self.driver.get(self.base_url)

        self.li = Login(self.driver)
        self.tb = TopBar(self.driver)
        self.mm = MainMenu(self.driver)
        self.pim_ae = PIMAddEmployee(self.driver)
        self.mi = MyInfoPage(self.driver)
        self.pimp_se = PIMPageSearchEmployee(self.driver)

        self.tb.logout_if_not()

        self.li.input_username(self.txt_admin_username)
        self.li.input_password(self.txt_admin_password)
        self.li.click_login_button()

        self.mm.open_main_menu()
        self.mm.select_from_main_menu(self.txt_main_menu_pim)

        self.pim_ae.click_add_button()
        self.pim_ae.checkbox_create_login_details_on()
        self.pim_ae.input_first_name(self.txt_employee_first_name)
        self.pim_ae.input_middle_name(self.txt_employee_middle_name)
        self.pim_ae.input_last_name(self.txt_employee_last_name)
        self.pim_ae.input_employee_id(self.txt_employee_id)
        self.pim_ae.input_username(self.txt_employee_username)
        self.pim_ae.input_password(self.txt_employee_password)
        self.pim_ae.input_password_confirm(self.txt_employee_password)
        self.pim_ae.click_save_button()

        self.mi.title_personal_details()

        self.tb.logout_if_not()

        self.li.input_username(self.txt_employee_username)
        self.li.input_password(self.txt_employee_password)
        self.li.click_login_button()

        # assert login with new employee
        self.mm.open_main_menu()
        self.tb.topbar_name()
        self.tb.topbar_header_title()

        # post-condition: login with admin, delete new employee from table
        self.tb.logout_if_not()

        self.li.input_username(self.txt_admin_username)
        self.li.input_password(self.txt_admin_password)
        self.li.click_login_button()

        self.mm.open_main_menu()
        self.mm.select_from_main_menu(self.txt_main_menu_pim)

        self.pimp_se.pim_page_search_user_by_id()
        self.pimp_se.pim_page_table_employee_id()

        self.pimp_se.pim_page_delete_employee_from_table()

        self.logger.info("********************* END test_pim_add_employee")


    # @pytest.mark.regression
    # def test_pim_page_add_user_required_error_messages(self, setup):
    #     self.logger.info("********************* START test_pim_page_add_user_required_error_messages *********************")
    #     self.driver = setup
    #     self.driver.get(self.base_url)
    #
    #     self.mm = MainMenu(self.driver)
    #     self.pp = PimAddEmployeePage(self.driver)
    #     self.lp = LoginPage(self.driver)
    #     self.tb = TopBar(self.driver)
    #
    #     self.tb.logout_if_not()
    #
    #     self.lp.input_username(self.username_text)
    #     self.lp.input_password(self.password_text)
    #     self.lp.click_login_button()
    #
    #     self.mm.open_main_menu()
    #     self.mm.select_from_main_menu(self.search_pim)
    #
    #     self.pp.click_add_button()
    #     self.pp.checkbox_create_login_details_on()
    #     self.pp.click_save_button()
    #     self.pp.required_error_message_first_name()
    #     self.pp.required_error_message_lastname()
    #     self.pp.required_error_message_username()
    #     self.pp.required_error_message_password()
    #     self.pp.required_error_message_confirm_password()
    #     # self.pp.click_cancel_button()
    # #     self.logger.info("********************* END test_pim_page_add_user_required_error_messages *********************")
    #
    # @pytest.mark.regression
    # def test_pim_page_add_employee_with_credentials(self, setup):
    #     self.logger.info("********************* START test_pim_page_add_employee_with_credentials *********************")
    #     self.driver = setup
    #     self.driver.get(self.base_url)
    #
    #     self.mm = MainMenu(self.driver)
    #     self.pp = PimAddEmployeePage(self.driver)
    #     self.mi = MyInfoPage(self.driver)
    #     self.lp = LoginPage(self.driver)
    #     self.tb = TopBar(self.driver)
    #     self.pi = PimPage(self.driver)
    #
    #     self.tb.logout_if_not()
    #
    #     self.lp.input_username(self.username_text)
    #     self.lp.input_password(self.password_text)
    #     self.lp.click_login_button()
    #
    #     self.mm.open_main_menu()
    #     self.mm.select_from_main_menu(self.search_pim)
    #
    #     self.pp.click_add_button()
    #     self.pp.checkbox_create_login_details_on()
    #     self.pp.input_first_name("firstname")
    #     self.pp.input_middle_name("middle name")
    #     self.pp.input_last_name("last name")
    #     self.pp.input_employee_id("0000")
    #     self.pp.input_username("orange_user_001")
    #     self.pp.input_password("Test_Password123")
    #     self.pp.input_password_confirm("Test_Password123")
    #     self.pp.click_save_button()
    #
    #     self.mi.title_personal_details()
    #     # assert personal details
    #
    #     self.tb.logout_if_not()
    #
    #     # self.tb.topbar_dropdown()
    #     # self.tb.click_on_item_from_user_menu()  # Logout
    #
    #     self.lp.input_username("orange_user_001")
    #     self.lp.input_password("Test_Password123")
    #     self.lp.click_login_button()
    #
    #     # assert
    #     self.mm.open_main_menu()
    #     self.tb.topbar_name()
    #     self.tb.topbar_header_title()
    #
    #     self.tb.logout_if_not()
    #     self.lp.input_username(self.username_text)
    #     self.lp.input_password(self.password_text)
    #     self.lp.click_login_button()
    #
    #     self.mm.open_main_menu()
    #     self.mm.select_from_main_menu(self.search_pim)
    #
    #     self.pi.pim_page_search_user_by_id()
    #
    #     self.pi.pim_page_table()
    #
    #     self.logger.info("********************* END test_pim_page_add_employee_with_credentials *********************")
    #
    # # test_pim_page_add_employee_without_credentials
