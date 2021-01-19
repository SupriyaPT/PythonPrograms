import json

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}


with open("file_data.json",'w') as f:
    json.dump(d,f,indent=4)


json_string = json.dumps(d,indent=4)
with open("file_data_dumps.json",'w') as f:
    f.write(json_string)

