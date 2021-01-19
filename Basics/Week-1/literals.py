a = 0b1010 #Binary Literals
b = 100 #Decimal Literal Prefix'0b' or '0B'
c = 0o310 #Octal Literal Prefix'0o' or '0O'
d = 0x12c #Hexadecimal Literal Prefix'0x' or '0X'

#Float Literal
float_1 = 10.5
float_2 = 1.5e2

#Complex Literal
x = 3.14j

#When we print the variables, all the literals are converted into decimal values.
print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)


#When converting from float to integer, the number gets truncated (integer that is closer to zero).
print(int(-2.8))
