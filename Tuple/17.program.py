# tuple operations

# we cannot directly change anything in the tuple, if we want to change the tuple we can convert it to a list and make changes and then convert the list back to tuple
countries = ("India", "England", "Australia", "USA", "China")
temp = list(countries)
temp.append("Finland")
countries = tuple(temp)
# print(countries)

# we can concatenate two tuples
group1 = ("RSA", "AUS", "BAN")
group2 = ("IND", "NZ", "AFG")
totalTeams = group1 + group2
# print(totalTeams)

# count
nums = (1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 6)
print(nums.count(1))

# index
print(nums.index(6))

# we can use index in ranges also(if the element your are searching for is not present in the tuple the index method will throw value error)
print(nums.index(2, 3, 7))

# length
print(len(nums))