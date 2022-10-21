keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']


dic = {
        keys[0]: values[0],
        keys[1]: values[1],
        keys[2]: values[2]
        }


colors = {"GreenYellow":"#ADFF2F","Chartreuse":"#7FFF00","LawnGreen":"#7CFC00"}

dic.update(colors)
print(dic)
