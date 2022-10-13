"""
a = 4
while a < 10:
    if a == 8:
        print(a)
    a += 2

for i in range(1,10,2):
    print(i)

for i in "4,6,1":
    print(i)


for i in range(1,10):
    if i == 5:
        print(i)
    else:
        print("unknown")


def some_num(a,b):
    return a+b

print(some_num(1, 5))



number = 0

for number in range(10):
    if number == 5:
        continue

    print("Цифра: ", number)

 
for num in "Hello":
    if num == "o":
        continue
    print(num)


name = {
        1:"Bob",
        2:"Tom",
        3:"Mark"
        }

for i in name.values():
    print(i)

name = {
        1:"Bob",
        2:"Tom",
        3:"Mark"
        }

for i, a in name.items():
    print(i, "--->", a)
"""





for i in range(0,10,2):
    print(i)



a = [1,2,3,4,6,7,9,7]
for i in range(6):
    a.pop()

print(a)
