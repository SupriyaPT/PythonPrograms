class Employee(object):
    companyName = "Cummins"   #class variable

    def __init__(self,fname,lname):
        self.fname = fname  #Instance variable
        self.lname = lname
        print("Object Created Successfully")

    # factory method to create class object using different arguments

    @classmethod
    def from_string(cls,value):
        print("inside class method")
        fname, lname = value.split('-')
        return cls(fname,lname)

    # instance method to access instance variables
    def print_employee(self):
        print("Hey my full name is {0}.{1}".format(self.fname, self.lname))
        print ("Company name is {}".format(Employee.companyName))
        
        


e1=Employee('supriya','parandkar')
e1.print_employee()

e2= Employee.from_string("abc-xyz")
e2.print_employee()






        





