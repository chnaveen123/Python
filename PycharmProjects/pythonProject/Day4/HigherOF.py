def callMe():
    print("Apples from ooty")

def fun(fnc):
    print("Hello..")
    fnc()
    print("Hi..")
    print("-" * 40)


    def defineMe():
        print(f"Oranges from kanupur")
    return defineMe

def funCallback(fnc):
    print("Mera bharath mahan")
    fnc()
    print("india is great")

funCallback(fun(callMe))