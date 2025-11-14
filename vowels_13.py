s = input("Enter a string: ")

vowels = sum(1 for c in s if c.lower() in "aeiou")
consonants = sum(1 for c in s if c.isalpha() and c.lower() not in "aeiou")
digits = sum(1 for c in s if c.isdigit())

print("Length:", len(s))
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
