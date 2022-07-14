l1 = list()
print(l1)

l2 = list(range(1,11))
print(l2)
print(id(l2[3]))


print(40 * "*")

l1 = list(range(1,11))

print(l1[0])
print(l1[9])
print(l1[-1])
print(l1[-3])

print(l1[3:8])
print(l1[1::2])
print(l1[0::2])

for i in l1:
    if i % 2 ==0:
        print(i, end=" ")


print(40 * "*")

l2 = list(range(3,25,3))
print(l2)
print(l2[-1])
print(l2[-5])
print(l2[-8])
for i in l2:
    if i % 3 == 0:
        print(i, end = " ")

""" """

print(40 * "*")

print(l1[:-10:-1])
print(l1[-1:-10:-1])
print(l1[-1::-1])
print(l1)

l1[1] = "two"
print(l1)
print(l1.pop(1))
print(l1)
print(l1.sort())

print(40 * "*")

list = list(range(1,6))
print(list)
list.append(6)
list.append(7)
list.append(8)
print(list)
list.append([9,10,11,12,13])
print(list)
print(list[-1][-2:-5:-1])
print(40 * "*")

print("{:-^40}".format("extend"))

l2 = [11,12,13,14,15]
print(l2)
l2.extend([16,17,18])
print(l2)
l2.extend([19,20,21])
print(l2)


print("{:-^40}".format("insert"))
n = len(l2)
l2.insert(n+1,22)
print(l2)


print("{:-^40}".format("pop"))

res = l2.pop()
print(res)
print(l2)
print("{:-^40}".format("remove"))

l2.remove(21)
print(l2)
l2.remove(17)
print(l2)
print("{:-^40}".format("clear"))
l2.clear()
print(l2)
print("{:-^40}".format("clear"))
l1 = [1, 2, 3, 1, 2, 1, 2, 1, 3, 1, 1, 2, 1, 4, 1, 2, 1]

for i in l1:
    if l1[i] == 1:
        l1.remove(i)
    print(l1)
print("{:-^40}".format("clear"))
l2 = [1, 2, 3, 4, [10, 20, 30, 40, 50], 6, 7, [11, 12, 13, 14, 15], 9, 10]
l2[4].clear()
l2[7].clear()
print(l2)

print("{:-^40}".format("clear"))
l1 = [1,2,3,1,2,1,2,1,3,1,1,2,1,4,1,2,1,1,1,1]
len = len(l1)

for i in range(len-1,-1,-1):
    if l1[i]==1:
        l1.pop(i)
print(l1)
print("{:-^40}".format("clear"))

l1 = [1,2,3,1,2,1,2,1,3,1,1,2,1,4,1,2,1,1,1,1]
for i in l1:
    if i == 1:
        l1.remove(i)
        print(l1)

print("{:-^40}".format("clear"))
l1 = [1,2,3,1,2,1,2,1,3,1,1,2,1,4,1,2,1,1,1,1]
n = []
for i in l1:
    if i!= 1:
        n.append(i)
print(n)


l1 = [1,2,3,1,2,1,2,1,3,1,1,2,1,4,1,2,1,1,1,1]
while(True):
    try:
        l1.remove(1)
    except ValueError:
        break
print(l1)

