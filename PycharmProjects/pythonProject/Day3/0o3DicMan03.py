print("{:*^40}".format("items"))

emp = {
    'emp1' : {'empid' : 67322, 'name' : 'naveen', 'age' : 24, 'desig' : 'JSE','dept' : 'dev','sal' : 40000},
    'emp2' : {'empid' : 67323, 'name' : 'praveen', 'age' : 26, 'desig' : 'JSE','test' : 'dev','sal' : 45000},
    'emp3' :  {'empid' : 67324, 'name' : 'raju', 'age' : 27, 'desig' : 'JSE','mtest' : 'dev','sal' : 40500}
 }
print(emp)
print("_"*40)
print(emp['emp1'])
print("_"*40)
print(emp['emp2'])
print("_"*40)
print(emp['emp3'])
print("*"*40)

for ky, info in emp.items():
    print(ky)
    print("______")
    for k, v in info.items():
        print(k, "=>", v)

print("{:*^40}".format("update"))
emp1 = {'empid': 1023, 'empname': 'Smith', 'age': 32, 'desig': 'Tl', 'dept': 'MKT'}
emp2 = {'empid': 2689, 'empname': 'Jane', 'age': 36, 'desig': 'MGR',  'sal': 165000}

print(emp1)
print("*"*40)
print(emp2)
emp1.update(emp2)
print(emp1)
print("*"*40)
emp2.update(emp1)
print(emp1)

print("*"*40)

emp1 = {'empid': 1023, 'empname': 'Smith', 'age': 32, 'desig': 'Tl', 'dept': 'MKT'}

emp4 = emp1.copy()
print(emp4)
print("* deep"*40)
from copy import deepcopy
emp5 = deepcopy(emp4)
print(emp5)
print("*"*40)
emp1 = {'empid': 1023, 'empname': 'Smith', 'age': 32, 'desig': 'Tl', 'dept': 'MKT'}
emp1['exp'] = 2
print(emp1)




print("*" *20)

d1={'a':1,'b':2,'c':3,'d':4,'e':5}
print(d1)
d2=d1
print(d2)
d2['z']=25
d2['y']=20
print(d2)
print(d1)



print('-'* 20)

from copy import deepcopy
d={"adit":"shinde","cat":{"pysics":"chem ","hist":"geo"}}

print(d)
i=deepcopy(d)
print(i)

d["cat"]["hist"]="shitale"
print(d,i)

