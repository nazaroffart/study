dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
try:
    for x in dict_.keys():
        x + 'abc'
except TypeError:
    for x in dict_.keys():
        if type(x) == int:
            print(str(dict_))