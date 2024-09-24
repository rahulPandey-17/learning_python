# tuples are immutable

nums = (12, 45, 78, 89)
# nums[2] = 33 # not allowed

# "in" is used in tuple same as in lists
countries = ("India", "Australia", "England", "Germany")

if "England" in  countries :
    print("Present")
else :
    print("Not present")

# we can use slicing in tuples
print(nums[1:3])