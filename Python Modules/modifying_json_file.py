import json

with open('file_data.json', 'r+') as file:
    dev_dict = json.load(file)
    dev_dict['employees'].append({'firstName': 'S', 'lastName': 'P'})
    print(dev_dict['employees'])
    file.seek(0,0)
    json.dump(dev_dict,file,indent=4)