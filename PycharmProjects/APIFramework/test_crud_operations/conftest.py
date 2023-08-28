import pytest
import requests

from utilities.read_properties import ReadConfig

@pytest.fixture(scope="function",autouse=True)
def initiate_get_request():
    get_response = requests.get(ReadConfig.getBaseURL() + ReadConfig.getEndPoint())
    return get_response
