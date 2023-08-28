import requests
import pytest




def test_get_request_verify_status_code():
    get_response=requests.get("https://reqres.in/api/users?page=2")
    assert get_response.status_code == 200

def test_get_response_headers_content_type():
    get_response = requests.get("https://reqres.in/api/users?page=2")
    print(get_response.headers)
    assert get_response.headers["Content-Type"]=="application/json; charset=utf-8"

def test_to_verify_get_response_body():
    get_response = requests.get("https://reqres.in/api/users?page=2")
    response_body=get_response.json()
    print(response_body["data"][0]["email"])
    assert response_body["total_pages"]==response_body["total_pages"]
    assert isinstance(response_body["total_pages"], int) is True
    assert response_body["data"][0]["email"]=="michael.lawson@reqres.in"

# def test_to_get_size_of_response_body_of_specific_list_element():
#     get_response = requests.get(f"{BASE_URI}/page=2")
#     response_body = get_response.json()
#     assert len(response_body["data"]) == 6










