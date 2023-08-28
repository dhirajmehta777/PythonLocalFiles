from http import HTTPStatus
from crud_operations.post_request import Post_API_Operations

class Test_post_api_operations():

    def test_post_request_operations(self):
        post_api=Post_API_Operations()
        assert post_api.post_request_verify_status_code() == HTTPStatus.CREATED
        assert post_api.post_response_headers_content_type()=="application/json; charset=utf-8"
        assert post_api.to_verify_post_response_body()==("morpheus","leader")