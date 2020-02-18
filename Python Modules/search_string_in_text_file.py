import re

file = open('test.txt', 'r')
line_number=0
for line in file:
    line_number += 1
    if (re.match("(.*)(p|P)ython(.*)",line)):
        print("String Found {} on line no. {}".format(line,line_number ))

file.close()
