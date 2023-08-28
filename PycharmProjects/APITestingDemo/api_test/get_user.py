import requests

resp=requests.get("https://reqres.in/api/users?page=2")
print(resp)#o/p <Response [200]>

#to know the type:
print(type(resp))#<class 'requests.models.Response'>

#to see the list of properties we have in response variable,
print(dir(resp))

#to check the status code of the API
print(resp.status_code)
code=resp.status_code
assert code == 200, "code doesn't match"

#To return the data we have following commands:
# print(resp.text)#response will be in plain string format, i.e. in unicode
# print(resp.content)#this will return the content in byte format
print(resp.json())#this will return data in json that is in serilized format,
# and we will be using this comand most of the time

#To get the headers:
print(resp.headers)#here we can get date, contenttype, encoading, connections, cookies, expdate

#to know exactly what value headers will return:
print(type(resp.headers))#this will return dictionary, key value pair

#to get cookies:
print(resp.cookies)

#to get encoding:
print(resp.encoding)

#to see the final url that you are hitting:
print(resp.url)

