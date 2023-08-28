import json

import requests


mydata=open("data.json","r").read()
resp=requests.post("https://reqres.in/api/users", data=json.loads(mydata))
#here loads method will deserilize the what ever data we have into python object
print(resp)#<Response [201]>

#if we want the data in json:
print(resp.json())
assert resp.json()['job']=='leader'

#if we want to get only the content-type of header:
print(resp.headers.get("Content-Type"))