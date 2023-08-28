import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage():
    LogoOfVtx_Xpath="//*[@id='prompt-logo-center']"
    LoginPage_Description_Xpath="//*[text()='Log in to q-a to continue to Vertex Cloud Platform UI.']"
    Username_Xpath= "//*[@id='username']"
    Usr_Continue_btn_xpath = "//*[contains(@class, 'button-login-id')]"
    Password_Xpath = "//*[@id='password']"
    Pwd_Continue_btn_Xpath="//*[contains(@class, 'button-login-password')]"
    Tax_Categorization_Page_Header="//div[text()='Category Review']"


    def __init__(self, driver):
        self.driver = driver

    def get_login_page_title(self):
        return self.driver.title

    def is_Vtx_logo_exists(self):
        vtx_logo_element = self.driver.find_element(By.XPATH, self.LogoOfVtx_Xpath)
        return bool(vtx_logo_element)

    def is_Vtx_loginpage_description_exists(self):
        vtx_login_description_element = self.driver.find_element(By.XPATH, self.LoginPage_Description_Xpath)
        return bool(vtx_login_description_element)

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.Username_Xpath).send_keys(username)

    def clickOnUsrLoginBtn(self):
        self.driver.find_element(By.XPATH, self.Usr_Continue_btn_xpath).click()

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.Password_Xpath).send_keys(password)

    def clickOnPwdLoginBtn(self):
        self.driver.find_element(By.XPATH, self.Pwd_Continue_btn_Xpath).click()

    def do_login_with_valid_credentials(self,username,password):
        self.setUserName(username)
        self.clickOnUsrLoginBtn()
        self.setPassword(password)
        self.clickOnPwdLoginBtn()

    def verify_tax_categorization_page_header(self):
        wait=WebDriverWait(self.driver,100)
        tc_header=wait.until(ec.visibility_of_element_located((By.XPATH,self.Tax_Categorization_Page_Header)))
        return tc_header.text







