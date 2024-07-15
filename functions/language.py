def greeting(lang) :
    if lang == "es" :
        print("ola")
    elif lang == "fr" :
        print("bonjour")
    else :
        print("hello")

print("First function")
greeting("es")
greeting("fr")
greeting("en")
print()

# function with return values
def greets() :
    return "Hello"

print("Second function")
print(greets(), "Rahul")
print(greets(), "Saurabh\n")

# we can now write the first function as follows with return statement
def greet(lang) :
    if lang == "es" :
        return "Ola"
    elif lang == "fr" :
        return "Bonjour"
    else :
        return "Hello"
    
print("Third function")
print(greet("es"), "Rahul")
print(greet("fr"), "Rahul")
print(greet("en"), "Rahul\n")