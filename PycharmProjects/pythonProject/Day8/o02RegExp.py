
import re

st = "good blood bad blood"

res = re.search(r'(\w+)\s(\w+)\s(\w+)\s(\2)',st)

if res :


    print("match found" )
    print(res.group(0))
    print(res.group(1))
    print(res.group(2))
    print(res.group(3))
    print(res.group(4))
else:
    print("no match found")








