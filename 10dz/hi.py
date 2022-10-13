

try:
    x = 0+"err"
except SyntaxError and TypeError:
    print(444)

a = [2,3,4,5,6,"i",7,8]
b = []
for i in a:
    b.append(True)
print(b)

for i in a:
    c = str(i)
    z = set(c)
    print(c)

for i in a:
    if type(i) == int:
        b.append(False)
    else:
        b.append(i)



try:
    set.all(a)
    print("true")
except:
    print(False)