from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.Basepage import BasePage


class LoginPage(BasePage):

    SignInWithGoogle=(By.XPATH,"//a[text()='Sign in with Google']")
    UsrName=(By.ID,"txtUsername")
    Password=(By.ID,"txtPassword")
    LoginBtn=(By.XPATH,"//*[text()='Login ']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self,title):
        return self.get_title(title)

    def is_signinWithGoogle_exists(self):
        return self.is_visible(self.SignInWithGoogle)

    def do_login(self, username, password):
        self.do_send_Key(self.UsrName, username)
        self.do_send_Key(self.Password, password)
        self.do_click(self.LoginBtn)
