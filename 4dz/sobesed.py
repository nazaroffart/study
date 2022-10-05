lng_prog = str(input("Язык программирования: "))
lng = lng_prog.lower()
if lng == "python" or "java" or "javascript":
    age = int(input("Возраст: "))
    if age >= 18 and age <= 65:
        exp = int(input("Опыт работы: "))
        if exp >= 3:
            zp = int(input("Желаемая зарплата: "))
            if zp <= 60000:
                print("Вы нам подходите")

            else:
                print("Вы нам не подходите")
        else:
            print("Вы нам не подходите")
    else:
        print("Вы нам не подходите")
else:
    print("Вы нам не подходите")
