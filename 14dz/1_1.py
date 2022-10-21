a = input("введи название файла: ")
def god_file():
    global a
    b = open(a,"w")
    b.close
    return b

x = int(input("если введешь 1, создастся файл с именем, ннада? "))
if x == 1:
    god_file()


