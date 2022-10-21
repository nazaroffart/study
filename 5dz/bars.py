a = "Сидел барсук в своей норе и ел картошечку пюре"
"""1"""
print(a)
"""2"""
list(a)
print("\n",len(a))

"""3"""
print("\n",a+".")

"""4"""
if a.find("ре"):
    print("\nре есть в в строке")

"""5"""
list(a)
print("\n",a[-1])

"""6"""
a_wrds = a.split(" ")
print("\n",len(a_wrds))
