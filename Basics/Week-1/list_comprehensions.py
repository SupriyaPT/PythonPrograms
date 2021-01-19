#Get table of 2
table_of_2 = [2 * x for x in range(1, 11)]
print(table_of_2)

#square of numbers
power_of_2 = [x ** 2 for x in range(91,101)]
print(power_of_2)


# list which extracts numbers from string
string = "my phone number is : 11122 !!"
string_list = string.split()
print(string_list)
print("\nExtracted digits")
numbers = [x for x in string_list if x.isdigit()]
print(numbers)
