from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://app.hubspot.com/login")
driver.maximize_window()

wait=WebDriverWait(driver,30)
#wait.until(ec.title_is('HubSpot Login'))
wait.until(ec.title_contains('HubSpot'))
print(driver.title)

email_id=wait.until(ec.presence_of_element_located((By.ID,'username')))
email_id.send_keys('test@gmail.com')
#here presence of element means weather that element is present inside the dom or not
