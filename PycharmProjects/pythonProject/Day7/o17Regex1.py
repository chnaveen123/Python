import re

"""st = "Hello world"

res = re.match(r'^Hello',st)
res = re.search(r'^Hello$',st)
res = re.search(r'b..t', st)
res = re.search(r'ba*t', st) ==> 0 or more occurances
res = re.search(r'ba?t', st) ==> 0 or 1 occurances
res = re.search(r'ba+t', st) ==> 1 or more occurances
res = re.search(r'ba{3,8}t', st) ==> based on characters we choose
res = re.search(r'b[a-z]t', st)
res = re.search(r'b[aeiou]t', st)
res = re.search(r'b[aeiou]t', st)

"""

st = "sample.py"

res = re.search(r'.py', st)

if res:
    #print(res)
    print(res.group(0))
    print("Match founded")

else:
    print("Match not found")