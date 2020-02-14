from course import Course

class Student(Course):
    #Static variable
    major="CSE"

    def __init__(self, rollno, name):
        #Instance variables
        self.rollno=rollno
        self.name=name



s1=Student(1,"John")
s2=Student(2,"Bill")

#Accessing class variable using class name
print(Student.major)

#Accessing static variable using class object
print(s1.major, s1.name, s1.rollno)
print(s2.major, s2.name, s2.rollno)