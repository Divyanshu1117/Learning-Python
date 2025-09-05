# Explicit TypeCasting
a = "1"
b = "2"
# a = 1
# b = 2
print(int(a) + int(b))

string = "15"
# string1 = "15D"
number = 7
string_number = int(string) # Throws an error if the string is not a valid integer
sum = number + string_number
print("The Sum of both the number is: ", sum)

# Implicit TypeCasting
c = 1.9
d = 8
print(c + d)

# Python automatically converts a to int
a1 = 7
print(type(a1))

# Python automatically converts b to float
b1 = 3.0
print(type(b1))

# Python automatically converts c to float as it is a float addition
c1 = a + b
print(c1)
print(type(c1))