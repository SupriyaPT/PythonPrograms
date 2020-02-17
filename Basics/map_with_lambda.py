'''Passing single iterator to map with lambda'''

numbers = [1,2,3,4]

result = map(lambda n : n*n, numbers)
print(set(result))  # converting map object to set

'''Passing Multiple Iterators to map() Using Lambda'''
num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))
