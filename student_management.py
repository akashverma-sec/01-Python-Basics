# Student Management System

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("\n----- Student Details -----")
        print("Name   :", self.name)
        print("Age    :", self.age)
        print("Course :", self.course)


name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
course = input("Enter Course: ")

student1 = Student(name, age, course)

student1.display()
