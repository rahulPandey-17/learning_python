# sets

# does not allow repeated values(it is a unordered collection)
nums = {2, 4, 5, 5, 6, 7, 7}
# print(nums)

# we can create set with different data-types
random = {True, "Rahul", 17, None}
# print(random)

# creating a empty set
empty = {}
print(type(empty)) # this will give dict as output(since the syntax of set and dict is very similar to set both starts and ends with curly braces)

# to create a empty set we have to use set()
empty_set = set()
print(type(empty_set)) # this will give output as set

# we can access the values of a set through looping
# for number in nums :
    # print(number)