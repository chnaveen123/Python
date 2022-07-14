
import sys

num = ""
inv = 1
try:
    inv = 1 / num
except Exception as e:
    print(e)
except ZeroDivisionError as z:
    print("Exception Ocured")
    print(sys.exc_info()[0])
    print(z)

except TypeError as t:
    print(t)
else:
    print(f"inv :{inv}")
finally:
    print("PROCESS Completed")

