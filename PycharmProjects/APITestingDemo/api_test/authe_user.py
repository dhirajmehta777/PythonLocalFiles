import requests

# res=requests.get("https://the-internet.herokuapp.com/basic_auth", auth=('abxd','sde'))
# print(res.status_code)#401 as crdentials are unauthorized

res=requests.get("https://the-internet.herokuapp.com/basic_auth", auth=('admin','admin'))
print(res.status_code)#200 as crdentials are authorized or valid