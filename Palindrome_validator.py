print(f" {s}is Palindrome" if (s:=input("Enter string: ")) == s[::-1] else f"{s} is Not Palindrome")
