# List of strings
l = ['sat', 'bat', 'cat', 'mat']

'''Expected output [['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]'''

new_list = list(map(list, l))
print(new_list)
