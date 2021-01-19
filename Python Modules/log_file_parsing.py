import re
line_number = 0
with open('test.txt', 'r') as file:
    for line in file:
        line_number += 1
        if "ERROR" in line:
            print(line_number, ": " , line)
