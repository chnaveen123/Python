numbers = [1,2,3,4,5]
itrObj = iter(numbers)

while True:
    try:
        elem = next(itrObj)
        print(elem)
    except StopIteration:
        break

print("*" * 40)
st = "Hello world"
for s in st:
    print(s, end=" ")
print()
print("*" * 40)

class MyNumber:
    def __init__(self, max):
        self.max = max
    def __iter__(self):
        self.n = 1
        return self
    def __next__(self):
        if self.n <= self.max:
            res = self.n
            self.n += 2
            return res
        else:
            raise StopIteration
myObj = MyNumber(10)
itrObj = iter(myObj)

print(next(itrObj))

for i in myObj:
    print(i)


