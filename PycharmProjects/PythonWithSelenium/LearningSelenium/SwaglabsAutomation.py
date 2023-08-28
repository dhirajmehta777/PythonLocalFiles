import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
products=driver.find_elements(By.XPATH, "//*[@class='inventory_item_name']")
prd=driver.find_elements(By.XPATH, "//div[@class='pricebar']//preceding-sibling::div//following-sibling::button")
buttons=driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
# for ele in products:
#     if(ele.text=='Sauce Labs Bike Light'):
#         driver.find_element(By.XPATH,"(//button[text()='Add to cart'])[1]").click()
#         break
# print('Thank you for the order')

def add_to_cart(productName):
    for ele in products:
        if (ele.text == productName):

            # def add_to_cart(productName):
            driver.find_element(By.XPATH, f"//*[@id='add-to-cart-{productName}").click()
            time.sleep(3)
        break
print('Thank you for the order')
add_to_cart('Sauce Labs Bolt T-Shirt')
