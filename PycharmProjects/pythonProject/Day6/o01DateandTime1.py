from datetime import datetime
import dateutils

dt = datetime.now()
print(dt)

print("-" * 40)

print(dt.strftime("%a"))
print(dt.strftime("%A"))

print("-" * 40)

print(dt.strftime("%b"))
print(dt.strftime("%B"))

print("-" * 40)
print(dt.strftime("%d"))
print("-" * 40)
print(dt.strftime("%D"))

print("-" * 40)
print(dt.strftime("%y"))
print(dt.strftime("%Y"))

print("-" * 40)
print(dt.strftime("%T"))

print("-" * 40)
print(dt.strftime("%H"+":"+"%M"))

print("-" * 40)
print(dt.strftime("%Y/%m/%d"))
print("-" * 40)
print(dt.strftime("%M-%B-%Y"))

print("-" * 40)
dt1 = "Wednesday, April 13, 2022"
print(dt1)
print(type(dt1))

print("-" * 40)
dt2 = "Monday, April 13, 2021"
print(dt2)

print("-" * 40)
date1 = (dt.strftime("%A, %B %d, %Y"))
print(date1)
print(type(date1))

print("-" * 40)
date1 = (datetime.strptime(dt1,"%A, %B %d, %Y"))
print(date1)
print(type(date1))

print("-" * 40)
date2 = (datetime.strptime(dt2,"%A, %B %d, %Y"))
print(date2)
print(type(date2))


print("-" * 40)
print(date1 - date2)

print("-" * 40)
print(dateutils.days(date1, date2))

print("-" * 40)
print(dateutils.weeks(date1, date2))


print("-" * 40)
print(dateutils.months(date1, date2))

print("-" * 40)
print(dateutils.years(date1, date2))




















