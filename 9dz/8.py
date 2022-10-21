a = int(input())
b = str(a)
c = "1"
for i in c:
    if a > 99 and a <= 999:
        print("число трехзначное")
        
    if a > 0 and a % 2 == 0:
        print("число положительное и четное")
    
    if a % 31 == 0:
        print("число делится на 31 без остатка")


