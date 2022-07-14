
import requests

BASE = "http://127.0.0.1:5000/"


response = requests.get(BASE + "/getproduct/baverage")

print(response.json())

res = response.json()

for k, info in res.items():
    print(k.upper())
    print("-------")
    for ky, vl in info.items():
        print(ky, "=>", vl)
        print("-" * 40)



