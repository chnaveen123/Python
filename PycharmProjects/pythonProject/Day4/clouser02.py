def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(name):
            from emojis import emojis

            emojised = emojis.encode(greet + " :" + sep + ": " +name)
            print(emojised)
        return innerMostFun
    return innerFun
engGrt = outerFun("Welcome")
tgrEmj = engGrt("tiger")
tgrEmj("NAveen")
hndGrt = outerFun("Namaskar")
elptEmj = hndGrt("elephant")
elptEmj("shareoff")

"""print("-"*40)
outerFun("Welcome")("====>")("Sachin")

print("-"*40)
engGrt = outerFun("Welcome")
hndGrt = outerFun("Namaskar")
TmlGrt = outerFun("Vanakam")

print("-" * 40)

sngln = engGrt("------->")
dbln = hndGrt("======>")
strln = TmlGrt("******>>")

print("-" * 40)

sngln("Sunil Gavaskar")
dbln("Kapil Dev")
strln("Naveen")
"""












