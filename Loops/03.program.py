# for loop with else

'''for numbers in range(1, 11) :
  print(numbers)
else :
  print("Completed")'''

'''for items in [] :
  print(items)
else :
  print("No items")'''


# if we break the loop before completion of all the iterable values, else block will not execute

for numbers in range(1, 11) :
  if numbers == 6 :
    break
  print(numbers)
else :
  print("Loop completed without interruption")