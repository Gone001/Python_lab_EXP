# Custom exception
class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    
    if num <= 0:
        raise NegativeNumberError("Number must be positive!")

except ValueError:
    print("That's not a valid number!")

except NegativeNumberError as e:
    print("Custom Exception:", e)

else:
    print("You entered a valid positive number:", num)