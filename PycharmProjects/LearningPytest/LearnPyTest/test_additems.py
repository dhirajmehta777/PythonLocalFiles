"""
pytest files should have the format test_*.py or *_test.py and test methods and functions should
start with keyword "test"
"""
import pytest


@pytest.mark.sanity
def testLogin():
    print("Login successfully")

def testLogoff():
    print("Logoff successfully")

def testCalculation():
    assert 2+2==4