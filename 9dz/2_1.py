factorial = 1
num = int(input())
if num < 0:
   print("Для отрицательных чисел факториал не определен")
elif num == 0:
   print("Факториал 0 равен 1")
else:
    for i in range(2, num+1):
        factorial = factorial * i
    
        print(factorial)
        


