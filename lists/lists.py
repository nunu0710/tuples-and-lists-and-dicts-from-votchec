"""
Lists are ordered collections of items that can be changed or modified. 
They can contain items of different types and support indexing and slicing.
"""


# Creating a list
my_list = [1, 2, 3, "Python", 5.5] 
print(my_list)

# You can access items within a list based on the index. Index is starting from 0
print(my_list[3])

# checking the lenght of list
print(len(my_list))

# printing last item
print(my_list[-1])

# Adding elements
my_list.append("New Item") # add item at the of the list
print(my_list)

my_list.insert(3, 4) # insert an item inside a list, before the indexed passed as a first argument
print(my_list)

# Removing elements
my_list.remove("Python") # removing an item based on the value
print(my_list)

del my_list[0] # removing an item based on index
print(my_list)

my_list.pop(2) # removing an item based on index using .pop() function
print(my_list)