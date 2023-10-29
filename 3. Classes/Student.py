'''
Sources
https://github.com/ImKennyYip/Data-Structures-Algorithms
https://www.youtube.com/channel/UCdZQlE28wAgm6SKX_u9_L-Q
'''

#snake case - function names, variables def add_two
#camel case - class name, Student, CreditCard, and not credit_card

class Student:
    def __init__(self, name = "Anon", age = 18):
        self.name = name
        self.age = age
        self.courses = [] #CS1114, CS1134
    
    def add_course(self, course):
        if (course in self.courses):
            print("Student already enrolled")
        else:
            self.courses.append(course)
    
    #dunder method, dunder = double underscore, operator overloading
    def __str__(self):
        return "Name: " + self.name + "\nAge: " + str(self.age) + "\nCourses:" + str(self.courses)
    
    def __repr__(self):
        return "apple"

#fields attributes
#behavior - methods

#students = [["Kenny", 23], ["Bob", 15]]

s1 = Student(age = 23) #object is an instance of a class
print(s1.name, s1.age)
s1.add_course("CS1134")
s1.add_course("CS1134")
s1.add_course("CS1114")
s1.add_course("CS2124")

print(s1.courses)
print(s1)