for i in range(-100,100):
    a = []
    if i % 13 == 0 and i % 2 == 0:
        a.append(i**7)
    c = i+7
    
    b = []
    if c % 2 != 0:
        b.append(i)
    if True:
        print(len(a)>0,len(b)>0)


