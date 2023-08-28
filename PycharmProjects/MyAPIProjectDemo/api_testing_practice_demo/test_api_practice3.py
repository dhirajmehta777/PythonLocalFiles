import requests

def update_post():
    return {
    "name": "morpheus",
    "job": "zion resident"
}

def test_update_request_verify_status_code():
    update_response=requests.put("https://reqres.in/api/users/2",json=update_post())
    print(update_response)
    print(update_response.headers)
    assert update_response.status_code == 200

def test_update_response_headers_content_type():
    update_response=requests.put("https://reqres.in/api/users/2",json=update_post())
    print(update_response.headers)
    assert update_response.headers["Content-Type"]=="application/json; charset=utf-8"

def test_to_verify_update_response_body():
    update_response = requests.put("https://reqres.in/api/users/2", json=update_post())
    print(update_response.json())
    assert isinstance(update_response.json()["name"], str) is True
    assert update_response.json()["name"]=="morpheus"
    assert update_response.json()["job"]=="zion resident"
