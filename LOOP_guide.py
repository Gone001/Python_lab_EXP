# for loop and while loop 
"""Sytanx :-
   for varaible in sequence
   Statement
"""
'''
str="GOPAL SOURA"
for ch in str :
    print(ch)
'''


"""Parameters of print function in python """
'''
1.object (can print object and objects at the same time)
2.Seperator( want to place between object ,default is "" )
3.end(what to place at the end of print function, default is \n)

'''
# important ;-In python there is no char data type ,even with any dat only 1 char is string with length=1
'''
name ="hello"
d="12"
m="1"
y="2024"
print(d,m,y ,sep="-",end="")
'''
#Example program with Raneg function 

'''
Range Function with for loop provides sequental width to follow in ascending or descending order 
Overloads of range function:-
1.range(stop) starts with 0 to stop -1
2.range(start ,stop) start with start variable to stop -1
3.range(start,stop,step) start with value of start to stop -1 with no of steps to skip in ascending  or descending order  
'''

for i in range(4,10+1):
    print(i,end=" ")
print()
for i in range(20,10+1,-2):
    print(i,end=" ")
print()
for i in range (10):
    print(i)
    
# write a program to take range form user and print multiples of 3 in the range with sum and their count 
'''
r=int(input("Enter th range : "))
n=int(input("Multiple  of a no : "))
count=0
sum=0
for i in range(n,r+1,n):
    print(i,end=" ")
    count+=1
    sum+=i
print()
print(count)
print(sum)
'''
# while loop is similar to C programming but there is no increment or decrement operator 

#While loop to print all the natural no in the range 
'''
a=1
while a <=10:
    print(a,end=" ")
    a+=1
'''

# write a program to take range form user and print multiples of 3 and 5 using while loop
'''
r=int(input("Enter th range : "))
b=1
while b<=r:
    if b%3 and b%5 == 0:
        print(b,end=" ")
        b+=1
  '''
#jumping statements in python
''' these statements are used when our program i in continous motion to interrupt that motion ,we use jumping statements 
while compiler reads jumping statement its execution path interrupts and change 

1.Break:- to exit from single block (used when continously motion or a loop )
2.Continue:- Skip statemet palce after it 
3.Pass :-do nothing 

'''
#Example on break continue and Pass
i=1
while i<=20:
    print(i,end=" ")
    if i==3:
        break
    i+=1
print()

j=1
while j<=20:
    print(j,end=" ")
    if j==3:
        pass
    j+=1
print()
'''
z=1
while z<=20:
    print(z,end=" ")
    if z==3:
        continue
    z+=1
    '''
z = 1
while z <= 20:
    if z == 3:
        z += 1
        continue
    print(z, end=" ")
    z += 1

''' write a program to accept a range form user 
    if 5 is in range,print element 5 found in the range ,
    if a number multiple of 2 is in the range ,continue the loop
    if a number 0 is in the range do nothing 
'''



# for else loop :-
'''
1.Else statement with for loop 
2.Else statement with while loop
when we place else with for loop and while loop, on sucessful execution of for loop and while the statement placed inside the else statement will execute.
On any interupt of for and while loop else wil not execute
'''
import sys
print()
print()
for i in range (1,20):
    print(i,end=" ")
    if(i==13):
        break
else:              #here statement in else will execute as loop
                    #completed all its passes or iteration 
    print("Hello program end ")
    
    