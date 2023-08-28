import pytest
"""
Ex6:How we can parameterize fixtures and test functions:
this will help us to iterate the test functions in multiple times, we can excute multiple test data at 
once for example if we want test the login page with different sets of data like 
(validusr, validpwd) (validusr, invalidpwd) (invalidusr, validpwd) (invalidusr, invalidpwd) then we go for 
paramiterization
"""
# @pytest.fixture(params=["a","b"])
# def demo_fixture(request):
#     print(request.param)
#
# def testLogin(demo_fixture):
#     print("Login successfully")

@pytest.mark.parametrize("a, b, final",[(2,6,8),(5,8,13),(5,10,15)])
def testAdd(a,b,final):
    assert a+b==final
