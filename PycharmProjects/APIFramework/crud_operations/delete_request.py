import requests
from utilities.read_properties import ReadConfig

class Delete_API_Operations():

    def delete_request_status_code(self):
        delete_response = requests.delete(ReadConfig.getBaseURL()+ReadConfig.deleteEndPoint())
        return delete_response.status_code