num = int(input("Enter the number : "))

number = num
rev = 0
while number > 0 :
    rev = (rev * 10) + (number % 10)
    number //= 10

print("Reverse of", num, "is :", rev)