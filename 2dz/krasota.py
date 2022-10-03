print("Формула красоты по Ландау")

k = float(input("Обхват по бюсту(см): "))
m = float(input("Обхват по бедрам(см): "))
n = float(input("Обхват по талии(см): "))
t = float(input("Рост(см): "))
p = float(input("Вес(кг): "))

l = (k*m*t)/(n**2*p)

print(l)
