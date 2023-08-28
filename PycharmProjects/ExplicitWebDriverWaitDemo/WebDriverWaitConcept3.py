import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://app.hubspot.com/login")
driver.maximize_window()

wait=WebDriverWait(driver,10)
signUp_link=wait.until(ec.element_to_be_clickable((By.LINK_TEXT,'Sign up')))
print(signUp_link.text)
signUp_link.click()
time.sleep(10)

first_name=wait.until(ec.visibility_of_element_located((By.ID,'uid-firstName-5')))
first_name.send_keys('naveen')
#here the diff between presence of element and visibility of element is:
#presence of element is weather the element is present inside the DOM
#Visiblity is the element is visible on the page as well as present inside the DOM which is having some height annd width
