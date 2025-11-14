lst = [25,10,45,30,15]
print("List:", lst)
print("Count of 10:", lst.count(10))
print("Index of 30:", lst.index(30))

lst.extend([50, 60])
print("After extend:", lst)

lst.pop()
print("After pop:", lst)

lst.clear()
print("After clear:", lst)
