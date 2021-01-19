import os
import sys
import pprint
#To get current working directory
a= os.getcwd()
print(a)

#get filename
print(sys.argv[0])

#List all the fies recursively
import glob
b = glob.glob("D:\Learning\Python\PythonPrograms", recursive=True)
pprint.pprint(b)