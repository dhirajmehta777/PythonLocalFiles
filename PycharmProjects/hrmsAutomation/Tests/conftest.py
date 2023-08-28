import pytest
from  selenium import webdriver

@pytest.fixture()
def setUp(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching Chrome Browser..........")
    elif browser == ' firefox':
        driver=webdriver.firefox
        print("Launching Firefox Browser..........")
    else:
        driver=webdriver.ie
        print("Launching IE Browser..........")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#To Run:we need to use this command
# pytest -v -s Tests/test_loginPage.py --browser chrome
#To run Parallel
# pytest -v -s -n=2 Tests/test_loginPage.py --browser chrome