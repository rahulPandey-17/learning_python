# functions

# calculating geometric mean of two numbers

'''def gmean(num1, num2) :

    return (num1 * num2) / (num1 + num2)

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

print(f"The geometric mean of {num1} and {num2} is {gmean(num1, num2)}")'''

# greater of two numbers

def greater(num1, num2) :

    if num1 > num2 :
        return num1
    return num2

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

print(f"{greater(num1, num2)} is the greater of the two numbers")