import pytest


@pytest.yield_fixture()
def setUp():
    print("once before every method")
    yield
    print("once after every method")

def testMethod5(setUp):
    print("this is test method5")

def testMethod6(setUp):
    print("this is test method6")