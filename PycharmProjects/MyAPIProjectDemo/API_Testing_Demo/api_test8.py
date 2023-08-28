'''
$ pip install -U requests
$ pip install -U pytest pytest-html
$ pip install -U jsonschema

'''

import requests

def test_get_employee_details_check_status_code_equals_200():
     response = requests.get("http://demo.example.com/employee/employee1")
     assert response.status_code == 200

"""
To generate an HTML report, run the test with the parameters below. 

$pytest -sv --html report.html
"""

"""
Extending our test suite
Typically, we're interested in things other than the response HTTP status code too. For example, let's check if the value of the response content-type header correctly identifies that the response body is in JSON format and validates incoming JSON schema.

API endpoint: 

http://demo.example.com/employee_details?id=1
"""
"""
Sample response:

{
  "status": "ok",
  "employee": {
    "id": "1",
    "firstName": "Abc",
    "middleName": null,
    "lastName": "Xyz"
  }
}
"""

"""
For the above example, let's define JSON schema against which we will validate the incoming response.

Few imports:

import requests
import json
from jsonschema import validate
from jsonschema import Draft6Validator
JSON schema declaration:

schema = {
    "$schema": "https://json-schema.org/schema#",

    "type" : "object",
    "properties" : {
        "status" : {"type" : "string"},
        "employee": {
            "type": "object",
            "properties": {
                "id": { "type": "string" },
                "firstName": { "type": "string" },
                "middleName": {
                    "anyOf": [
                        {"type": "string"},
                        {"type": "null"}
                    ] },
                "lastName": { "type": "string" }
            },
            "required": ["id", "firstName", "lastName"]
        }
    }
}
"""

"""
Test case function:

def test_get_employees_validates_json_resonse_schema ():

    response = requests.get("http://demo.example.com/employee")
    
    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200

    # Validate response content type header
    assert response.headers["Content-Type"] == "application/json"

    resp_body = response.json()

    # Validate will raise exception if given json is not
    # what is described in schema.
    validate(instance=resp_body, schema=schema)
"""