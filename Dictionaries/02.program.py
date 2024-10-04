# Dictionary Methods

employee = {
  1001 : 88,
  1002 : 90,
  1003 : 76,
  1004 : 95
}

# update()

employee_2 = {
  2002 : 66,
  2004 : 98
}

employee.update(employee_2)
print(employee)

# clear() {clears the dictionary}
employee_2.clear()
print(employee_2)

# pop() {removes the key-value pairs passed as argument}
employee.pop(1003)
print(employee)

# popitem() {removes the last key-value pair from the dictionary}
employee.popitem()
print(employee)

# del {to delete a entire dictionary}
# del employee  {if key is not provided, it will delete the entire dictionary}
del employee[1004]  # {if key is provided, it will delete the mentioned key-value pair}
print(employee)