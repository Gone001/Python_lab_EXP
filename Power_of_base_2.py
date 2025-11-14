base=int(input("Enter the base no :"))
power=int(input("Enter the powr or exponent :"))

count=0
blank=1

while count<power:
    
    blank=blank*base
    count+=1
    
print("The base power of %d is : " % base ,blank)