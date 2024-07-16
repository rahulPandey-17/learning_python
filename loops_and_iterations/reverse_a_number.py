# program to reverse a given number(while loop)

number = int(input("Enter the number : "))
rev = 0
num = number

while num > 0 :
    rev = (rev * 10) + (num % 10)
    num //= 10

print("Reverse of", number, "is", rev)