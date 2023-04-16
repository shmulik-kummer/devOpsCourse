# import requests
#
# response = requests.get("http://127.0.0.1:5001/whatismyname")
# print(response.text)

x = "shmulik"

w = ""
for i in x:
    w = i + w

if x == w:
    print("Yes")
else:
    print("No")