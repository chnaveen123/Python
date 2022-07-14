f = open("data.txt", "r")

n = input("enter value :")
m = "NO"

for char in f:

    if n == m:
        print(char)

f.close()