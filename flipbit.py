
number = input("Enter a integer")
binary = bin(number)[2:]
nlength = len(binary) 
ones=binary.count("1")

indices_1 = [ i for i , v in enumerate(binary) if v == "1"]
indices_0 = [ i for i , v in enumerate(binary) if v == "0"]

replace_inde_0 = ''

# for idx,item in enumerate(binary):
#     if item == ''

	
