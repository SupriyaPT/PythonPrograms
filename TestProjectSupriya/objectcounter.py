class ObjectCounter:

    #Static field
    numberofObjects=0

    def __init__(self):
        #Accesing static field from instance method
        ObjectCounter.numberofObjects+=1


    #Static method

    @staticmethod
    def displayCount():
        print(ObjectCounter.numberofObjects)



o1= ObjectCounter()
o2=ObjectCounter()
print("number of objects created {0}".format(ObjectCounter.numberofObjects))