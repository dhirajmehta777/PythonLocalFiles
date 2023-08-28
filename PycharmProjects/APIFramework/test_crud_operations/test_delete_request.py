from http import HTTPStatus
from crud_operations.delete_request import Delete_API_Operations

class Test_delete_api_operations():

    def test_delete_request_operations(self):
        delete_api=Delete_API_Operations()
        assert delete_api.delete_request_status_code() == HTTPStatus.NO_CONTENT
