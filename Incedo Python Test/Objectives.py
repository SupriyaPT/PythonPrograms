def foo(k):
    k=[1]
q=[0]
foo(q)
print(q)    #[0]

######################################################
dictionary1 = {'Google':1, 'Facebook':2, 'Microsoft':3}
dictionary2 = {'GFG':1, 'Microsoft':2, 'Youtube':3}
dictionary1.update(dictionary2)

for key,values in dictionary1.items():
    print(key,values)

'''
Google 1
Facebook 2
Microsoft 2
GFG 1
Youtube 3 '''
#######################################################

value=[1,2,3,4,5]

try :
    value = value[5]/0
except(IndexError, ZeroDivisionError) :
    print('GeeksforGeeks', end='')
else:
    print('GFG', end='')
finally:
    print('Geeks', end='')

#GeeksforGeeksGeeks

########################################

class A:
    def __init__(self):
        self.__i = 1
        self.j = 5

    def display(self):
        print(self.__i, self.j)

class B(A):
    def __init__(self):
        super().__init__()
        self.__i = 2
        self.j = 7

c = B()
c.display()   #[1,7]
