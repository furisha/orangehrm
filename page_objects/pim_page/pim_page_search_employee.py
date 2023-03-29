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


class PIMPageSearchEmployee:

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

    def pim_page_search_user_by_id(self):

        label_employee_id = self.driver.find_element(By.XPATH, self.label_employee_id_xpath)
        assert label_employee_id.is_displayed()
        employee_id_active = self.driver.find_element(
            locate_with(By.XPATH, self.input_employee_id_xpath).below(label_employee_id))
        assert employee_id_active.is_displayed()
        employee_id_active.send_keys("0000")

        button_search = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.button_search_xpath)))

        button_search.click()
        time.sleep(2)

    def pim_page_table_employee_id(self):

        try:
            table_cell_id_first_xpath = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.table_cell_id_first_xpath)))
            assert table_cell_id_first_xpath.text == "0000"
            self.logger.info(table_cell_id_first_xpath.text)
        except Exception as e:
            self.logger.error("table_cell_id_first_xpath failed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

    def pim_page_delete_employee_from_table(self):

        try:
            table_cell_checkbox_first_xpath = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.table_cell_checkbox_first_xpath)))
            assert table_cell_checkbox_first_xpath.is_displayed()
            self.logger.info("click table_cell_checkbox_first_xpath")
            table_cell_checkbox_first_xpath.click()
            # time.sleep(5)
        except Exception as e:
            self.logger.error("click table_cell_checkbox_first_xpath failed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            table_delete_selected = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.button_delete_selected_xpath)))
            assert table_delete_selected.is_displayed()
            self.logger.info("table_delete_selected is displayed")
            table_delete_selected.click()
            self.logger.info("click table_delete_selected")
            # time.sleep(5)
        except Exception as e:
            self.logger.error("table_delete_selected failed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            button_yes_delete = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.button_yes_delete_xpath)))
            assert button_yes_delete.is_displayed()
            self.logger.info("button_yes_delete is displayed")
            button_yes_delete.click()
            self.logger.info("employee successfully deleted")
            # time.sleep(5)
        except Exception as e:
            self.logger.error("button_yes_delete failed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))
