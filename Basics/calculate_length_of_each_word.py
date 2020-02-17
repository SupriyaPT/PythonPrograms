def my_func(word):
    return len(word)


result = map(my_func, ('apple', 'banana', 'cherry'))

print(result)

#convert the map into a list, for readability:
print(list(result))


