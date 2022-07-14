import re

st = """
    the quick brown fox jumps over the lazy black dog
    the quick brown fox jumps over the lazy black dog
    the quick brown fox jumps over the lazy black dog
    the quick brown fox jumps over the lazy black dog
    the quick brown fox jumps over the lazy black dog
    the quick brown fox jumps over the lazy black dog
    the  quick brown fox jumps over the lazy black dog
    the quick brown fox jumps over the lazy black dog
        
"""

reg = re.compile(r't\w+')
print(f"reg: {reg}")

res = re.findall(reg, st)

print(f"res : {res}")

print(len(res))