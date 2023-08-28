import time

from selenium.webdriver.common.by import By

class VtxLoginPage():
    LogoOfVtx_Xpath="//*[@id='prompt-logo-center']"
    Email_Address_Xpath = "//*[@id='username']"
    Password_Xpath = "//*[@id='password']"
    Continue_btn_Xpath="//*[text()='Continue']"

    def __init__(self, driver):
        self.driver = driver

    def get_vtx_login_page_title(self):
        return self.driver.title

    def is_vtx_logo_exists(self):
        vtx_logo_element = self.driver.find_element(By.XPATH, self.LogoOfVtx_Xpath)
        return bool(vtx_logo_element)

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.Email_Address_Xpath).send_keys(username)

    def click_On_ContinueBtn(self):
        self.driver.find_element(By.XPATH, self.Continue_btn_Xpath).click()

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.Password_Xpath).send_keys(password)

    def do_Vtx_login_with_valid_credentials(self,username,password):
        self.setUserName(username)
        self.click_On_ContinueBtn()
        self.setPassword(password)
        self.click_On_ContinueBtn()
        # time.sleep(10)
