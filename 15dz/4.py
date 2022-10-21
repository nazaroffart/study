a = int(input("ширина: "))
b = int(input("длина: "))

def plos(a, b):
    if a == b:
        c = (a+b)*2
    else:
        c = a*b
    return c
print(plos(a,b))
