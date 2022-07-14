a=[1,2,3,4,5]
b=[1,2,3,4,5,6,7]
class greter(Exception):
    pass
class lesser(Exception):
    pass

class notequl(Exception):
    pass
class equal(Exception):
    pass

try:
    if len(a)>len(b):
        raise lesser("second list  is greater ")
    elif a==b and len(a)==len(b):
        raise equal("both are equal in length ")
    elif len(a)> len(b):
        raise greter(" first list is greatest")

except greter as great:
    print(great)
except lesser as les:
    print(les)
except notequl as notEq:
    print(notEq)
except equal as eql:
    print(eql)
finally:
    print("process completed succesfully ")

