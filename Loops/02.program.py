# program implementing while loop

# import random

# randomNumber = random.randint(1, 100)
# guesses = 0

# while True :

#     num = int(input("Guess the number (1-100) : "))
#     guesses += 1

#     if num < randomNumber :
#         print("Guess higher")
#     elif num > randomNumber :
#         print("Guess lower")
#     else :
#         print("Congrats, you found the number in", guesses, "guesses.")
#         break

# we can use else with a while loop

number = 5

while number > 0 :
    print(number)
    number -= 1
else :
    print("After the condition becomes false in while loop, now i am inside the else block")