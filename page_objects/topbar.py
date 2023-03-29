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


class TopBar:

    logger = LogGen.loggen()
    login_config = ReadLoginConfig()

    topbar_config = ReadTopBarConfig()

    topbar_title_header = topbar_config.get_topbar_info('topbar_title_header_xpath')
    topbar_user_dropdown_xpath = topbar_config.get_topbar_info('topbar_user_dropdown_xpath')
    topbar_user_dropdown_menu_xpath = topbar_config.get_topbar_info('topbar_user_dropdown_menu_xpath')
    topbar_menu_item_xpath = topbar_config.get_topbar_info('topbar_menu_item_xpath')
    topbar_menu_item_name_xpath = topbar_config.get_topbar_info('topbar_menu_item_name_xpath')
    topbar_header_title_xpath = topbar_config.get_topbar_info('topbar_header_title_xpath')

    login_title_class_name = login_config.get_login_info('login_title_class_name')

    def __init__(self, driver):
        self.driver = driver

    def topbar_name(self):
        try:
            topbar_menu_item_name = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.topbar_menu_item_name_xpath)))
            assert topbar_menu_item_name.text == "orange last"
            self.logger.info("topbar_menu_item_name is: " + topbar_menu_item_name.text)
        except Exception as e:
            self.logger.error("topbar_menu_item_name is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

    def topbar_header_title(self):
        try:
            topbar_header_title = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.topbar_header_title_xpath)))
            assert topbar_header_title.text == "Dashboard"
        except Exception as e:
            self.logger.error("topbar_header_title is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

    def topbar_dropdown(self):
        try:
            topbar_user_dropdown_xpath = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.topbar_user_dropdown_xpath)))
            assert topbar_user_dropdown_xpath.is_displayed()
            topbar_user_dropdown_xpath.click()
            time.sleep(2)
            self.logger.info("click topbar_user_dropdown_xpath")
        except Exception as e:
            self.logger.error("topbar_user_dropdown_xpath is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

    def click_on_item_from_user_menu(self):
        try:
            topbar_menu_item_xpath = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.topbar_menu_item_xpath)))

            topbar_menu_item_xpath_counter = self.driver.find_elements(By.XPATH, self.topbar_menu_item_xpath)
            for menu_items in topbar_menu_item_xpath_counter:
                if menu_items.text == "Logout":
                    menu_items.click()
                    time.sleep(5)
                    self.logger.info("click Logout")
                    break
        except Exception as e:
            self.logger.error("topbar_menu_item Logout is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

    def logout_if_not(self):
        topbar_user_dropdown_xpath_counter = self.driver.find_elements(By.XPATH, self.topbar_user_dropdown_xpath)
        if len(topbar_user_dropdown_xpath_counter) == 0:
            self.logger.info("Login page")
            assert len(topbar_user_dropdown_xpath_counter) == 0
        else:
            topbar_user_dropdown_xpath = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.topbar_user_dropdown_xpath)))
            topbar_user_dropdown_xpath.click()
            topbar_user_dropdown_menu_xpath = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.topbar_user_dropdown_menu_xpath)))

            topbar_menu_item_xpath_counter = self.driver.find_elements(By.XPATH, self.topbar_menu_item_xpath)
            for menu_items in topbar_menu_item_xpath_counter:
                if menu_items.text == "Logout":
                    menu_items.click()
                    self.logger.info("click Logout")



        # topbar_user_dropdown_xpath = self.driver.find_element(By.XPATH, self.topbar_user_dropdown_xpath)
        # if topbar_user_dropdown_xpath.is_displayed():
        #     assert topbar_user_dropdown_xpath.is_displayed()
        #     self.logger.info("topbar_user_dropdown_xpath is displayed")
        #     topbar_user_dropdown_xpath.click()
        #     # topbar_menuitem_xpath = WebDriverWait(self.driver, 20).until(
        #     #     ec.visibility_of_element_located((By.XPATH, self.topbar_menuitem_xpath)))
        #     topbar_menuitem_xpath_counter = self.driver.find_elements(By.XPATH, self.topbar_menuitem_xpath)
        #     for menu_items in topbar_menuitem_xpath_counter:
        #         if menu_items.text == "Logout":
        #             # time.sleep(5)
        #             self.logger.info("click Logout")
        #             # break
        # else:
        #     # login_title_class_name = self.driver.find_element(By.CLASS_NAME, self.login_title_class_name)
        #     # assert login_title_class_name.is_displayed()
        #     self.logger.info("login_title_class_name is displayed")
        # topbar_user_dropdown_xpath = WebDriverWait(self.driver, 20).until(
        #     ec.visibility_of_element_located((By.XPATH, self.topbar_user_dropdown_xpath)))
        # if
        #     topbar_user_dropdown_xpath.is_displayed()
        #     topbar_user_dropdown_xpath.click()
        #     time.sleep(2)
        #     self.logger.info("click topbar_user_dropdown_xpath")
        #     topbar_menuitem_xpath = WebDriverWait(self.driver, 20).until(
        #         ec.visibility_of_element_located((By.XPATH, self.topbar_menuitem_xpath)))
        #     topbar_menuitem_xpath_counter = self.driver.find_elements(By.XPATH, self.topbar_menuitem_xpath)
        #     for menu_items in topbar_menuitem_xpath_counter:
        #         if menu_items.text == "Logout":
        #             menu_items.click()
        #             time.sleep(5)
        #             self.logger.info("click Logout")
        #             # assert self.login_title_class_name.is_displayed()
        #             # self.logger.info("I'm on Login page")
        #             # time.sleep(5)
        #             break
        # try:
        #     topbar_menuitem_xpath = WebDriverWait(self.driver, 20).until(
        #         ec.visibility_of_element_located((By.XPATH, self.topbar_menuitem_xpath)))
        #
        #     topbar_menuitem_xpath_counter = self.driver.find_elements(By.XPATH, self.topbar_menuitem_xpath)
        #     for menu_items in topbar_menuitem_xpath_counter:
        #         if menu_items.text == "Logout":
        #             menu_items.click()
        #             time.sleep(5)
        #             self.logger.info("click Logout")
        #             # assert self.login_title_class_name.is_displayed()
        #             # self.logger.info("I'm on Login page")
        #             # time.sleep(5)
        #             break
        # except Exception as e:
        #     self.logger.error("topbar_menu_item Logout is not displayed", exc_info=True)
        #     raise Exception("Message: {}".format(str(e)))
