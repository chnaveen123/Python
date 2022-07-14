glbx = 100

def fun(n):
    global glbx

    glbx = 500

    print(n)



    print(f"glbx Inside : {glbx}")

print(f"glbx Before : {glbx}")

fun(50)

print(f"glbx After : {glbx}")

print("*" * 40)
