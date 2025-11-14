import ast
n = ast.literal_eval(input("Enter the list: "))
largest = n[0]
for i in n:
    if i > largest:
        largest = i
print("Largest:", largest)
smallest = n[0]
for i in n:
    if i < smallest:
        smallest = i
print("Smallest:", smallest)
n.sort()
print(n)
n.sort(reverse=True)
print(n)
