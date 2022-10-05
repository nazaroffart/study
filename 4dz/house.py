geo = str(input("Район: "))
geo_low = geo.lower()
if geo_low != "чон арык" or "байтик" or "ортосай":
    print("\nэти районы нам не подходят")
else:
    mat = str(input("Кирпич или бетон: "))
    mat_low = mat.lower()
    if mat_low == "кирпич":
        uch = float(input("Сколько соток участок: "))
        if uch <= 4:
            price = int(input("Цена: "))
            if price <= 50000:
                print("\nкак раз то, что нужно")
            else:
                print("\nэто не то, что мы выбираем")
        else:
            print("\nэто не то, что мы выбираем")
    elif mat_low == "бетон":
        uch = float(input("Сколько соток участок: "))
        if uch <= 5:
            price = int(input("Цена: "))
            if price <= 45000:
                print("\nкак раз то, что нужно")
            else:
                print("\nэто не то, что мы выбираем")
        else:
            print("\nэто не то, что мы выбираем")
    else:
        print("\nэто не то, что мы выбираем")
