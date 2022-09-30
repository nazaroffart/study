print('\nвсякие переменные\n')
"""love"""
l_flow = "Цветы"
l_pres = "Подарки"
l_ik = "Иссык-куль"
l_work = "Любовь к работе"
l_trips = "Совместные путешествия"
l = [l_flow,l_pres,l_ik,l_work,l_trips]
print("тут шото-то про любоф:")
for i in range(0,len(l)):
    print(l[i])
print('\n')

"""rel"""
r_paga = "Язычество"
r_god = "Бог"
r_all = "Аллах"
r_bibl = "Библия"
r_kora = "Коран"
r = [[r_paga],[r_god],[r_all],[r_bibl],[r_kora]]
print("тут шото про религии:", r, sep="\n")
print('\n')

"""cosm"""
c_aster = "Астероид"
c_sput = "Спутник"
c_ilon = "Илон Маск"
c_sun = "Солнце"
c_moon = "Луна"
c = [c_aster, c_sput, c_ilon, c_sun, c_moon]
print('тут уже поинтереснее, про космос:')
for n, line in enumerate(c, 1):
    if len(c) == n:
        print(line)
    else:
        print(line, end='=>')
print('\n')

"""auto"""
a_lamba = "Ламбаргини"
a_speed = "Скорость"
a_ferra = "Феррари"
a_trips = "Погнать в закат"
a_track = "Гоночный трек"
a = [a_lamba, a_speed, a_ferra, a_trips, a_track]
print("переменные с автомобилями:")
for auto in a:
    print(a)

"""nature"""
n_mounts = "Горы"
n_forest = "Лес"
n_river = "Река"
n_lake = "Озеро"
n_hike = "Поход"
n = [n_mounts, n_forest, n_river, n_lake, n_hike]
print("тут шото о природе")
print(n)
