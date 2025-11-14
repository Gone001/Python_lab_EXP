lst = [25, 10, 45, 30, 15]

print("List:", lst)
print("Length:", len(lst))
print("Is 30 in list?", 30 in lst)
print("Sorted list:", sorted(lst))

lst.reverse()
print("Reversed list:", lst)

copy_lst = lst.copy()
print("Copied list:", copy_lst)
