# Input strings
a = input("Enter first string: ")
b = input("Enter second string: ")

print("\nConcatenation:", a + b)
print("Repetition:", a * 3)
print("Length:", len(a), len(b))
print("Is b in a?", b in a)
print("First char of a:", a[0], "| Last char of b:", b[-1])
print("Uppercase a:", a.upper(), "| Lowercase b:", b.lower())
print("Comparison:", "Equal" if a==b else "a>b" if a>b else "a<b")
