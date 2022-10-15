"""
a = open('python.txt', "r")
t_words = []
b = a.read()

for i in b:
    items = b.split(" ") 
    print(items)
    break
"""
t_words = []
with open("python.txt") as file:
    read = file.readlines()
    r_str = "".join(read)
    spl = r_str.split()
    for i in spl:
        if "t" in i:
            t_words.append(i)
        if "T" in i:
            t_words.append(i)
    print(t_words)
