from http import HTTPStatus
from crud_operations.put_request import Put_API_Operations

class Test_put_api_operations():

    def test_put_request_operations(self):
        put_api=Put_API_Operations()
        assert put_api.put_request_verify_status_code() == HTTPStatus.OK
        assert put_api.put_response_headers_content_type()=="application/json; charset=utf-8"
        assert put_api.to_verify_put_response_body()==("morpheus","zion resident")