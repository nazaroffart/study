a = [1,2,3]
b = (4,5,6)
c = [7,8,9]
a_set = set(a)
b_set = set(b)
c_set = set(c)

abc = set([frozenset(a),frozenset(b),frozenset(c)])
print(type(abc))

d = frozenset([1341,1345,4653])
abc_add = abc.add(d)


print(abc, type(abc))
