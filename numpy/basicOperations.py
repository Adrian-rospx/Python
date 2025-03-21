import numpy as np

data = np.array([[1,6,5,4],
                 [9,4,7,3]])
ones = np.ones((2,4), dtype=int)

# perform addition between arrays:
add = data + ones
print(add)

# perform all basic operations:
sub = data - ones
mult = data*ones*2
div = data / 2
print(mult)
print(div)

# sum of all array elements:
s = np.sum(data)
print(s)
# sum over one axis:
# over rows:
print(data.sum(axis=0))
# over columns:
print(data.sum(axis=1))