# set methods

nums1 = {1, 2, 5, 6, 8}
nums2 = {5, 7, 9, 10}

# union
# print(nums1.union(nums2))

# since the union methods returns a new set without changing any of the original sets used, to update a particular set we can use update() method
# nums1.update(nums2)
# print(nums1)  # update method is essentially (union update), it first performs the union operation on sets and then updates the desired set with the result

cities = {"Tokyo", "Madrid", "Berlin", "Mumbai"}
cities1 = {"Chennai", "Tokyo", "Madrid", "Kanpur"}
cities2 = {"Tokyo", "Berlin"}

# intersection
# print(cities.intersection(cities1))  # prints the common values of both the sets

# intersection_update
# cities.intersection_update(cities1)
# print(cities)

# symmetric_difference
# print(cities.symmetric_difference(cities1))  # prints all the values that are not common in both the sets

# symmetric_difference_update
# cities.symmetric_difference_update(cities1)
# print(cities)

# difference
# print(cities.difference(cities1))  # prints the values that are only present in the original set(in this case cities) and not in both sets

# difference_update
# cities.difference_update(cities1)
# print(cities)

''' in-built set methods '''

# isdisjoint()
# print(cities.isdisjoint(cities1))  # (two sets are said to be disjoint if they have no elements in common), so it will return False

# issuperset()
# print(cities.issuperset(cities1))  # (checks if a set contains all the elements of another set(not few but all elements))

# issubset()
# print(cities2.issubset(cities))

# add()
# cities2.add("Helsinki")  # adds a single item to a set
# print(cities2)

# remove()/discard()
# cities2.remove("Helsinki")
# print(cities2)

# cities2.discard("Helsinki")  # will not raise any error
# cities2.remove("Helsinki")   # remove will raise a error if you try to delete a value that is not present in the set

# pop()
# print(cities.pop())  # removes any random value from the set
# print(cities)

# del(not a method but a keyword)
# del cities2     # use to remove a entire set
# print(cities2)  # will raise a error as cities2 no more exists

# clear()
# cities2.clear()  # it is used when we don't want to delete a entire set, but want to remove all values inside it
# print(cities2)

# we can use if to check weather a value exists in a set or not

if "Mumbai" in cities :
    print("Present")
else :
    print("Absent")