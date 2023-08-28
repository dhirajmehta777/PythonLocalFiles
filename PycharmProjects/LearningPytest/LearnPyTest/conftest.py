"""
Ex5:How to use Conftest.py in pytest:
its a test configuration file that can be having the common modules or common methods that will be
utilised by all your test cases,
here we can separate commonly used methods and move them into conftest.py file
"""
import pytest
"""
scope="session":
scope="function":
scope="class":
scope="module":
scope="package":
"""

# @pytest.fixture(scope="function",autouse=True)#here we can use @pytest.yeild_fixture this will also work in the same manner but it
# # is consider as older version so now we use only @pytest.fixture
# #here the importance of autouse =True is bydefault the fixture will be called before all the tests and
# # there is no need to pass an argument as "setUp" in every test method
# def setUp():
#     print("Launch browser")
#     print("Login")
#     print("Browse Products")
#     yield#Here yeild will execute after executing the every tests this will act as tear down method
#     print("LogOff")
#     print("Close Browser")

@pytest.fixture(scope="session",autouse=True)
def setUp(browser):
    if browser=="chrome":
        print("Launch browser")
    elif browser == "ff":
        print("Launch firefox")
    else:
        print("provide valid browser")
    print("Login")
    print("Browse Products")
    yield#Here yeild will execute after executing the every tests this will act as tear down method
    print("LogOff")
    print("Close Browser")

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

#command to run:pytest -v -s --browser chrome