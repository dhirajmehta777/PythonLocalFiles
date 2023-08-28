"""
Run the following command to install pytest:
pip install -U pytest
Check for pytest version:
pytest --version
"""
import pytest

"""
Create your first test:
Create a new file called test_sample.py containing a function and a test
"""
def func(x):
    return x+1

def test_answer():
    assert func(3)==4

"""
Note:We can use the assert statement to verify the test expectations
"""
"""
Run multiple tests:pytest will run all files of the form test_*.py or *_test.py
"""
"""
Assert that a certain exception is raised
"""
def test_case01():
    with pytest.raises(Exception):
        assert (1/0)

def func1():
    raise ValueError("Exception func1 raised")

def test_case02():
    with pytest.raises(Exception) as excinfo:
        #assert (1,2,3)==(1,2,4)
    #print(excinfo)
        func1()
    print(str(excinfo))
    assert (str(excinfo.value))=='Exception func1 raised'

"""
Ex2:raised exception
"""
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()

"""
Group multiple tests in calss:
"""
class TestClass:
    def test_one(self):
        x="this"
        assert "h" in x

    def test_two(self):
        x="hello"
        assert hasattr(x,"hello")
