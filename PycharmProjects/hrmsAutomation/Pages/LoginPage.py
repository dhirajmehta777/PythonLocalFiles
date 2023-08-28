from selenium.webdriver.common.by import By


class LoginPage:

    Username_Id="txtUsername"
    Password_Id="txtPassword"
    Login_btn_xpath="//*[text()='Login ']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.Username_Id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.Password_Id).send_keys(password)

    def clickOnLoginBtn(self):
        self.driver.find_element(By.XPATH, self.Login_btn_xpath).click()
