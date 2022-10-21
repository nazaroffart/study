import time


def decor(func):
    def wrapper():
        print("начинает обертку")
        func()
        print("закрыть")
    return wrapper
def pr():
    print("оборачиваемая функция")
a = decor(pr)
a()
print(a)

def sd(x):
    return x**2
print(sd(5))

a = (lambda x: x**2)(int(input()))
print(a)

print((lambda x: x**2)(int(input())))



def decor(func):
    def wrapper():
        start_time = time.time()
        func()
        print(time.time() - start_time)
    return wrapper



@decor
def pr():
    print("оборачиваемая функция")
pr()

"""



try:
    def rec(x):
        if x < 5:
            print(x)
            rec(x+1)
#        print(x)
    rec(1)
except:
    print("done")
"""
