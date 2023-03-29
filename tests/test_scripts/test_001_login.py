import time
import pytest
import time
import allure
import random
from selenium import webdriver

# from page_objects.login_page import LoginPage

from page_objects.login_page.login_page_visibility import LoginPageVisibility
from page_objects.login_page.login_page_error_messages import LoginPageErrorMessages
from page_objects.login_page.login import Login

from utilities.read_properties import ReadLoginConfig
from utilities.read_properties import ReadUrl

from utilities.custom_logger import LogGen


class TestLogin:

    login_config = ReadLoginConfig()
    logger = LogGen.loggen()
    url_config = ReadUrl()

    url_base = url_config.get_url_info('url_base')
    url_login = url_config.get_url_info('url_login')
    url_index = url_config.get_url_info('url_index')

    txt_admin_username = login_config.get_login_info('txt_admin_username')
    txt_admin_password = login_config.get_login_info('txt_admin_password')

    @pytest.fixture(autouse=False)
    def setup_test_script(self):
        yield
        self.driver.quit()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_page_visibility(self, setup):
        self.logger.info("test_login_page_visibility *** START")
        self.driver = setup
        self.driver.get(self.url_base)

        self.lpv = LoginPageVisibility(self.driver)
        self.lpv.check_url(self.url_login)
        self.lpv.login_page_visibility()
        self.logger.info("test_login_page_visibility *** END")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_page_error_messages(self, setup):
        self.logger.info("test_login_page_error_messages *** START")
        self.driver = setup
        self.driver.get(self.url_base)

        self.li = Login(self.driver)
        self.lpem = LoginPageErrorMessages(self.driver)

        self.li.click_login_button()

        self.lpem.message_invalid_required_username()
        self.lpem.message_invalid_required_password()

        self.lpem.input_random_username()
        self.lpem.input_random_password()

        self.li.click_login_button()

        self.lpem.message_invalid_credentials()

        self.logger.info("test_login_page_error_messages *** END")

        # continue... (add more error messages)

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("test_login *** START")
        self.driver = setup
        self.driver.get(self.url_base)

        self.li = Login(self.driver)

        self.li.input_username(self.txt_admin_username)
        self.li.input_password(self.txt_admin_password)
        self.li.click_login_button()
        self.li.check_url(self.url_index)

        self.logger.info("test_login *** START")
