import numpy as np

a = np.array([[1 , 2, 3, 4], 
              [5, 6, 7, 8], 
              [9, 10, 11, 12]])
# numpy arrays can indexed just like python lists
print(a[1, :3])

# you can print all items that fulfill a condition:
print(a[a < 5])

# it is possible to select a view of elements
# and use it to index an array
five_up = (a>=5)
print(a[five_up])

even = a[a%2 == 0]
print(even)

# you can select using multiple conditions
# with the & and | operators
c = a[(a>7) | (a%2==0)]
print(c)

# the boolean operators |, & may also be used to 
# specify whether an element fulfills a specific conditions
odd = (a%2 == 1) | (a > 10)
print(odd)

# this returns the indices of the items that are less
# than zero. It returns a tuple of two arrays:
#   the first one is the row indices where they were found
#   the second one is the column indices 
b = np.nonzero(a < 5)
print(b)

# for a list of coordinates:
coordinate_list = list(zip(b[0], b[1]))
for coord in coordinate_list:
    print(coord)

# you can also print the values with:
print(a[b])

# indices are left empty if they do not exist in the array
missing = np.nonzero(a == 42)
print(missing)