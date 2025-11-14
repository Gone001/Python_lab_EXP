num=int(input("Enter the no :"))
check=0
temp=num
digits=len(str(num))
while temp>0:
    digit=temp%10
    check+=digit**digits
    temp//=10
print(f"{num} is an Armstrong "if check==num else f"{num} is not an Armstrong no ")