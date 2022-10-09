city_list = []

a = input("""Выберите действие:
1. Добавить новый город
2. Отобразить список городов
3. Заменить город
4. Удалить город
5. Выход\n\n""")

if a == '1':
    add_city = input("Введите название города: ")
    if add_city in city_list:
        print(f"Город {add_city} уже есть.Его индекс: {city_list.index(add_city)}")        
    else:
        city_list.append(add_city)
        print(f"Добавлен город {add_city}")
        a = input('''Выберите действие:
    1. Добавить новый город
    2. Отобразить список городов
    3. Заменить город
    4. Удалить город
    5. Выход
    ''')
        
        if a == '1':
            add_city = input("Введите название города: ")
            if add_city in city_list:
                print(f"Город {add_city} уже есть.Его индекс: {city_list.index(add_city)}")        
            else:
                city_list.append(add_city)
                print(f"Добавлен город {add_city}")
                a = input('''Выберите действие:
            2. Отобразить список городов
            3. Заменить город
            4. Удалить город
            5. Выход
            ''')

        
            if a == "2":
                print(city_list)
            elif a == "3":
                city_name = input("какой город надо заменить: ")
                if city_name in city_list:
                    city_list.remove(city_name)
                    ch_city = input("Введите новый город: ")
                    city_list.append(city_name)
                    print(f"Вы заменили {city_name} на {ch_city}",city_list)
                else:
                    print(f"города {city_name} нет в списке городов")

            elif a == "4":
                city_del = input("какой город вы хотите удалить: ")
                if city_del in city_list:
                    city_list.remove(city_del)
                    print(f"город {city_del} удален")
                else:
                    print(f"города {city_del} не существует")
        
        elif a == "2":
            print(city_list)
        elif a == "3":
            city_name = input("какой город надо заменить: ")
            if city_name in city_list:
                city_list.remove(city_name)
                ch_city = input("Введите новый город: ")
                city_list.append(city_name)
                print(f"Вы заменили {city_name} на {ch_city}",city_list)
            else:
                print(f"города {city_name} нет в списке городов")

        elif a == "4":
            city_del = input("какой город вы хотите удалить: ")
            if city_del in city_list:
                city_list.remove(city_del)
                print(f"город {city_del} удален")
            else:
                print(f"города {city_del} не существует")
elif a == "2":
    
    print("Список городов еще пуст. если хочешь добавить город, нажми 1")
    a = input("""Выберите действие:
    1. Добавить новый город
    2. Отобразить список городов
    3. Заменить город
    4. Удалить город
    5. Выход\n\n""")
    
    if a == '1':
        add_city = input("Введите название города: ")
        if add_city in city_list:
            print(f"Город {add_city} уже есть.Его индекс: {city_list.index(add_city)}")        
        else:
            city_list.append(add_city)
            print(f"Добавлен город {add_city}")
            a = input('''Выберите действие:
        1. Добавить новый город
        2. Отобразить список городов
        3. Заменить город
        4. Удалить город
        5. Выход
        ''')
        
            if a == "2":
                print(city_list)
            elif a == "3":
                city_name = input("какой город надо заменить: ")
                if city_name in city_list:
                    city_list.remove(city_name)
                    ch_city = input("Введите новый город: ")
                    city_list.append(city_name)
                    print(f"Вы заменили {city_name} на {ch_city}",city_list)
                else:
                    print(f"города {city_name} нет в списке городов")

            elif a == "4":
                city_del = input("какой город вы хотите удалить: ")
                if city_del in city_list:
                    city_list.remove(city_del)
                    print(f"город {city_del} удален")
                else:
                    print(f"города {city_del} не существует")

