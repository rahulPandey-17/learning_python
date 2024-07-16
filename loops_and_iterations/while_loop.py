# program to demonstrate the working of a while loop

'''n = 5
while n > 0 :
    print(n)
    n -= 1
print("Blastoff")
print(n)'''

# code snippet to demonstrate the break statement

'''while True :
    line = input("> ")
    if line == "Done" :
        break
    print(line)
print("Finished!")'''

# code snippet to demonstrate continue statement

while True :
    line = input("> ")
    if line[0] == "#" :
        continue
    if line == 'done' :
        break
    print(line)
print("Done!")