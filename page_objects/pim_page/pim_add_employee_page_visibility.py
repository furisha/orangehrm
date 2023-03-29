import time
import pytest
import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.relative_locator import locate_with

from selenium.webdriver import ActionChains
from selenium.webdriver import Keys

from utilities.custom_logger import LogGen
from utilities.read_properties import ReadLoginConfig
from utilities.read_properties import ReadMainMenuElements
from utilities.read_properties import ReadTopBarConfig
from utilities.read_properties import ReadLabelsConfig
from utilities.read_properties import ReadPimElements

import os


class PIMAddEmployeePageVisibility:

    logger = LogGen.loggen()
    login_config = ReadLoginConfig()
    main_menu_elements = ReadMainMenuElements()
    pim_elements = ReadPimElements()
    label_config = ReadLabelsConfig()
    topbar_config = ReadTopBarConfig()

    base_url = login_config.get_login_info('base_url')
    username_text = login_config.get_login_info('username_text')
    password_text = login_config.get_login_info('password_text')
    login_title_class_name = login_config.get_login_info('login_title_class_name')

    search_pim = main_menu_elements.get_main_menu_info('txt_main_menu_pim')

    button_add_xpath = pim_elements.get_pim_info('button_add_xpath')
    button_cancel_xpath = pim_elements.get_pim_info('button_cancel_xpath')
    button_save_xpath = pim_elements.get_pim_info('button_save_xpath')

    password_hint_xpath = pim_elements.get_pim_info('password_hint_xpath')

    input_first_name_xpath = pim_elements.get_pim_info('input_first_name_xpath')
    input_middle_name_xpath = pim_elements.get_pim_info('input_middle_name_xpath')
    input_lastname_xpath = pim_elements.get_pim_info('input_lastname_xpath')
    input_employee_id_xpath = pim_elements.get_pim_info('input_employee_id_xpath')

    label_employee_id_xpath = label_config.get_labels_info('label_employee_id_xpath')
    label_username_xpath = label_config.get_labels_info('label_username_xpath')
    label_password_xpath = label_config.get_labels_info('label_password_xpath')
    label_confirm_password_xpath = label_config.get_labels_info('label_confirm_password_xpath')
    label_status_xpath = label_config.get_labels_info('label_status_xpath')
    label_enabled_xpath = label_config.get_labels_info('label_enabled_xpath')
    label_disabled_xpath = label_config.get_labels_info('label_disabled_xpath')

    topbar_title_header = topbar_config.get_topbar_info('topbar_title_header_xpath')
    topbar_user_dropdown_xpath = topbar_config.get_topbar_info('topbar_user_dropdown_xpath')
    topbar_user_dropdown_menu_xpath = topbar_config.get_topbar_info('topbar_user_dropdown_menu_xpath')
    topbar_menu_item_xpath = topbar_config.get_topbar_info('topbar_menu_item_xpath')
    topbar_menu_item_name_xpath = topbar_config.get_topbar_info('topbar_menu_item_name_xpath')

    def __init__(self, driver):
        self.driver = driver

    def add_employee_page_visibility(self):

        profile_photo = self.driver.find_element(By.XPATH, "//input[@type='file']")
        profile_photo.send_keys("/Users/vfurman/test_profile.jpeg")

        first_name = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, self.input_first_name_xpath)))
        assert first_name.is_displayed()

        middle_name = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, self.input_middle_name_xpath)))
        assert middle_name.is_displayed()

        last_name = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, self.input_lastname_xpath)))
        assert last_name.is_displayed()

        label_employee_id = self.driver.find_element(By.XPATH, self.label_employee_id_xpath)
        assert label_employee_id.is_displayed()
        print(label_employee_id.text)
        employee_id_active = self.driver.find_element(
            locate_with(By.XPATH, self.input_employee_id_xpath).below(label_employee_id))
        assert employee_id_active.is_displayed()

        checkbox_create_login_details = self.driver.find_element(By.CLASS_NAME, "oxd-switch-input--active")
        try:
            if checkbox_create_login_details.is_displayed():
                checkbox_create_login_details.click()
                time.sleep(1)
        except Exception as e:
            self.logger.error("checkbox is not displayed")
            raise Exception("Message: {}".format(str(e)))

        # Label Username
        try:
            label_username_xpath = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.label_username_xpath)))
            assert label_username_xpath.is_displayed()
            self.logger.info("label_username_xpath is displayed")
        except Exception as e:
            self.logger.error("input_username failed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        # Label Password
        try:
            label_password_xpath = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.label_password_xpath)))
            assert label_password_xpath.is_displayed()
            self.logger.info("label_password_xpath is displayed")
        except Exception as e:
            self.logger.error("label_password_xpath failed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        # Confirm Password Label
        try:
            label_confirm_password_xpath = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.label_confirm_password_xpath)))
            assert label_confirm_password_xpath.is_displayed()
            self.logger.info("label_confirm_password_xpath is displayed")
        except Exception as e:
            self.logger.error("label_confirm_password_xpath failed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        # Status
        user_status_label = self.driver.find_element(By.XPATH, self.label_status_xpath)
        assert user_status_label.is_displayed()

        label_enabled_xpath = self.driver.find_element(By.XPATH, self.label_enabled_xpath)
        assert label_enabled_xpath.is_displayed()
        try:
            label_enabled = self.driver.find_element(
                locate_with(By.TAG_NAME, "input").below(label_enabled_xpath))  # 1 input below label username
            assert label_enabled.is_displayed()
            self.logger.info("label_enabled is displayed")
        except Exception as e:
            self.logger.error("label_enabled is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        label_disabled_xpath = self.driver.find_element(By.XPATH, self.label_disabled_xpath)
        assert label_disabled_xpath.is_displayed()
        try:
            label_disabled = self.driver.find_element(
                locate_with(By.TAG_NAME, "input").below(label_disabled_xpath))  # 1 input below label username
            assert label_disabled.is_displayed()
            self.logger.info("label_disabled is displayed")
        except Exception as e:
            self.logger.error("label_disabled is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        radio_button_disabled_checkbox = self.driver.find_element(By.XPATH, "//label[normalize-space()='Disabled']//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input']")
        assert radio_button_disabled_checkbox.is_displayed()
        label_disabled_xpath.click()
        self.logger.info("radio_button_disabled_checkbox is clicked")

        password_hint = self.driver.find_element(By.XPATH, self.password_hint_xpath).text
        assert password_hint == "For a strong password, please use a hard to guess combination of text with upper and lower case characters, symbols and numbers"

        try:
            save_button = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.button_save_xpath)))
            assert save_button.text == "Save"
            self.logger.info("save_button is displayed")
        except Exception as e:
            self.logger.error("save_button is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))
