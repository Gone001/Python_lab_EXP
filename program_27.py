
fruits = {"Apple", "Banana", "Cherry", "Mango", "Orange"}

print("Original Set:")
print(fruits)
fruits.discard("Banana")
print("\nAfter using discard('Banana'):")
print(fruits)
fruits.remove("Cherry")
print("\nAfter using remove('Cherry'):")
print(fruits)
removed_item = fruits.pop()
print(f"\nAfter using pop() (removed '{removed_item}'):")
print(fruits)
