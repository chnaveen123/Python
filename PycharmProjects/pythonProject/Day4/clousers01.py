def outerFun(greet):

    def innerFun(name):

        print(greet, name)

    return innerFun
outerFun("Hello")("sachin")

hindiGrt = outerFun("Namaskar")
tamilGrt = outerFun("vanakkam")
spanisGrt = outerFun("Hola")

hindiGrt("Jadeja")
tamilGrt("Naveen")
spanisGrt("Messi")





