# Class Example

class Student:
    pass

student1 = Student()

print(student1)

# Constructor Example

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Akash", 22)

print("Name:", student1.name)
print("Age:", student1.age)

# Method Example

class Student:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello,", self.name)

student1 = Student("Akash")

student1.greet()