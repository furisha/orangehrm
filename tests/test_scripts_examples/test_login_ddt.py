import pytest
from page_objects.login_page import LoginPage
# from utilities.read_authorization_properties import ReadAuthorizationConfig
from utilities.read_properties import ReadLoginConfig
from utilities.custom_logger import LogGen
from utilities import xlutils

import time


# class Test_001_Login:
#     config = ReadLoginConfig()
#     baseURL = config.get_common_info('baseURL')
#     actualURL = config.get_common_info('actualURL')
#     username = config.get_common_info('username')
#     password = config.get_common_info('password')
#     login_page_title = config.get_common_info('login_page_title')
#     dashboard_page_url = config.get_common_info('dashboardURL')

class Test_002_DDT_Login:
    login_config = ReadLoginConfig()
    baseURL = login_config.get_login_info('baseURL')
    # actualURL = login_config.get_login_info('actualURL')
    path = ".//test_data/loginData.xlsx"
    # username = login_config.get_login_info('username')
    # password = login_config.get_login_info('password')
    # login_page_title = login_config.get_login_info('login_page_title')
    # dashboard_page_url = login_config.get_login_info('dashboardURL')

    logger = LogGen.loggen()


    @pytest.fixture(autouse=True)
    def setup_test_script(self):
        yield
        self.driver.quit()


    # def test_homepage_title(self, setup):
    #     self.logger.info("********************* Test_001_Login START *********************")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #
    #     actual_login_url = self.driver.current_url
    #     assert actual_login_url == self.actualURL
    #     self.logger.info("********************* Test URL PASS *********************")
    #     # assert actual_login_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    #
    #     actual_title = self.driver.title
    #     assert actual_title == self.login_page_title
    #     self.logger.info("********************* Test HomePage Title PASS *********************")


    def test_login(self, setup):
        self.logger.info("********************* Login test START *********************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows = xlutils.get_row_count(self.path, 'Sheet1')
        print("Number of Rows i a Excel:", self.rows)

        lst_status = []

        for r in range(2, self.rows+1):
            self.user = xlutils.read_data(self.path, 'Sheet1', r, 1)
            self.password = xlutils.read_data(self.path, 'Sheet1', r, 2)
            self.exp = xlutils.read_data(self.path, 'Sheet1', r, 3)

            self.lp.login_user(self.username, self.password)
            # self.lp.login_user(self.username)
            # self.lp.set_password(self.password)
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "OrangeHRM"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("Passed")
                    self.lp.login_user()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("Failed")
                    self.lp.logout_user()
                    lst_status.append("Fail")

            if act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("Passed")
                    self.lp.login_user()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("Failed")
                    self.lp.logout_user()
                    lst_status.append("Fail")

            if "Fail" not in lst_status:
                self.logger.info("LoginDDT test passed")
                self.driver.close()
                assert True
            else:
                self.logger.info("LoginDDT test failed")
                self.driver.close()
                assert False

            self.logger.info("END")



        # self.lp.login_user(self.username, self.password)
        #
        # actual_dashboard_url = self.driver.current_url
        # assert actual_dashboard_url == self.dashboard_page_url
        # self.logger.info("********************* Test URL PASS *********************")
        # # "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        #
        # actual_title = self.driver.title
        # assert actual_title == self.login_page_title
        # self.logger.info("********************* Test Dashboard Title PASS *********************")
        # self.lp.logout_user()
        # self.logger.info("********************* Logout PASS *********************")

