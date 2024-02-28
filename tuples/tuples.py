"""
Tuples are ordered collections similar to lists, but they are immutable, 
meaning they cannot be changed once created. Tuples are faster than lists 
and are used to protect the data from being changed.
"""

# Creating a tuple
my_tuple = (1, 2, 3, "Python", 4.5)

# Accessing elements
print(my_tuple[3])  # Output: Python

# Slicing tuples
print(my_tuple[1:4])