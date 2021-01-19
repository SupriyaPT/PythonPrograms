arr = [1, 4, 2, 6]
x = lambda i: (bin(i).count('1'),i)
sorted(arr, key=x)
y= lambda i: bin(i).count('1')
sorted(arr, key=y)