try:
    a = int(input("введи первое число: "))
    b = int(input("введи второе число: "))
    c = input("введи шо хош сделать с ними: ")
    def arithmetic():
        if c == "/":
            x = a / b
        elif c == "*":
            x = a * b
        elif c == "+":
            x = a + b
        elif c == "-":
            x = a - b

        else:
            print("нет такой операции")
        return x
    print(arithmetic())
except:
    print("программа умеет только +, -, *, /")
