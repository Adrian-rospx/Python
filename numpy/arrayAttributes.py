import numpy as np
import math

# 2d array:
a = np.array([[1,2,3],
              [4,5,6],
              [9,8,7],
              [4,5,12]])

# number of dimensions in an array:
dims = a.ndim
print(dims)

# shape returns a tuple of intagers specifying
# the number of elements in each dimension
shape = a.shape
print(shape)
print(len(a.shape) == a.ndim)

# size attribute contains the fixed total number
# of elements inside the array
size = a.size
print(size)
print(a.size == math.prod(a.shape))

# arrays are typically homogenous and their datatype
# is stored in the dtype attribute:
datatype = a.dtype
print(datatype) # int64 for 64 bit intager