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
from utilities.read_properties import ReadMyInfoConfig

import os


def random_generator(size=4, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class MyInfoPage:

    logger = LogGen.loggen()

    my_info_configuration = ReadMyInfoConfig()

    personal_details_title_xpath = my_info_configuration.get_my_info_info('personal_details_title_xpath')
    personal_details_employee_name_xpath = my_info_configuration.get_my_info_info('personal_details_employee_name_xpath')

    def __init__(self, driver):
        self.driver = driver

    def title_personal_details(self):
        title_personal_details = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.personal_details_title_xpath)))
        assert title_personal_details.is_displayed()
        self.logger.info("title_personal_details is displayed")

