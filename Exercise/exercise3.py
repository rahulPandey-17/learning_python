questions = [
    "Who developed Python Programming Language",
    " Which type of Programming does Python support?",
    "Is Python case sensitive when dealing with identifiers?",
    "Which of the following is the correct extension of the Python file?",
    "Is Python code compiled or interpreted?",
    "What will be the value of the following Python expression?"
]

options = [
    ["Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom"],
    ["object-oriented programming", "structured programming", "functional programming", "all of the mentioned"],
    ["no", "yes", "machine dependent", "none of the mentioned"],
    [".python", ".pl", ".py", ".p"],
    ["Python code is both compiled and interpreted", "Python code is neither compiled nor interpreted", "Python code is only compiled", "Python code is only interpreted"],
    ["7", "2", "4", "1"]
]

answers = ["3", "4", "2", "1", "1"]

money = 0

print("Welcome to python quiz")

for question in range(len(questions)) :

    print("\nQ. ", end = "")
    print(questions[question], end = "\n\n")

    for option in range(len(options[question])) :
        print(f"{option + 1}. {options[question][option]}")
    
    ans = input("\nEnter the answer : ")

    if ans == answers[question] :
        money += 100000
    else :
        print("\nWrong Answer!!")
        break
print(f"Total Earnings = {money}")