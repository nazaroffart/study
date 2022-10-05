vlad = int(input("Сколько владельцев у авто? "))
if vlad <= 2:
    mark = str(input("Какая марка авто? "))
    mark_low = mark.lower()
    if mark_low == "тойота" or "toyota" or "лексус" or "lexus":
        year = int(input("Какого года? "))
        if year >= 2004 and year <= 2022:
            col = str(input("Какого цвета авто нужно? "))
            col_low = col.lower()
            if col == "серый" or "белый" or "grey" or "white":
                rul = str(input("С какой стороны руль?"))
                if rul == "лево" or "левый" or "слева" or "left":
                    prob = int(input("какой пробег у авто? "))
                    if prob <= 150000:
                        str(input("эту машину я готов купить не больше чем за 10000"))
                    elif prob <= 200000 and prob > 150000:
                        print("эту машину я готов купить не больше чем за 8000")
