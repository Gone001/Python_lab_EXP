'''
String slicing :- used to extract a portion of string using []
Syntax 
[starts : stop :step ]
traversal on tring can be done using indexing ( method to traverse individual elements with its index value 0 starts with 0)
'''
'''
str='hello world'
print(str[0])#print element at index 0 means first element 
print(str[0:])#print element 0 onwards (positive indexing left to right )
print(str[-1])#negative indexing (Right to left )
print(str[:-1])#print from last character onwards
print(str[1:3])# print element at last index 1 this will print second and third element 
print(str[1:6:2])# start ith index 1 upto index 5 with step 2
print(str[::-1])#reverse the whole string 

# topic :-list data structure 
'''
'''
1. list in pythin is a ordered and follow sequencial storage of elements 
2. Mutable type (means allow changes even after initialization 
3. Hetrogenous data structure store elements with multiple data types (eg int , float ,string )
4. Empty will be represented by [] .eg list[]
5  we can also nest a list inside another list as element eg.list =[1,['a','b'],3.5]
6. Elements of list are stored in a ordered and sequental manner eg.list =[1,2,4,5,6,7]
     1 is at index 0
     2 is at index 1
7. list can store duplicte values list =[1,1,1,3,3,3,3]
8. Constructor () function with list we can use name of list to print all elements of list 
'''
''''
list1=[1,1,1,3,3,3,3,]
print(list1)
list =[1,2.3,"kiran",'aadi','-',0.0002]
list2=[int(True),False,"Hii"]
print(list)
print(list2)
# exampe to store data inside the list in runtime mode

list3=[]           # empty list 
e=int(input("Enter total numbers "))     # Maximum no of elements to store in list 
for i in range(e): # i will iterate from 0 to e
    n=int(input("Enter :"))
    list3.append(n) # method to store the element inside list during  runtime mode
    
print(list3)
print(f"No of first element in list is {list3.count(n)}")
list3.sort() # sort the list 
print(list3)
list3.reverse() # reverse the sorted list 
print(list3)

'''

#Predefined functions for list data Structures 
'''
1.index() : return the position of the element in a list 
2.count() : Count accurance of elements in a list 
3.Sort () : Sort list elemnets in ascending order 
4.sort(Reverse=True ):sort in descending order 
5.appned() : add a new element in the end of the list 
6.extends([]) :add multiple items in a list 
7.pop() : remove elements from at specific index (default position in last , if not specified)
8.clear() : delete all elements of the list 
9.delete() : delete by indes value 
10. insert() add elements at specific position 
'''
import time
# Create an initial list
my_list = [10, 20, 30, 40, 50]
start_time = time.time()
print(id(list))

# 1. index(): Return the position of an element
print("Index of 30:", my_list.index(30))  # Output: 2

# 2. count(): Count occurrences of an element
my_list.append(20)
print("Count of 20:", my_list.count(20))  # Output: 2

# 3. sort(): Sort list elements in ascending order
my_list.sort()
print("Sorted list:", my_list)  # Output: [10, 20, 20, 30, 40, 50]

# 4. sort(reverse=True): Sort list in descending order
my_list.sort(reverse=True)
print("Descending order:", my_list)  # Output: [50, 40, 30, 20, 20, 10]

# 5. append(): Add a new element at the end
my_list.append(60)
print("After append:", my_list)  # Output: [50, 40, 30, 20, 20, 10, 60]

# 6. extend([]): Add multiple elements to the list
my_list.extend([70, 80])
print("After extend:", my_list)  # Output: [50, 40, 30, 20, 20, 10, 60, 70, 80]

# 7. pop(): Remove element at specific index (default last)
removed_element = my_list.pop()  # Removes last element
print("Popped element:", removed_element)
print("After pop:", my_list)

# Remove element at index 2
my_list.pop(2)
print("After popping index 2:", my_list)

# 8. clear(): Delete all elements from the list
temp_list = my_list.copy()
temp_list.clear()
print("After clear:", temp_list)  # Output: []

# 9. delete by index (using del)
del my_list[1]  # Delete element at index 1
print("After delete by index:", my_list)

# 10. insert(): Add element at specific position
my_list.insert(1, 25)  # Insert 25 at index 1
print("After insert:", my_list)

# 11. Reverse the list 
my_list.reverse()
print("Reverse order:", my_list)  # Output: [70, 60, 50, 40, 30, 20, 20, 10]

print(id(list))
end_time = time.time()
execution_time_ms = (end_time - start_time) * 1000
print(f"Execution time: {execution_time_ms:.3f} ms")


