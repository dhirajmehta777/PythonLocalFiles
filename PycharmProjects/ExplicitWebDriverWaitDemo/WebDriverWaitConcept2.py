import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()
driver.find_element(By.NAME,'proceed').click()
time.sleep(20)
wait=WebDriverWait(driver,30)
alert=wait.until(ec.alert_is_present())
print(alert.text)
alert.accept()
driver.close()
