a = input("введи функцию: ")
if a in dir(str()):
    print("str")
elif a in dir(list()):
    print("list")
else:
    print("nope")