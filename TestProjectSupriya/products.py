class Product:
    def __init__(self):
        self.name = "iPhone"
        self.description = "Its awesome"
        self.price = 700

    #Instance method to access instance variables

    def display(self):
        print(self.name)
        print(self.description)
        print(self.price)


p1= Product()
print(p1.description)
#or
p1.display()