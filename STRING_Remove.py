# Input from user
s = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Remove vowels and print remaining characters line by line
for ch in s:
    if ch not in vowels and ch.isalpha():
        print(ch)
