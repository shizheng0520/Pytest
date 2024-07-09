import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pageobject.login_page import LoginPage
from config.config import url, driver_path, system_version
from log.log import logger
from data.data import ReadWrite
from time import sleep

class LoginCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Service(executable_path = driver_path)
        cls.driver = webdriver.Chrome(service=0)
        cls.driver.maximize_window()
        cls.driver.get(url)
        cls.loginpage = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
       
    def test_1(self):
        '''
        登录有效的用户名和密码
        '''
        user_list = ReadWrite().excelread('users')
        username = user_list[0][0]
        password = user_list[0][1]
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.click_login()
        self.loginpage.click_logout()
        sleep(2)
        logger.info('登录成功')
        # except:
        #     print('登录页面不显示')

    # @unittest.skipIf(system_version == '1.1', reason = '只有版本号为1.2才执行')
    # def test_2(self):
    #     '''
    #     登录无效的用户名和密码
    #     '''
    #     user_list = ReadWrite().excelread('users')
    #     username = user_list[0][0]
    #     self.loginpage.input_username(username)
    #     self.loginpage.click_login()
    #     sleep(3)
    #     alert_login = self.driver.switch_to.alert
    #     alert_login.accept()
 