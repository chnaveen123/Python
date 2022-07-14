def get_name(surname):
    print(surname)
    while True:
        name = yield
        print(f"received {name}")
        if surname in name:
            print(f"surname {surname} matched in name")

coObj = get_name("pillai")
print(coObj)
coObj.__next__()
coObj.send("Virat Kohli")
coObj.send("Naveen Chiruveru")
coObj.send("Dhoni m.s")
coObj.send("dheeraj pillai")