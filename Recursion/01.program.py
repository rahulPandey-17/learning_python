# factorial to demonstrate recursion

'''def factorial(num) :

    if num == 0 or num == 1 :
        return 1
    return num * factorial(num - 1)

num = int(input("Enter a number : "))
print(f"The factorial of {num} is {factorial(num)}")'''

# fibonacci series to demonstrate recursion

def fib(n) :

    if n == 1 :
        return 0
    if n == 2 :
        return 1
    return fib(n - 1) + fib(n - 2)

n = int(input("Enter the value of n : "))
print(f"The {n}th term of the series is {fib(n)}")