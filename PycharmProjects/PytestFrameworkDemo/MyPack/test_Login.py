import pytest


@pytest.yield_fixture()
def setUp():
    print("Opening URL to login")
    yield
    print("closing browser after login")

def test_loginByemail(setUp):
    print("this is login by email test")

def test_loginByfacebook(setUp):
    print("this is login by facebook test")