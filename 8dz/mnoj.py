a = (1,3,5,6)
name = set(a)
name1 = {4,5,6,7}

print(name , name1)

print(name-name1)
print(name&name1)
print(name.intersection(name1))

hey = name.discard(5)
print(hey)
