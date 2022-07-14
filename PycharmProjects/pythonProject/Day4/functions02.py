"""
Outer function is the parent of inner function
Rule1: to declare a non local variable we should have a local variable in parent function
"""
name = "Naveen"
def outerfun():
    name = "sachin"

    def innerfun():
        global name
        name = "dhoni"

        print(f"Hello {name}")
    print(f"before outer: {name}")

    print(f"Before: {name}")
    innerfun()
    print(f"After: {name}")

print(f"before outer: {name}")
outerfun()
print(f"After outer: {name}")