b = 100
c = 50
t = 5
b1 = 0
c1 = 0
t1 = 0
balance = 1000

while balance > 5:
    if balance > b:
        balance -= b
        b1 = b1 + 1
    if balance > c:
        balance -= c
        c1 = c1 + 1
    if balance > t:
        balance -= t
        t1 = t1 + 1

print(b1, c1, t1) 
print(balance)
