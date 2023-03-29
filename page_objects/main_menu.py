import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver import ActionChains
from selenium.webdriver import Keys

from utilities.read_properties import ReadMainMenuElements

from utilities.custom_logger import LogGen


class MainMenu:
    logger = LogGen.loggen()

    load_main_menu_elements = ReadMainMenuElements()

    search_input_xpath = load_main_menu_elements.get_main_menu_info('search_input_xpath')
    search_input_class_name = load_main_menu_elements.get_main_menu_info('search_input_class_name')
    chevron_left_class_name = load_main_menu_elements.get_main_menu_info('chevron_left_class_name')
    chevron_right_class_name = load_main_menu_elements.get_main_menu_info('chevron_right_class_name')
    main_menu_item_name = load_main_menu_elements.get_main_menu_info('main_menu_item_name')

    def __init__(self, driver):
        self.driver = driver

    def open_main_menu(self):
        chevron_left = self.driver.find_element(By.CLASS_NAME, self.chevron_left_class_name)
        try:
            if chevron_left.is_displayed():
                assert chevron_left.is_displayed()
                self.logger.info("chevron_left is displayed")
            else:
                chevron_right = self.driver.find_element(By.CLASS_NAME, self.chevron_right_class_name)
                assert chevron_right.is_displayed()
                chevron_right.click()
                self.logger.info("chevron_right is displayed and clicked")
        except Exception as e:
            self.logger.error("chevron is not displayed")
            raise Exception("Message: {}".format(str(e)))

    def search_main_menu(self, menu_item):
        try:
            main_menu_items_counter = self.driver.find_elements(By.CLASS_NAME, self.main_menu_item_name)
            self.driver.find_element(By.CLASS_NAME, self.search_input_class_name).send_keys(menu_item)
            for menu_items in main_menu_items_counter:
                if menu_items.text == menu_item:
                    menu_items.click()
                    self.logger.info("selected : " + menu_item + " from main menu")
                    break
        except Exception as e:
            self.logger.error("chevron is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

    def search_main_menu_empty(self):
        search_main_menu = self.driver.find_element(By.CLASS_NAME, self.search_input_class_name)
        search_main_menu.send_keys("random")
        main_menu_items_counter = self.driver.find_elements(By.CLASS_NAME, self.main_menu_item_name)
        if len(main_menu_items_counter) == 0:
            self.logger.info("no items in the main menu list")
            assert len(main_menu_items_counter) == 0
        else:
            self.logger.error("main menu has items in the list")

    def select_from_main_menu(self, menu_item):
        try:
            main_menu_items_counter = self.driver.find_elements(By.CLASS_NAME, self.main_menu_item_name)
            for menu_items in main_menu_items_counter:
                if menu_items.text == menu_item:
                    menu_items.click()
                    self.logger.info("selected : " + menu_item + " from main menu")
                    break
        except Exception as e:
            self.logger.error("menu_item is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

    def delete_text_from_main_menu_search(self):
        search_input_xpath = self.driver.find_element(By.XPATH, self.search_input_xpath)
        act = ActionChains(self.driver)
        act.double_click(search_input_xpath).perform()
        act.key_down(Keys.DELETE)
        act.perform()
        self.logger.info("delete_text_from_main_menu_search - pass")
