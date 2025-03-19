import numpy as np

# ! The desired reshaped array needs to have
# the same number of elements as the current one

a = np.arange(1, 13)
# reshaping requires entering the desired shape
mat = a.reshape((3,4))
print(mat)

# the np.reshape method gives more possibilities
# the default order is C-like
reshape = np.reshape(a, shape=(2,2,3), order="C")
print(reshape)

# Converting a 1D array to a 2D array
# (allows manual adjustments)
row_vector = a[np.newaxis, :]
print(row_vector.shape,'\n', row_vector)
# convert a 1d array into a row or column vector with a new axis:
col_vector = a[:, np.newaxis]
print(col_vector.shape,'\n', col_vector)

# expand an array by adding a new axis at a specified position
b = np.expand_dims(a, axis=1)
print(b) # creates a column vector

c = np.expand_dims(a, axis=0)
print(c) # creates a row vector