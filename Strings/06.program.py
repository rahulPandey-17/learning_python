# Basic String functions

names = "Rahul,Saurabh"

# Length
print("Length of the string : ", len(names))

# Slicing
# In slicing front index is inclusive and rear index is exclusive
print("Sliced string is : ", names[:5]) 
print("Sliced string is : ", names[6:])

# negative indexing in slicing
print("Using negative indexing for rear index : ", names[:-8]) # whever we use negative indexing python implicitly prefixes len(str) before the index. So it becomes len(names) - 8 = 5. So it is essentially same as names[:5]
print("Using negative indexing for front index : ", names[-13:5]) # it is same as len(names) - 13 = [0:5]