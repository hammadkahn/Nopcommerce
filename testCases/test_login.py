import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from testCases import confitest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self):
        self.logger.info("************* Test_001_Login *************")
        self.logger.info("************* Verifying Home Page Title *************")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************* Home Page Title Test Passed *************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************* Home Page Title Test Failed *************")
            assert False


    def test_login(self):
        self.logger.info("************* Verifying Login Test *************")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************* Login Test Passed *************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("************* Login Test Failed *************")
            assert False
