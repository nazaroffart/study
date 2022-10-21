k = int(input("вместимость котлет на сковороде: "))
m = int(input("кол-во времени для обжарки котлет с каждой стороны: "))*2
n = int(input("сколько котлет надо пожарить: "))

if n>k and n < k*2:
    print(m*2)

elif n > k*2 and n<k*3:
    print(m*3)
elif n<k:
    print(m)
