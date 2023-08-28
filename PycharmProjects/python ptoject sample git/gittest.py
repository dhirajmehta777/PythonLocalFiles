from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())

# from webdriver_manager.firefox import GeckoDriverManager
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# path = "/home/excellarate/browserdrivers/chromedriver"
# driver= webdriver.Chrome(executable_path=path)

url = "https://hrms.synerzip.in/symfony/web/index.php/auth/login"
driver.get(url)
driver.maximize_window()
print(driver.title)
driver.close()