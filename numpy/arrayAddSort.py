import numpy as np

arr = np.array([2,1,5,7,3,9,8,6, 4])

# sort an array:
sort = np.sort(arr)
print(sort)

# in addition to sort there are:
# argsort - indirect sort that returns the indices that would sort the array
# lexsort - indirect stable sort
# searchsorted - finds elements in a sorted array
# partition - partial sort

# concatenate both lists and arrays:
a = np.array([[1,6,4,8,2], [9,8,7,6,5]])
b = np.array([[7,5,2,9,5]])

conc = np.concatenate((a,b), 0)
print(conc)