#  Print out in each line the sum of homologous items of the two sequences.
#
import string

a = [1, 2, 3]
b = (4, 5, 6,8)



for i in range(0,3):
    print(a[i]+b[i])

#OR

for a_ele,b_ele in zip(a,b):
    print(a_ele+b_ele)



"""
Question: Create a script that generates a file where all letters of English alphabet are listed two in each line. The inside of the text file would look like:

ab
cd
ef

and so on.
"""

with open('sequence.txt', 'w') as file:
    for L1,L2 in zip(string.ascii_lowercase[0::2],string.ascii_lowercase[1::2]):
        file.write(L1+L2 + "\n")