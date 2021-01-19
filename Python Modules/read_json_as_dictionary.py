import json

#load take file pointer as an argument, however loads does not take file pointer as argument. It takes object as argumet


with open('file_data.json','r') as f:
    dictionary_read = json.load(f)

print(dictionary_read)

"""
Sometimes we receive JSON response in string format. So to use it in our application, we need to convert JSON string into a Python dictionary.
"""

developerJsonString = """{
    "name": "jane doe",
    "salary": 9000,
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "Web Development"
    ],
    "email": "JaneDoe@pynative.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}
"""

developerDict = json.loads(developerJsonString)
print(developerDict)