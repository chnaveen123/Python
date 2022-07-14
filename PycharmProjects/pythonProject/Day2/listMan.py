print("{:-^40}".format("count"))

l1 = [1,2,3,1,2,1,2,1,3,1,1,2,1,4,1,2,1,1,1,1]

print(l1.count(1))
print(l1.count(2))
print(l1.count(3))

print("{:-^40}".format("index"))

l2 = [1, 2, 3, 4, [10, 20, 30, 40, 50], 6, 7, [11, 12, 13, 14, 15], 9, 10]
print(l2.index( 7))
print(l2.index([10,20,30,40,50]))
print(l2[4][1:4])

print("{:-^40}".format("copy"))

l1 = [1,2,3,4,5]
print(l1)
l2 = l1
print(l2)
print("{:-^40}".format("copy"))
l2.extend([6,7,8,9])
print(l2)
print(l1)

print("{:-^40}".format("Deep-copy"))
l3 = [6,7,8,9,10]
print(l3)
l4 = l3.copy()
print(l4)

l4.insert(0,5)
l4.insert(0,4)
l4.insert(0,3)
print(l3)
print(l4)

l5 = [10,20,30,40,[5,15,25,35],50]
print(l5)
l6 = l5.copy()
print(l6)
l7 = l5
print(l7)
from copy import deepcopy
l5 = [10,20,30,40,[5,15,25,35],50]
l8 = deepcopy(l5)
print(l8)
l8[4].insert(1,2)
l8[4].insert(2,3)
print(l8)
print(l5)

print("{:-^40}".format("Sort"))

l = [1,6,3,4,2,5,9,7,8]
l.sort()
print(l)
print(sorted(l))
print(sorted(l, reverse = True))



l1 = [1,"Naveen",6,"mango",3,"Orange",4,"red","orange",2,"cat",5,9,7,8]
res = sorted(l1, key=ascii)
print(res)

l = [9, 'zebra', 'apple',5, 'yellow', 'blue', 8, 'green', 'violet', 1, 'pink', 'orange', 10,
     4, 'red', 'dog', 2, 'cat', 'snake', 6, 1024, 19, 120, 1452, 3, 28, 215, 2098, 7]
res = sorted(l, key=ascii)
print(res)


l = ['zebra', 'apple', 'yellow', 'blue',  'green', 'violet',  'pink', 'orange',
      'red', 'dog',  'cat', 'snake']
res = sorted(l, key=len)
print(res)



mnth = ['dec','aug','oct','nov','sep','jan','apr','mar','jul','feb','may','jun']
res = sorted(mnth, key=len)
res1 = sorted(mnth)
print(res1)
print(res)