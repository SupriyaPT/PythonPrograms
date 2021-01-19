list1 = [1,44,5,98,67,3,54]

for i in range (0,len(list1)):
    for j in range (i,len(list1)):
        if list1[j] < list1[i]:
            temp = list1[i]
            list1[i]= list1[j]
            list1[j] = temp

print("Sorted List", list1)
print("Second lowest number ", list1[1])
