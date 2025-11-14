n = int(input("Enter number of elements: "))
items = []
for i in range(n):
    val = input("Enter element: ")
    items.append(val)
t = tuple(items)
print("Tuple:", t)
