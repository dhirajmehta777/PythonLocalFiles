import requests

payload={
    "name": "morpheus",
    "job": "leader"
}
print(type(payload))#<class 'dict'>
resp=requests.post("https://reqres.in/api/users", data=payload)#here post means we are creating the new user
print(resp)#<Response [201]>

#if we want the data in json:
print(resp.json())
assert resp.json()['job']=='leader'