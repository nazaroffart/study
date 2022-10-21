list_1 = ['name', 'age', '1', '19']
def rev(a):
    global list_1
    x = list_1[:int(len(list_1)/2)]
    y = list_1[int(len(list_1)/2):]
    z = x[::-1]+y[::-1]
    return z
print(rev(list_1))
