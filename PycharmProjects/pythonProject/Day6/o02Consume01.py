import sys
sys.path.append("C:\Delhi")
for i in sys.path:
    print(i)
from gurgoan.MyModule import Player


"""import gurgoan.MyModule as m

from m  import Player"""

# m.greet("Sourav Ganguly")

print("-" * 40 )

pl1 = Player("Sourav Ganguly", 38)

pl1.get_details()


