import pytest


@pytest.yield_fixture()
def setUp():
    print("Opening URL to signup")
    yield
    print("closing browser after signup")

def test_signupByemail(setUp):
    print("this is signingup by email test")

def test_signupByfacebook(setUp):
    print("this is signingup by facebook test")

"""
If we want to run a specific test method then we have this command:
pytest -v -s test_SignUp.py::test_signupByfacebook
If we want to run all the modules present in a package at a time the we have this command
cd MyPack
pytest -v -s
If we want to run specific module the we have command
pytest -v -s MyPack/test_SignUp.py
"""