English=float(input("Enter the marks of English :"))
Hindi=float(input("Enter the marks of Hindi :"))
maths=float(input("Enter the marks of Maths :"))
Science=float(input("Enter the marks of Science :"))
SSt=float(input("Enter the marks of SST :"))

Result=(English+Hindi+maths+Science+SSt)/5
print(int(Result))
if(Result>=90):
    print("A grade ")
elif(Result<=89):
    print("B+ grade")
    