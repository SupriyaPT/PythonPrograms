'''Using map for single argument function'''

def calculate_square(n):
    return n*n

tuple1 = (1,2,3,4)

result = map(calculate_square, tuple1)

print(result)
# print(tuple(result))  # converting map object to tuple
# print(list(result))  # converting map object to list
print(set(result))    # converting map object to set

list1 = [5,3,8]

result2 = list(map(calculate_square, list1))

print(result2)


'''Using map for multiple argument function'''


def multiply(n,z):
    return n*z


list1 = [1,2,3,4]
list2 = [1,2,3,4]
result = map(multiply, list1, list2)

print(result)

print(list(result))  # converting map object to list
