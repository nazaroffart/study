a = input("login: ")
b = input("pass: ")
with open("users.txt", "w") as file:
    file.write(a)
    file.write(b)
