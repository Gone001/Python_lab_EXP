#python tuple:-
'''
1. Built in data type
2. Immutable
3. ordered 
4. Support index method
5. ()-tuples donation 
6. t=()  - Empty tuple 
7. can hold elements with different data type 
8. Predefined methods for tuples :-index ,Count 
 
'''
t1=()   # empty tuple 
print(t1)
t2=(1)  # not a tuple it is an int  because we need to have , in the tuple between varaibles even only if a single varaible is present 
print(t2) 
t3=(1,)  #this is tuple because we have , after a varaible 
print(t3)
t4=(1.1)
print(t4) # not a tuple its a float 
t5=("abc",1,11,True,'a')
print(t5)
print(t5[2]) # tuple support indexing slicing and count methods

#t5[0]="vi"  # illegal because tuple are immutable 
print(t5.index(1)) # Index function will print the index value of element 
print(t5.count(1)) # count wil peint occurnece of elements in tuple 



# Dictionary 
'''
1.stores in key pairs
2.unordered sequence
3.does not support indexing 
4.{} donation 

'''


d3={
    "Student":{"Pant":234,"Shirt":453},
    "Tecahers":{"Shoe":334,"Belt":99}
    }

print(d3["Student"]["Pant"])
# Rules of keys and value 
# we can use any mutable data type for key 
# we can use any mutable or immutable data for values
# We can nest a dictionary inside a dictionary 
# predefined functions for dictionary 
# a.keys 
print(d3.keys())
print(d3.values())

