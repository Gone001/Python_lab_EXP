class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}")


# Creating (instantiating) objects of Student class
s1 = Student("Gopal", 21, "BCA")
s2 = Student("Rahul", 20, "B.Tech")
s3 = Student("Neha", 22, "MBA")

# Calling method using objects
s1.display_info()
s2.display_info()
s3.display_info()
