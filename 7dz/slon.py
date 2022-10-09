x_sl = int(input("Координата слона по оси х: "))
y_sl = int(input("Координата слона по оси у: "))

x_fig = int(input("Координата фигуры по оси х: "))
y_fig = int(input("Координата фигуры по оси у: "))

if x_sl == x_fig and y_sl == y_fig:
    print("Слон бьет фигуру")
else:
    print("Слон не бьет фигуру")

