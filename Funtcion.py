# example program to understand arguments :-
def addiion (x,y):
    return x+y

result=addiion(2,9)
print(result)

# example program on dafault parameters
def fun(x,y,z=0):
    return x*y*z

print(fun(2,4))  # python can not theow error when you set a default value for varaible as parameter  and forgett to give the argmnents 
                 # we need to initialize the value during parameter () 
                 
                 
'''def fun(x,y,z=0,a):  # here a give error because it is not initailized 
    return x*y*z

print(fun(2,4))
'''
# we cannot place rewuired parameters after optional
# parameters in function implementation, it will raise error




# program on argments 
# Sometimes we are not sure about number of parameter in python function 
# In advance ,eg :- A calculator for a flexible no of parameters  
# Multiplication of any no

def fun(*num):
    total=1
    for i in num:
        total*=i
    print(total)
fun(1,4,3,5,3,5,3)

def dictionary(**diction):
    for key , value in diction.items():
        print(f"{key}:{value}",type(key),type(value))
        
dictionary(name="Riya", id=24,city="Mumbai")

def outer(r):
    if r==1 or  r==0:
        return 1
    else:
        return r*outer(r-1)
    
print(outer(5))


# simple_otp.py
import random
import string

def generate_otp(length=6):
    digits = string.digits
    return ''.join(random.choice(digits) for _ in range(length))

if __name__ == "__main__":
    print("OTP:", generate_otp(6))
