a = input("введи слово: ")
rev = a[::-1]
print(rev)

def pali(a):
    global rev
    while True:
        if rev == a:
            print("палином")

        elif rev != a:
            print("не палином")
        break
print(pali(a))
