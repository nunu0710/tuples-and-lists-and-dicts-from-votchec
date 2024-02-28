"""
Sets are unordered collections of unique elements. 
They are useful for operations involving the checking of whether an item is part of a set, 
and they support mathematical operations like union, intersection, difference, and symmetric difference.
"""

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements
my_set.add(6)

# Removing elements
my_set.remove(2)

# Set operations
another_set = {4, 5, 6, 7, 8}
print(my_set.union(another_set))  # Union
print(my_set.intersection(another_set))  # Intersection

print(my_set)
