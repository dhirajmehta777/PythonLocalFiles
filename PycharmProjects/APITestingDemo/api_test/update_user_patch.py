import requests

payload={
    "job": "Automation"
}
print(type(payload))#<class 'dict'>
resp=requests.patch("https://reqres.in/api/users/2", data=payload)#here put means we are updating the existing user
print(resp)

#if we want the data in json:
print(resp.json())#{'name': 'Jhon', 'job': 'QA', 'updatedAt': '2022-12-02T12:17:45.893Z'}
assert resp.json()['job']=='Automation'