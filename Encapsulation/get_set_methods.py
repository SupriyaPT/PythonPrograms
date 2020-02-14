class Student:
    def setId(self,id):
        self.id =id

    def getId(self):
        print (self.id)

    def setName(self,name):
        self.name=name

    def getName(self):
        print(self.name)



s=Student()
# s.name="Supriya"
# s.name="John"
# print(s.name)
s.setName("Supriya")
s.setId(12)


s.getName()
s.getId()

