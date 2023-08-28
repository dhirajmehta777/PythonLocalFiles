import  requests

r=requests.get("https://httpbin.org/delay/5", timeout=3)
#here within 3 seconds if we wont get response the it will throw "read time out" error
#here it takes 5 seconds to respond hence thrown error
print(r.status_code)