from pytest import fixture
from pytest import mark

@fixture()
def connect_db():
    print("I need to connect to employee database")
    yield
    print("I need to disconnect to employee database")
#@mark.fixture_example
def test_first(connect_db):

    print("I am first test to verify employee name against id")


#@mark.fixture_example
def test_second(connect_db):
    #print("I need to connect to employee database")
    print("I am second test to verify employee id against department")
    #print("I need to disconnect to employee database")

@mark.fixture_example
def test_third(connect_db):
    #print("I need to connect to employee database")
    print("I am third test to verify employee id against supervisor")
    #print("I need to disconnect to employee database")
