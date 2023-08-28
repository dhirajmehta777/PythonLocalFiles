import requests
from utilities.put_payload import Put_API_Payload
from utilities.read_properties import ReadConfig

class Put_API_Operations():

    def put_request_verify_status_code(self):
        put_response = requests.put(ReadConfig.getBaseURL()+ReadConfig.putEndPoint(), json=Put_API_Payload.update_post())
        return put_response.status_code

    def put_response_headers_content_type(self):
        put_response = requests.put(ReadConfig.getBaseURL()+ReadConfig.putEndPoint(), json=Put_API_Payload.update_post())
        return put_response.headers["Content-Type"]

    def to_verify_put_response_body(self):
        put_response = requests.put(ReadConfig.getBaseURL()+ReadConfig.putEndPoint(), json=Put_API_Payload.update_post())
        put_response_body=put_response.json()
        return put_response_body["name"],put_response_body["job"]