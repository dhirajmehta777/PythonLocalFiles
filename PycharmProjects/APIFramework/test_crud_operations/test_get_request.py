from http import HTTPStatus

import pytest

from crud_operations import get_request
from crud_operations.get_request import Get_API_Operations


class Test_get_api_operations():

    def test_get_request_operations(self):
        get_api=Get_API_Operations()
        assert get_api.get_request_status_code() == HTTPStatus.OK
        assert get_api.get_response_headers_content_type()=="application/json; charset=utf-8"
        assert get_api.verify_get_response_body()==("michael.lawson@reqres.in",2)








