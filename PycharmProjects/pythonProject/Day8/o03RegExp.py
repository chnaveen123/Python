"""
st = "The quick brown fox jumps over the lazy black dog"

"""
import re
st = "The quick brown fox jumps over the lazy black dog"

res = re.search(r'(f\w+)', st)

if res:


    print("Match founded")
    print(f"String that did't match : {st[:res.start()]}")
    print(f"string that matched : {res.group(0)} \t {st[res.start():res.end()]}")
    print(f"string that is not checked :{st[res.end():]}")

else:
    print("Match not found")