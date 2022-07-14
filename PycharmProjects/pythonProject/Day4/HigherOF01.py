def bank_flow(fnc):
    print("Login")
    fnc()
    print("Logout")

def withdraw():
    print("debitted")
def deposit():
    print("Credited")
def gift():
    print("Tranferred")

bank_flow(withdraw)
bank_flow(deposit)
bank_flow(gift)


