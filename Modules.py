'''
# Module in python 

1.Modules are files which includes classes and function (user defined or inbuilt)
2.Extention is .py but not all because some modules are built in java ,C++ and other languages bv
'''
# importance :-
'''
1.provide cod reusability 
2.Easy to manage 

'''
# types of modules in pyhton 
'''
1.user defined module (.py) reuse with import statement 
2.predefined modules (alredy pyhton setup )

Build-in 
System libreary 
Third party modules (installed uisng pip ) 

'''

# how to list moduels installed in a system 
'''
help('modules')  # list all the moduels including the third party 

# how to list name of module using third party module using dependancy manager 

import math 
print("Square root of 16",math.sqrt(16))
import os 
import datetime
import sys

dir(sys)
# used to list module name 
# command list name of module 
# Q which command is used to check module name of a function 
print(sys.builtin_module_names)

print(len(sys.builtin_module_names))
# How to check or list built in module names 



# How to check the file or module type in pyhton 
print(sys.prefix)
# sys.prefix command is used to retrieve file location of a module 
# command to check physical condition of module (the file is .py not but here we can list only .py files )

print(os.__file__)
# print(math.__file__) # developed in C not supported by _file_ command 

# write a program to implement built in math module and use predefine function of math modules in programm 
res=math.factorial(6)
print(res)
'''
from even import check
numbers=[24,3,2,4,2,6,5,7,8]
output=check(*numbers)
print(output)