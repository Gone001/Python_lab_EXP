sub1=float(input("Enter the marks of English :"))
sub2=float(input("Enter the marks of Hindi :"))
sub3=float(input("Enter the marks of Maths :"))
sub4=float(input("Enter the marks of Scinece :"))
sub5=float(input("Enter the marks of Social Science :"))
total=sub1+sub2+sub3+sub4+sub5
percentage =(total/500)*100
print("\n")
print("The total marks of 5 subjects is :",int(total))
print("The percentage of 5 subjects is :",percentage)
if(percentage>=90):
    print("The grade is A")
elif(percentage>=80):
    print("The grade is B")
elif(percentage>=70):
    print("The grade is C")
elif(percentage>=60):
    print("The grade is D")
elif(percentage<35):
    print("He is failed ")