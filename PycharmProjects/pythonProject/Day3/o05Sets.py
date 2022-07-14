s1 = set()
print(s1)
print(type(s1))
print("-" *20)
s2 = {1,2,3,4,5,6,1,2,3}
print(s2)
print(type(s2))
print("-" *20)
s3 = (set(range(1,10)))
print(s3)
for i in s3:
    print(i, end=" ")
print()
print("-" *20)
s4 = {1,2}
print(s4)
s4.add(1)
s4.add(3)
s4.add(2)
s4.add(4)
print(s4)

print("Update".center(40,"*"))
print(s4)
s4.update([1, 2])
s4.update([2, 3, 4])
s4.update([3, 4, 5])
s4.update([6,7,8])
print(s4)

print("pop".center(40,"*"))
print(s4)
s4.pop()
print(s4)
s4.pop()
print(s4)

print("remove".center(40,"*"))

print(s4)
s4.remove(8)
s4.remove(5)
print(s4)

print("discard".center(40,"*"))
print(s4)
s4.discard(4)
s4.discard(8)
print(s4)

print("-" *40)
A = {1,2,3,4,5,6}
B = {5,6,7,8,9,10}
print(A)
print(B)
print(A | B)
print(B.union(A))
print("-" *40)
print(A & B)

print("-" *40)

print(A - B)
print(B - A)

print("-" *40)
print(A ^ B)
print(B.symmetric_difference(A))

print("-" *40)

fs = frozenset([1,2,3,4,5])
print(f"fs :{fs}")
print("-" *40)

d1 = { 1:2, 3:4}
d2 = {4:5, 6:7}
d3 = {8:9, 10: 11}

d4 = {}

print(d4.update(d1))
print(d4.update(d2))
print(d4.update(d3))
print("-" *40)
print(d4)
print("-" *40)
d1={1:2,3:4}
d2={4:5,6:7}
d3={8:9,10:11}
d1.update(d2)
d1.update(d3)
d4=dict()
d4=d1
print("d4:",d4)













