import requests

# resp=requests.get("https://reqres.in/api/users?page=2")
#################OR#####################################
p={"page":2}
resp=requests.get("https://reqres.in/api/users",params=p)
print(resp.url)
json_response = resp.json()

#To get some specific record from json:
print(json_response['total'])
assert json_response['total']==12, "total count doesnt match"

print(json_response['total_pages'])
assert json_response['total_pages']==2, "total pages count doesn,t match"

print(json_response["data"][0]["email"])
assert (json_response["data"][0]["email"]).endswith("reqres.in"), "email format is not matching"

print(json_response["data"][0]["first_name"])
assert json_response["data"][0]["first_name"]!=None

print(json_response["data"][2]["last_name"])
assert json_response["data"][2]["last_name"]!=None

print(json_response["support"]["url"])