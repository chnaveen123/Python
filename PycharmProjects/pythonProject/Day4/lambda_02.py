months = ['feb','mar','jan','apr','jun','may','aug','jul','oct','nov','sep','dec']
print(months)

from calendar import month_name

strdmonths = sorted(months, key = list(map(lambda m: m[0:3].lower(),list(month_name))).index)

print(f"sortedMonths : {strdmonths}")

print("Filter".center(40,"-"))

l = list(range(1,21))
print(l)
res = list(filter(lambda x: x % 3 ==0, l))
print(res)

print("Reduce".center(40,"-"))

l = [4,9,6,2,5,8,10,15,9,12,11]

from functools import reduce

res = reduce(lambda x, y: x if x > y else y, l)
print(res)
print("*" *  40)

l = [4,9,6,2,5,8,10,15,9,12,11]

from functools import reduce

res = reduce(lambda x, y: x * y , l)
print(res)






