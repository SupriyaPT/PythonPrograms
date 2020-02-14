class Course:
    #Parameterized constructor
    def __init__(self, name, rating):
        self.name = name
        self.rating= rating

    #Instance method
    def calculate_average_ratings(self):
        #local variable
        number_of_ratings = len(self.rating)
        average = sum(self.rating)/number_of_ratings
        print ("Average ratings for {0} is {1}".format(self.name, average))

c1=Course("Java", [1,2,3])
print(c1.name)
print(c1.rating)
c1.calculate_average_ratings()

c2=Course("Python",[4,5,5])
print(c2.rating)
print(c2.name)
c2.calculate_average_ratings()