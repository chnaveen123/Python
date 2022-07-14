
def drawborder(fnc):
     def helper(*args):

         fnc(*args)


     return helper


@drawborder('*','#',40)
def greet(msg):
    print("greet",msg)

@drawborder('=','_',30)
def RSVP(msg):
    print("RSVP",msg)
