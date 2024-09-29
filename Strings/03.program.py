# String Methods

# Strings are immutable in python

string = "Rahul"

# lower
print(string.upper())

# upper
print(string.lower())

# strip, we have three variants of strip
text = "!!!!Rahul!!!!"

# rstrip(removes from the right)
print(text.rstrip("!"))

# lstrip(removes from the left)
print(text.lstrip("!"))

# strip(removes from both sides)
print(text.strip("!"))

# replace(replaces all occurences)
print(string.replace("Rahul", "Saurabh"))

# split(converts string into a list)
names = "Rahul Saurabh Alok Harshit"
print(names.split(" "))

# capitalize(makes the first character of the string into upper case and the rest to lowercase)
heading = "python"
print(heading.capitalize())

# count(count occurences in a string)
print(heading.count("p"))

# endswith(to check if the string ends with the given value)
print(text.endswith("!!!!"))
# we can also find a value between the string by giving indices to the endswith() method
print(text.endswith("a", 4, 6))

# find(searches for the first occurence of a given string and return it's index)
print(text.find("R"))

# index(it is pretty similar to the find method with the only exception being it will raise a error if the given value is not found instead of returning -1)
# print(text.index("Z"))

# isalnum(to check if a string is alpha numeric(and no other special character))
print(text.isalnum())

# isalpha(to check if a string contains only letters)
print(string.isalpha())

# isupper and islower
print(string.isupper())
print(string.islower())

# isprintable(tells if all the character in the string is printaible or not, like if a escape sequence is present in the string it will return false as it does not print on the console)
escape = "Rahul\n"
print(escape.isprintable())

# isspace(returns true if the string contains only white spaces)
spaces = "  "
print(text.isspace())
print(spaces.isspace())

# istitle(returns true only if the first letter of each word in the string is capital)
title = "To Kill A Mockingbird"
print(title.istitle())

# title(converts the string into a title by capitalizing the first letter of each word)
book = "as a man thinketh"
print(book.title())

# swapcase(converts lower case to uppercase and vice versa)
print(string.swapcase())