import numpy as np

# initialise array with zero values
zero = np.zeros((2,2))
print(zero)

# initialise with zero
# you can also set the data type explicitly
# by default it is float64
one = np.ones(9, dtype=np.int64)
print(one)

# make an empty array whoose elements
# have undefined behaviour (it is faster)
empty = np.empty((3,2), dtype=np.int64)
print(empty)

# create an array with a range of elements:
arange = np.arange(1, 9, 2)
print(arange)

# write linearly spaced numbers in an interval
linspc = np.linspace(0, 30, num=21)
print(linspc)