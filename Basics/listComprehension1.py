'''

Find vowels in a sentence

normal list comprehension
new_list = [expression for member in iterable]

list comprehension with conditional logic. You can place the conditional at the end of the statement for simple filtering
new_list = [expression for member in iterable (if conditional)]

'''

sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']
print("Number of vowels in sentence ", len(vowels))
