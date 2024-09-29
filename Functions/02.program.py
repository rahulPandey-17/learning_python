# function arguments

# default arguments(useful when the values are not passed to a function)
def average(num1 = 12, num2 = 25) :
    return (num1 + num2) / 2

# required arguments
def average(num1, num2) :
    return (num1 + num2) / 2

# variable length arguments
def average(*numbers) :  # it will take numbers as tuple as the parameter

    sum = 0
    for number in numbers :
        sum += number
    print(f"The average of the numbers is {sum/len(numbers)}")

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))

# print(f"The average of the two numbers is {average()}")
# print(f"The average of the two numbers is {average(num1, num2)}")
average(5, 6, 7, 1)