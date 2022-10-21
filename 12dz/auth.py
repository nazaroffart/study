dic = {input("введи логин: "): input("введи пароль: ")}

with open("database.txt") as file:
    lines = file.read().splitlines()
    aaa = {}
for i in lines:
    key,value = i.split(": ")
    aaa.update({key: value})
    for key, value in lines.items():
        if aaa == dic:
            print("ure in the system Neo")
        else:
            print("whore u??")

