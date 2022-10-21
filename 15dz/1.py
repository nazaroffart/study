start = int(input("введи первое число: "))
end = int (input("введи второе число: "))

def sum_range(start, end):
    a = []
    if start > end:
        start,end = end,start
        for i in range(start,end+1):
            a.append(i)
            b = sum(a)    
    else:
        for i in range(start,end+1):
            a.append(i)
            b = sum(a)
    return b
print(sum_range(start,end))
