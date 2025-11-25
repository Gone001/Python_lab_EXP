my_dict = {"a": 10, "b": 20, "c": 30}

key_to_update = "b"
new_value = 99

if key_to_update in my_dict:
    my_dict[key_to_update] = new_value
    print("Updated:", my_dict)
else:
    print("Key not found.")
