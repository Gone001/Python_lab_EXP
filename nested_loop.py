 # nested loop 
 
''' loop inside a loop 
on every execution of outer loop innner loop will completely executes 

.0000000000000003333333333333333333333eg :-For loop inside for loop\
    2. while loop inside while loop 
    3. while loop inside for loop 
'''
"""
..........
for i in range (1,6):
    print(f"{i}  :=")
    print()
    for j in range (1,6):
        print(j, end=" ")
        
    print("\n")
   """
# Q print star the star will increase by incrase in line 

n=int(input("Enter the no "))
for i in range (1,n+1):
    for j in range (1,i+1):
        print("*",end=" ")
    print()

n=int(input("Enter the no "))
for i in range (n,1,-1):
    for j in range (i,0,-1):
        print(j,end=" ")
    print()
    
n=int(input("Enter the no "))
for i in range (n,1,-1):
    for j in range (i,1,-1):
        print("*",end=" ")
    print()

n = int(input("Enter a number: "))

i = n
while i > 0:
    j = 0
    while j < i: # pass j increase and i decrease 
        print("*", end=" ")
        j += 1
    print()   
    i -= 1
