class A(object) :
    def abc(self):
        var1 = "DDDD"
        print "from class A :"
    def __init__(self):
        self.name = "supriya_A" 

class B(object):
     def abc(self):
        print "from class B :"
     def __init__(self):
        self.name = "supriya_B"         

class C(object):
    def abc(self):
        print "from class C :"
    def __init__(self):
        self.name = "supriya_C"                 

class D(A, B, C):
    def __init__(self):
        self.name = "supriya_D"
        C.__init__(self)
    def abc(self):
        A.abc(self)
        B.abc(self)
        C.abc(self)
        print "from class D :"
        

        

obj1 = D()
obj1.abc()
print obj1.name
