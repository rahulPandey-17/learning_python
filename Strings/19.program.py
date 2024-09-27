# docstrings

def square(num) :

    '''Takes a number and squares it'''
    return num ** 2

num = int(input("Enter the number : "))
print(square(num))

# we can print the docstrings, it is not like comments python treats docstrings differently
print(square.__doc__)