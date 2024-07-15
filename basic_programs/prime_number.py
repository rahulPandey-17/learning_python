num = int(input("Enter the number : "))

flag = 0
if num < 2 :
    print(num, "is not a prime number")
else :
    for i in range(2, (num // 2) + 1) :
        if num % i == 0 :
            flag = 1
            break
    if flag == 0 :
        print(num, "is a prime number")
    else :
        print(num, "is not a prime number")