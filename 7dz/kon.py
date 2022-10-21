x_kon = int(input("Введи значение коня по оси х: "))
y_kon = int(input("Введи значение коня по оси у: "))

x_fig = int(input("Введи значение фигуры по оси х: "))
y_fig = int(input("Введи значение фигуры по оси у: "))

if (x_kon + 2 == x_fig and y_kon + 1 == y_fig or 
x_kon + 2 == x_fig and y_kon - 1 == y_fig or x_kon - 2 == x_fig and y_kon + 1 == y_fig or 
x_kon - 2 == x_fig and y_kon - 1 == y_fig or x_kon + 1 == x_fig and y_kon + 2 == y_fig or 
x_kon + 1 == x_fig and y_kon - 2 == y_fig or x_kon - 1 == x_fig and y_kon + 2 == y_fig or 
x_kon - 1 == x_fig and y_kon - 2 == y_fig):
    print("Конь бьет фигуру")

else:
    print("Конь не бьет фигуру")
