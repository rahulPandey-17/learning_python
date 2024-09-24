# list methods

numbers = [12, 34, 56, 78, 90]

# append
numbers.append(55)
print(numbers)

# sort
# ascending
numbers.sort()
print(numbers)

#descending
numbers.sort(reverse=True)
print(numbers)

# reverse
numbers.reverse()
print(numbers)

# index(prints the index of first occurence of the element)
print(numbers.index(56))

# count
print(numbers.count(12))

# copy
num = numbers.copy()
print(num)

# insert
numbers.insert(1, 40)
print(numbers)

# extend
numbers.extend(num)
print(numbers)

# we can concatenate two lists using '+' operator
digits = numbers + num
print(digits)