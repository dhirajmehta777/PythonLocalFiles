import requests
import pytest
from utilities.readproperties import ReadConfig

def test_get_request_verify_status_code():
    print(ReadConfig.getBaseURL())
    get_response=requests.get(ReadConfig.getBaseURL())
    assert get_response.status_code == 200

# def test_get_response_headers_content_type():
#     get_response = requests.get("https://reqres.in/api/users?page=2")
#     print(get_response.headers)
#     assert get_response.headers["Content-Type"]=="application/json; charset=utf-8"
#
# def test_to_verify_get_response_body():
#     get_response = requests.get("https://reqres.in/api/users?page=2")
#     response_body=get_response.json()
#     print(response_body["data"][0]["email"])
#     assert response_body["total_pages"]==response_body["total_pages"]
#     assert isinstance(response_body["total_pages"], int) is True
#     assert response_body["data"][0]["email"]=="michael.lawson@reqres.in"