name = "Rahul Pandey"
print("Hey, " + name)

print('Rahul codes in "C++" and "Python"\n')

# Multi-line string

print("""The random. choice() function is used in the python string to generate the sequence of characters and digits that can repeat the string in any order. Create a program to generate a random string using the random. choices() function.""")

# Since string is a sequence of characters we can access individual characters of the string via indices

print("\nAccessing the string via indices :")

string = "Python"

# print(string[0], end = "")
# print(string[1], end = "")
# print(string[2], end = "")
# print(string[3], end = "")
# print(string[4], end = "")
# print(string[5], end = "\n")

# we can also print the above string using for loop, also it's recommended that way as is it cleaner and efficient for long strings

for character in string :
    print(character, end = "")
print()