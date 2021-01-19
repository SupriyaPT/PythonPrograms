#Create an English to Portuguese translation program.
d = dict(weather = "clima", earth = "terra", rain = "chuva")
def eng_to_portuguese(word):
    return d[word]

# while True:
#     input_word = input("Enter a word : ")
#     if input_word in d.keys():
#         print("Translated value : ",eng_to_portuguese(input_word))
#     else:
#         print("We couldn't find that word!")
#
#OR
input_word = input("Enter a word : ").lower()
try:
    print("Translated value : ",eng_to_portuguese(input_word))
except KeyError:
    print("We couldn't find that word!")

