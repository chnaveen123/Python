
class TooYoung(Exception):
    pass

class  TooOld(Exception):
    pass
class TooLittle(Exception):
    pass

age = 18
try:
    if age <= 10:
        raise TooLittle("Too very little to decide teh leader")
    elif age <= 15:
        raise TooYoung("Age is less to cast your valueable vote")

    elif age > 100:
        raise TooOld("Too Old to decide Leader")
    else:
        print("You can Cast your Leader")
except TooLittle as l:
    print(l)
except TooYoung as y:
    print(y)
except TooOld as o:
    print(o)

except Exception as e:
    print(e)
finally:
    print("completed the process of voting")
