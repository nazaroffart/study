a = int(input("введи начальное число: "))
b = int(input("введи конечное число: "))

def rec_fack(a,b):
    fak = 1
    for i in range(a,b+1):
        fak *= i
    
        def pali(fak):
            n = str(fak)
            v = n[::-1]
            print(v)
       
    return pali(fak)



print(rec_fack(a,b))
