xy1 = []

x1 = int(input("Введи координату первого числа по оси х: "))
xy1.append(x1)
y1 = int(input("Введи координату первого числа по оси у: "))
xy1.append(y1)

xy2 = []
x2 = int(input("Введи координату второго числа по оси х: "))
xy2.append(x2)
y2 = int(input("Введи координату второго числа по оси у: "))
xy2.append(y2)

if xy1[0] > 0 and xy1[1] > 0 and xy2[0] > 0 and xy2[1] > 0:
    print("значения в одном диапазоне")
elif xy1[0] < 0 and xy1[1] < 0 and xy2[0] < 0 and xy2[1] < 0:
    print("значения в одном диапазоне")
elif xy1[0] > 0 and xy1[1] < 0 and xy2[0] > 0 and xy2[1] < 0:
    print("значения в одном диапазоне")
elif xy1[0] < 0 and xy1[1] > 0 and xy2[0] < 0 and xy2[1] > 0:
    print("значения в одном диапазоне")
else:
    print("значения в разных диапазонах")

