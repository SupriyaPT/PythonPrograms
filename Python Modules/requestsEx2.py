import  requests

response = requests.get("http://www.pythonhow.com/data/sampledata.txt")
# text_response = response.text
print(response.content)

#
# import requests

response = requests.get("http://www.pythonhow.com/data/universe.txt")
response.raise_for_status()
text = response.text
count_a = text.count("a")
print(count_a)