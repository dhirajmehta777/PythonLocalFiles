import requests
from utilities.read_properties import ReadConfig
from utilities.post_payload import Post_API_Payload

class Post_API_Operations():

    def post_request_verify_status_code(self):
        post_response = requests.post(ReadConfig.getBaseURL()+ReadConfig.postEndPoint(), json=Post_API_Payload.create_post())
        return post_response.status_code

    def post_response_headers_content_type(self):
        post_response = requests.post(ReadConfig.getBaseURL()+ReadConfig.postEndPoint(), json=Post_API_Payload.create_post())
        return post_response.headers["Content-Type"]

    def to_verify_post_response_body(self):
        post_response = requests.post(ReadConfig.getBaseURL()+ReadConfig.postEndPoint(), json=Post_API_Payload.create_post())
        post_response_body=post_response.json()
        return post_response_body["name"],post_response_body["job"]