"""
folder with any file type ….. {'ext':4,'txt':6,'py':2}'
"""
import os
import glob

dir_files = os.walk(r'C:\Users\supriya.parandkar\.PyCharmEdu2018.2\config\scratches\test')
fileTypesDir = {}

for  root_dir, sub_dirs, files in dir_files:
    for file in files:
        split_filename = file.split(".")
        if split_filename[1] in fileTypesDir.keys():
            fileTypesDir[split_filename[1]] = fileTypesDir[split_filename[1]] + 1
        else:
            fileTypesDir[split_filename[1]] = 1

print(fileTypesDir)

list_all_files=glob.glob(r'C:\Users\supriya.parandkar\.PyCharmEdu2018.2\config\scratches\test\*')
print(list_all_files)
result_dict={}
for ele in list_all_files:
    if os.path.isfile(ele):
        name, ext = os.path.splitext(ele)
        if ext in result_dict.keys():
            result_dict[ext]= result_dict[ext]+1
        else:
            result_dict[ext]=1

print("result_dict",result_dict)



highest_count = 0
second_highest_count = 0
highest_count_type=[]

for type in fileTypesDir.keys():
    if fileTypesDir[type] >= highest_count:
        highest_count = fileTypesDir[type]
        highest_count_type.append(type)

print("Highest Count types are {} with count {}".format(highest_count_type,highest_count ))

highest_count_type.clear()
for type in fileTypesDir.keys():
    if fileTypesDir[type] < highest_count and fileTypesDir[type] > second_highest_count:
        second_highest_count = fileTypesDir[type]
        highest_count_type.append(type)


print("Second Highest Count types are {} with count {}".format(highest_count_type,second_highest_count ))





