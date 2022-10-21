import random
import sys

a = "0444"
b = ["1", "4", "5", "7", "9", "0"]
try:
    def gen_number():
        global b
        random.shuffle(b)
        return (b)


    def komb_number():
        global b
        random.choices(b, k=6)
        return b
   
    def g_n():
        global b
        num = "".join(random.choices(b, k = 6))
        return f"{num}"

    if sys.argv[1] == "-n":
        for i in range(5):
            print(a+"".join(gen_number()))
    
    elif sys.argv[1] == "-m":
        for i in range(5):
            print("\n",a+g_n())
    
    elif sys.argv[1] == "-k":
        for i in range(10):
            print("\n",a+"".join(komb_number()))
except:
    print("ты можешь воспользоваться прогой только с ключами -m , -n , -k. пример: python3 2_1.py -m")


