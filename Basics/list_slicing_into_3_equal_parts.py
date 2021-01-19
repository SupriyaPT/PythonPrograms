# Exercise Question 3: Given a list slice it into a 3 equal chunks and rever each list

sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]

start = 0
end=3
final_list=[]
for i in range(0,3):
    list=sampleList[start:end]
    list.reverse()
    final_list.append(list)
    start = end
    end = end+3

print(final_list)


length = len(sampleList)
chunkSize  = int(length/3)
start = 0
end = chunkSize
for i in range(1, 4, 1):
  indexes = slice(start, end, 1)
  listChunk = sampleList[indexes]
  print("Chunk ", i , listChunk)
  print("After reversing it ", listChunk[::-1])
  start = end
  if(i != 2):
    end +=chunkSize
  else:
    end += length - chunkSize