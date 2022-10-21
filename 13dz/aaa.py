import os
import sys
os.system("ls -la")
os.system("uname")

print(56+54)

if sys.argv[0] == "-a":
    print("hello world")



import random

print(random.randrange(1,5,1))
print(random.randint(1,3))


a = [546,656,61,456]
print(random.choice(a))

import math

print(math.factorial(8))



from hi import *
print(c)
