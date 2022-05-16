import requests

url = "https://crumbs.web.actf.co/"
req = requests.get(url)
result = req.text.split(" ")[2]
for i in range(1001):
    req = requests.get(url+result)
    result = req.text.split(" ")[2]
    print(str(i) + " => " + result)
