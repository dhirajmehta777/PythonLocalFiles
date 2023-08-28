import pytest
"""
Ex4:What is Fixtures in pytest:
prerequsites and initial setups and tear down methods will be controlled by fixtures in pytest.
predefined steps like launchinf browser, nvigating to url and the tear down i.e. closing 
of browser after all the test cases are performed or automated.
These predefined steps will execute before all the tests execution and execution the post condition
will execute that is teardown
command used to run:pytest LearnPyTest/test_cart.py -vs
"""


# @pytest.fixture#here we can use @pytest.yeild_fixture this will also work in the same manner but it
# # is consider as older version so now we use only @pytest.fixture
# def setUp():
#     print("Launch browser")
#     print("Login")
#     print("Browse Products")
#     yield#Here yeild will execute after executing the every tests this will act as tear down method
#     print("LogOff")
#     print("Close Browser")

# def testAddItemtoCart(setUp):#Here the setup method will run before running this method as we
#     # passed the arrgumnet as setUp inside these method which belongs to fixture and if we pass this
#     # fixture method in the remove item then at that time these prerequesites will excute before these remove item method also
#     print("Add Item successfully")
#
# def testRemoveitemfromCart(setUp):
#     print("Remove Item successfully")

def testAddItemtoCart():#here arrgument "setUp" is not passed as we used autouse=True in the fixture
    print("Add Item successfully")

def testRemoveitemfromCart():
    print("Remove Item successfully")