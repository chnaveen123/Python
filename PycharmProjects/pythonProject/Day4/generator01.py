def fun():
    n = 1
    print("apples from ooty.")
    yield n

    n += 9
    print("Oranges from kanpur")
    yield n
    n += 10
    print("Grapes from hubli")
    yield n

funObj = fun()
print(f"funObj :{funObj}")
print(funObj.__next__())
print(funObj.__next__())
print(funObj.__next__())

print("-" * 40)

def get_val():
    for i in range(1,11):
        yield i
res = get_val()

print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))