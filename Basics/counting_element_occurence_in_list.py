# Exercise Question 4: Given a list iterate it and count the occurrence of each element and create a dictionary to show the count of each element

sampleList = [11, 45, 8, 11, 23, 45, 23, 45, 89]

output_dict={}

for i in range(0, len(sampleList)):
    if sampleList[i] not in output_dict.keys():
        output_dict[sampleList[i]] = 1

    else :
        output_dict[sampleList[i]] +=1


print(output_dict)