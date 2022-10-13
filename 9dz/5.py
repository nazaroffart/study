"""
for i in range(1,11):
    print(i)
a = 0
while a < 10:
    a += 1
    print(a)
while a > 1:
    a -= 1
    print(a)
"""    

a = 10

for i in range(1,21):
    if i >= 10:
        print(i - (i-a))
        a = a-1
    else:
        print(i)
