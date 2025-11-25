my_dict = {"a": 10, "b": 20, "c": 30}
key_to_delete = "b"
print("Original dictionary",my_dict)
if key_to_delete in my_dict:
    del my_dict[key_to_delete]
    print("Updated:", my_dict)
else:
    print("Key not found.")
