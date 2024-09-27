# fstrings

# before fstrings

text = "Hey my name is {0}, and i am from {1}."

name = "Rahul"
country = "India"

print(text.format(name, country))

# using fstring
print(f"Hi my name is {name}, and i am from {country}.")

# if we have to literally print the name of the variable, we can do that using fstring
print(f"Hi my name is {{name}}, and i am from {{country}}.")