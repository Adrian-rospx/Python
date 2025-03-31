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

# scalar multiplication, called BROADCASTING
print(10 * data)

# broadcasting: performing operations on differently sized arrays
print (np.array([1,6,4,5]) * 2)

# useful operations:
print(data.max())
print(data.min(axis=1))
print(data.sum())

# aggregation functions
# mean:
mean = np.mean(data)
print(mean)
# prod (result of multiplying elements):
prod = np.prod(data)
print(prod)
# std - standard deviation
std = np.std(data)
print(std)