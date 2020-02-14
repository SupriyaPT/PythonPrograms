#Outer class
class Car:
    def __init__(self,make, year):
        self.make =make
        self.year =year

    #Inner class
    class Engine:
        def __init__(self, number):
            self.number=number
        def start(self):
            print ("Engine started")

c1=Car("BMW",2017)
e = c1.Engine(123)
e.start()