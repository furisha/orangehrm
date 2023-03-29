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

from utilities.read_properties import ReadLabelsConfig
from utilities.read_properties import ReadPimElements

import os


def random_generator(size=4, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class PIMPageVisibility:

    label_config = ReadLabelsConfig()
    pim_config = ReadPimElements()
    logger = LogGen.loggen()

    label_employee_name_xpath = label_config.get_labels_info('label_employee_name_xpath')
    label_employee_id_xpath = label_config.get_labels_info('label_employee_id_xpath')
    label_employment_status_xpath = label_config.get_labels_info('label_employment_status_xpath')
    label_include_xpath = label_config.get_labels_info('label_include_xpath')
    label_supervisor_name_xpath = label_config.get_labels_info('label_supervisor_name_xpath')
    label_job_title_xpath = label_config.get_labels_info('label_job_title_xpath')
    label_sub_unit_xpath = label_config.get_labels_info('label_sub_unit_xpath')

    button_add_xpath = pim_config.get_pim_info('button_add_xpath')
    button_search_xpath = pim_config.get_pim_info('button_search_xpath')
    button_delete_selected_xpath = pim_config.get_pim_info('button_delete_selected_xpath')
    button_yes_delete_xpath = pim_config.get_pim_info('button_yes_delete_xpath')

    input_employee_id_xpath = pim_config.get_pim_info('input_employee_id_xpath')

    table_cell_id_first_xpath = pim_config.get_pim_info('table_cell_id_first_xpath')
    table_cell_checkbox_first_xpath = pim_config.get_pim_info('table_cell_checkbox_first_xpath')


    def __init__(self, driver):
        self.driver = driver

    def click_add_button(self):
        button_add = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, self.button_add_xpath)))
        assert button_add.is_displayed()
        button_add.click()
        time.sleep(1)

    def pim_page_visibility(self):

        # Filter / Search

        try:
            label_employee_name = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.label_employee_name_xpath)))
            assert label_employee_name.is_displayed()
            self.logger.info("label_employee_name is displayed")
        except Exception as e:
            self.logger.error("label_employee_name failed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            input_employee_name = self.driver.find_element(
                locate_with(By.TAG_NAME, "input").below(label_employee_name))
            assert input_employee_name.is_displayed()
            self.logger.info("input_employee_name is displayed")
        except Exception as e:
            self.logger.error("input_employee_name is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            label_employee_id = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.label_employee_id_xpath)))
            assert label_employee_id.is_displayed()
            self.logger.info("label_employee_id is displayed")
        except Exception as e:
            self.logger.error("label_employee_id failed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            input_employee_id = self.driver.find_element(
                locate_with(By.TAG_NAME, "input").below(label_employee_id))
            assert input_employee_id.is_displayed()
            self.logger.info("input_employee_id is displayed")
        except Exception as e:
            self.logger.error("input_employee_id is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            label_employment_status = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.label_employment_status_xpath)))
            assert label_employment_status.is_displayed()
            self.logger.info("label_employment_status is displayed")
        except Exception as e:
            self.logger.error("label_employment_status failed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            dd_employee_status = self.driver.find_element(
                locate_with(By.TAG_NAME, "input").below(label_employment_status))
            assert dd_employee_status.is_displayed()
            self.logger.info("dd_employee_status is displayed")
        except Exception as e:
            self.logger.error("dd_employee_status is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            label_include = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.label_include_xpath)))
            assert label_include.is_displayed()
            self.logger.info("label_include is displayed")
        except Exception as e:
            self.logger.error("label_include failed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            dd_include = self.driver.find_element(
                locate_with(By.TAG_NAME, "input").below(label_include))
            assert dd_include.is_displayed()
            self.logger.info("dd_include is displayed")
        except Exception as e:
            self.logger.error("dd_include is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            label_supervisor_name = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.label_supervisor_name_xpath)))
            assert label_supervisor_name.is_displayed()
            self.logger.info("label_supervisor_name is displayed")
        except Exception as e:
            self.logger.error("label_supervisor_name failed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            input_supervisor_name = self.driver.find_element(
                locate_with(By.TAG_NAME, "input").below(label_supervisor_name))
            assert input_supervisor_name.is_displayed()
            self.logger.info("input_supervisor_name is displayed")
        except Exception as e:
            self.logger.error("input_supervisor_name is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            label_job_title = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.label_job_title_xpath)))
            assert label_job_title.is_displayed()
            self.logger.info("label_job_title is displayed")
        except Exception as e:
            self.logger.error("label_job_title failed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            dd_job_title = self.driver.find_element(
                locate_with(By.TAG_NAME, "input").below(label_job_title))
            assert dd_job_title.is_displayed()
            self.logger.info("dd_job_title is displayed")
        except Exception as e:
            self.logger.error("dd_job_title is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            label_sub_unit = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.label_sub_unit_xpath)))
            assert label_sub_unit.is_displayed()
            self.logger.info("label_sub_unit is displayed")
        except Exception as e:
            self.logger.error("label_sub_unit failed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            dd_sub_unit = self.driver.find_element(
                locate_with(By.TAG_NAME, "input").below(label_sub_unit))
            assert dd_sub_unit.is_displayed()
            self.logger.info("dd_sub_unit is displayed")
        except Exception as e:
            self.logger.error("dd_sub_unit is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        # Table
