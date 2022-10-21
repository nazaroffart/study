def ranger(min, max):
    list1 = range(min, max + 1)
    return list1
a = ranger(max = 6, min = 1)
print(a)


def f(m, g = 9.8):
    return m*g
print(f(m = 5, g = 9.8))

def figure(*args):

    i = 0
    string_coords = ""
    while (i < len(args)):
        if(i%2 == 0):
            string_coords += "x(" + str(args)





def figure(name, *goals):
    print("players name: ", name)
    for i in goals:
        print(i)
figure("Benzems", 1)

a = [1,2,3]
b = [*a, 4,5,6]
c = a+b
print(c)

def func(owner, **pets):
    print(owner)
    for pets, name in pets.items():
        print(f"{pets}: {name}")
func(owner = "John",dog = "Btock", turtle = "sss")


a = {"key": "value"}
b = {**a, "key2": "value2"}
print(b)
