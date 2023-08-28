"""
pytest files should have the format test_*.py or *_test.py and test methods and functions should
start with keyword "test"
"""
import pytest

"""
Ex2:How to execute pytest using command line:
foe example if we want to execute four test files using command line, just right click on project and 
copy teh path of the project into the terminal or direct open the project into the terminal and type 
the command as pytest then it will run all the tests which are present in the project

Simply we need to type a command in the terminal that is "pytest" and press enter
if we want more details then we need to type a command "pytest -v"
if we want to know about different commands just type "pytest --help"
along with passed discription if we want to get the print statement then just type "pytest -v -s"
if we want to execute files having log keyword then just type "pytest LearnPytest/test_checkout.py -vsk log"
"""

"""
Ex3:Grouping Tests in Pytest:
How we can mark the testcases, we have the decorator @pytets.mark.sanity, apply this marker above all 
the sanity methods and try to execute the same with a command that is "pytest -mv sanity" or if we want
to execute only regression testmethods then just type "pytest -mv regression"

To know more about built in markers then just type the command "pytest --markers"
"""


@pytest.mark.skip
def testLogin():
    print("Login successfully")

@pytest.mark.regression
def testLogoff():
    print("Logoff successfully")

@pytest.mark.sanity
def testCalculation():
    assert 2+2==4

@pytest.mark.xfail#If we want to explicitly fail the test then we go for this marker, if you wont i
# mplement this marker then in console it will show it as Failed insteatd of xfail so better to apply this marker
def testCalculation1():
    # assert 2+2==4 here in console it will show "xpass"
    assert 2 + 2 == 5 #here in console it will show "xfail"