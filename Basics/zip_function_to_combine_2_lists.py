"""Exercise Question 5: Given a two list of equal size create a set such that it shows the element from both lists in the pair"""

firstList = [2, 3, 4, 5, 6, 7, 8]
print("First List ", firstList)

secondList = [4, 9, 16, 25, 36, 49, 64]
print("Second List ", secondList)

result_set=set()

for i,j in zip(firstList,secondList):
    result_set.add((i,j))

print(result_set)

"""OR"""

result = zip(firstList, secondList)
print(result)
resultSet = set(result)
print(resultSet)