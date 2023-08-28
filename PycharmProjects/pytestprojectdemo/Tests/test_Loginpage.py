import  pytest

from Config.config import TestData
from Pages.Loginpage import LoginPage
from Tests.test_base import BaseTest


class Test_Login(BaseTest):

    def test_signinWithGoogle(self):
        self.LoginPage=LoginPage(self.driver)
        flag=self.LoginPage.is_signinWithGoogle_exists()
        assert flag

    def test_login_page_title(self):
        self.LoginPage = LoginPage(self.driver)
        title = self.LoginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title==TestData.LOGIN_PAGE_TITLE

    def test_Login(self):
        self.LoginPage=LoginPage(self.driver)
        self.LoginPage.do_login(TestData.USER_NAME,TestData.PASSWORD)

