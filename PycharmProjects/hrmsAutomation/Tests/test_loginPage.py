import pytest
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig

class TestLoginPage:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    def test_login_page_title(self, setUp):
        self.driver=setUp
        self.driver.get(self.baseURL)
        actual_title = self.driver.title

        if actual_title == "SYNERZIP":
            assert  True
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//" + "login_Page_title.png")
            self.driver.close()
            assert  False

    def test_login(self, setUp):
        self.driver=setUp
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickOnLoginBtn()
        self.driver.close()

