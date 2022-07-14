import re
 #words that start with(case sensitive)# # A, W, T, O, M, Z, Y, P, S

fh = open(r"data.txt", "r").read()
m = re.findall(r'[S]\w+', fh)
n = re.findall(r'[A]\w+', fh)
N = re.findall(r'[W]\w+', fh)
for i in m:
 print(i)
print(f"m :{m}")
print(len(m))
print("-" * 40)
print(f"m :{n}")
print(len(n))
print("-" * 40)
print(f"m :{N}")
print(len(N))