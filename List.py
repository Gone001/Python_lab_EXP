list="Gopal",32,90.45,"soura"
nolist=("gopal","soura",56,78,44,23.3443434343)
print(type(list))
print(type(nolist))
print(list[0])
a=list[0]
print(a.upper())


name = "Rahul"
age = 21

print(f"My name is {name}, I am {age}")  # f-string (modern)
print("My name is {}, I am {}".format(name, age))  # format method
print("My name is %s, I am %d" % (name, age))      # old style


text = "  Python Programming  "

print(text.lower())     # '  python programming  '
print(text.upper())     # '  PYTHON PROGRAMMING  '
print(text.strip())     # 'Python Programming' (remove spaces)
print(text.replace("Python", "Java"))  # '  Java Programming  '
print(text.split())     # ['Python', 'Programming'] (split by spaces)
print("-".join(["2025", "09", "06"]))  # '2025-09-06'

