class Programmer:
    # def __init__(self, name, salary, technology):
    #     self.name = name
    #     self.salary = salary
    #     self.technology = technology

    #Use getter and Setter method to set instance variable

    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def setSalary(self, sal):
        self.salary = sal

    def getSalary(self):
        return self.salary

    def setTechnologies(self, techs):
        self.technologies = techs

    def getTechnologies(self):
        return self.technologies


p1=Programmer()
p1.setName("John")
p1.setSalary(1000)
p1.setTechnologies(["java","python"])

print(p1.getName(), p1.getSalary(), p1.getTechnologies())