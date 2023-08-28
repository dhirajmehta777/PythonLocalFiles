import pytest
import requests
from utilities.read_properties import ReadConfig

class Get_API_Operations():

    # @pytest.fixture(scope="function", autouse=True)
    # def initiate_get_request(self):
    #     get_response = requests.get(ReadConfig.getBaseURL() + ReadConfig.getEndPoint())
    #     return get_response

    def get_request_status_code(self):
        get_response = requests.get(ReadConfig.getBaseURL()+ReadConfig.getEndPoint())
        return get_response.status_code

    def get_response_headers_content_type(self):
        get_response = requests.get(ReadConfig.getBaseURL()+ReadConfig.getEndPoint())
        return get_response.headers["Content-Type"]

    def verify_get_response_body(self):
        get_response = requests.get(ReadConfig.getBaseURL()+ReadConfig.getEndPoint())
        response_body = get_response.json()
        return response_body["data"][0]["email"], response_body["total_pages"]







