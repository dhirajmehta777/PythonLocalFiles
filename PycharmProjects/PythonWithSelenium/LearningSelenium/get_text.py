import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager



driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://hrms.synerzip.in/symfony/web/index.php/auth/login")
driver.maximize_window()
driver.find_element(By.ID, "txtUsername").send_keys("dhiraj.mehta")
driver.find_element(By.ID, "txtPassword").send_keys("Mehta@91")
driver.find_element(By.XPATH, "//*[text()='Login ']").click()
driver.find_element(By.XPATH, "//*[@id='menu_pim_viewDirectory']").click()
job_title_element=driver.find_element(By.XPATH, "//*[@id='empDir_job_title']")
drp_job_title = Select(job_title_element)
drp_job_title.select_by_visible_text("Lead QA Engineer")
business_unit_element = driver.find_element(By.XPATH, "//*[@id='empDir_sub_unit']")
drp_job_title = Select(business_unit_element)
drp_job_title.select_by_visible_text("BU-7 (Mukund Rajamannar)")
driver.find_element(By.XPATH, "//*[@id='searchBtn']").click()
time.sleep(10)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(10)
element=driver.find_elements(By.XPATH,"//table[@id='resultTable']//tbody//tr//td[2]//span[text()='Designation: ']")
for e in element:
    print(e.text)