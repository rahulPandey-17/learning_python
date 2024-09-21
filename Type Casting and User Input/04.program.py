a = "2"
b = "4"

# normal string contatination

print(a + b)

# type-casted output

print(int(a) + int(b))

# Implicit conversion

num1 = 10
num2 = 10.2

print(num1 + num2) # will convert the result into float, as it offers more precision

# Taking a user input

# print("Enter your name : ", end = "")
# name = input() # it is the most basic form of input

# we can also put a text to console inside of input and reduce the syntax and increase readibility

name = input("Enter your name : ")

print("Your name is " + name)