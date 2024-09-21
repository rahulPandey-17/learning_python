# Simple Calculator

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

print("\nBelow are your operator choices :\n")
print("1. Addition (+)\n2. Subraction (-)\n3. Division (/)\n4. Multiplication (*)")
print("5. Exponent (**)\n6. Remainder (%)\n")

choice = input("Enter your choise : ")

if choice == "1" :
    print("Result : ", (num1 + num2))
elif choice == "2" :
    print("Result : ", (num1 - num2))
elif choice == "3" :
    print("Result : ", (num1 / num2))
elif choice == "4" :
    print("Result : ", (num1 * num2))
elif choice == "5" :
    print("Result : ", (num1 ** num2))
else :
    print("Result : ", (num1 % num2))