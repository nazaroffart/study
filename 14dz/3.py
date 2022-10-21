a = int(input("введи первое число: "))
b = int(input("введи второе число: "))
def minus():
    c = a - b
    return c

def plus():
    c = a + b
    return c

def oba():
    minus()
    plus()
    if a>0:
        return plus()
    else:
        return minus()

print(oba())
