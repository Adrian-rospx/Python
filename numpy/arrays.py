import numpy as np

# Numpy documentation
# https://numpy.org/doc/stable/

# NumPy (Numerical Python) is a fundamental Python library for 
# data manipulation and matrix/array computatons

# unlike lists, arrays are homogenous data structures
# that only stores data of the same type
aList = [1, 3, 5, 12]
a = np.array([1,5,9,15,13,18])

# unlike arrays, when created by accessing other arrays 
# they use REFERENCES instead of copying the array
# See: "VIEWS"
bList = aList[:2]
b = a[:3]
bcopy = a[:3].copy()

aList[1] = 256
a[1] = 256

print(bList)
# notice how these are different:
print(b)
print(bcopy)

# Higher order dimensional arrays:
mat = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(mat)