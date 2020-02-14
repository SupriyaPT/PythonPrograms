class Patient:
    def setId(self,id):
        self.id =id

    def getId(self):
        print(self.id)

    def setName(self,name):
        self.name =name

    def getName(self):
        print(self.name)

    def setSsn(self,ssn):
        self.ssn =ssn

    def getSsn(self):
        print(self.ssn)

p=Patient()
p.setName("John")
p.setId(1)
p.setSsn("5ag2")

p.getId()
p.getName()
p.getSsn()