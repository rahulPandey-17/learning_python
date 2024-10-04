info = {
  "name" : "Rahul",
  "age" : 24,
  "isEligible" : True
}

# accessing dictionary items

# a particular item
'''print(info["name"])  # it will throw error if key dosen't exists
print(info.get("name"))  # it will not throw error if the key is not in dictionary(will return null)

# if you want to access all the keys
print(info.keys())

# you can use for loop as well
for key in info.keys() :
  print(key)

# if you want to access a;; the values
print(info.values())

# you can use for loop as well
for value in info.values() :
  print(value)'''

# accessing key-value pairs
print(info.items())