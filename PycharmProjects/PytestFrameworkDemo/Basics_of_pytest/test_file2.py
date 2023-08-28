#How to work with pytest fixtures:
#the purpose of test fixtures is to provide a fixed baseline upon which test can reliably and repeatedly execute
import pytest
"""
@pytest.fixture():Executes specific method before every test method
@pytest.yield_fixture():Executes specific test method before and after every test method
"""

@pytest.fixture()
def setUp():
    print("once before every method")

def testMethod3(setUp):
    print("this is test method3")

def testMethod4(setUp):
    print("this is test method4")