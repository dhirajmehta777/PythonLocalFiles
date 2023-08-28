import  requests

resp=requests.delete("https://reqres.in/api/users/2")
#print(resp.json())#this command will not work as we are deleting.
print(resp.status_code)
assert resp.status_code == 204, "user deletion failed"