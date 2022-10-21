file = open("text.txt", 'a+')

file.write("ну шо ты там")
print(file.read())

file.close()



with open("text.txt", "rb") as file:
    for i in file:
        print(file.read())
