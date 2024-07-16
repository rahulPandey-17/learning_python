# program to print the sum of natural numbers upto the given input(while loop)

n = int(input("Enter the number you want the sum upto : "))
'''number = 1
sum = 0

while number <= n :
    sum += number
    number += 1

print("Sum of all the natural numbers upto", n, "is", sum)'''

# program to print the sum of natural numbers upto the given input(for loop)

sum = 0

for number in range(1, (n + 1)) :
    sum += number

print("Sum of all the natural numbers upto", n, "is", sum)