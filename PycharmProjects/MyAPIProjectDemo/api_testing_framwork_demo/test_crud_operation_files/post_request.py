import requests

def create_post():
    return {
    "name": "morpheus",
    "job": "leader"
}

def test_post_request_verify_status_code():
    post_response=requests.post("https://reqres.in/api/users",json=create_post())
    print(post_response.headers)
    assert post_response.status_code == 201

def test_post_response_headers_content_type():
    post_response=requests.post("https://reqres.in/api/users",json=create_post())
    print(post_response.headers)
    assert post_response.headers["Content-Type"]=="application/json; charset=utf-8"

def test_to_verify_post_response_body():
    post_response = requests.post("https://reqres.in/api/users", json=create_post())
    print(post_response.json())
    assert isinstance(post_response.json()["id"], str) is True
    assert isinstance(post_response.json()["name"], str) is True
    assert post_response.json()["name"]=="morpheus"
    assert post_response.json()["job"]=="leader"