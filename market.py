item1=int (input("Enter the price of item 1: "))
item2=int (input("Enter the price of item 2: "))
item3=int (input("Enter the price of item 3: "))
item4=int (input("Enter the price of item 4: "))
item5=int (input("Enter the price of item 5: "))
item5=int (input("Enter the price of item 5: "))
item6=int (input("Enter the price of item 6: "))
item7=int (input("Enter the price of item 7: "))
item8=int (input("Enter the price of item 8: "))
item9=int (input("Enter the price of item 9: "))
item10=int (input("Enter the price of item 10: "))
total_price = item1 + item2 + item3 + item4 + item5 + item6 + item7 + item8 + item9 + item10
print("Total Price of all items: ", total_price)

if(total_price>2000):
    print("You are eligible for discount")
    discount = total_price * 20/100
    print("Your discount is: ", discount)
    print("total price after discount is: ", total_price - discount)

else:print("Thank you for the shooping ")