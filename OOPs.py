class Employee:

    number_of_employees=0
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.name = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.number_of_employees += 1

    def fullname(self):
        return "{} {} ".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)



emp_1 = Employee("Supriya", "Parandkar", 50000)
emp_2 = Employee("test", "user", 60000)

print (Employee.raise_amt)
print (emp_1.raise_amt)
