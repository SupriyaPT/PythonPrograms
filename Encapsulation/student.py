class Student:
    def __init__(self):
        #private variable
        self.__id =123
        self.__name="John"
        #public variable
        self.class_name="first"

    #To access private variables
    def display(self):
        print(s.__id )  #private variables can be accessed from within the class
        print(s.__name)

s=Student()
# print(s.id)    #Error, private variables can not be accessed directly from outside the class using instance variables
# print(s.name)    #Error

#print(s.class_name)  #Can be accessed without error

#using instance method  to access private variables
s.display()


#Or you can use name mangling , other way of accessing
print(s._Student__id)
