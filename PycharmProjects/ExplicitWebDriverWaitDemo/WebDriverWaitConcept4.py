import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.freshworks.com/")
driver.maximize_window()

wait=WebDriverWait(driver,30)
footer_links=wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR,'ul.footer-nav li')))
print(len(footer_links))
for ele in footer_links:
    print(ele.text)

#there are other methods like
wait.until(ec.frame_to_be_available_and_switch_to_it())
wait.until(ec.element_located_to_be_selected())#this is for dropdowns or checboxes


