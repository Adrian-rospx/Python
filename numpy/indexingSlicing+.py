import numpy as np

a = np.arange(11)
print(a)

# create a new array by sectioning an
# already existing one
arr1 = a[3:8]
print(arr1)

# stack two arrays
a1 = np.array([[1, 2],
               [3, 4]])
a2 = np.array([[5, 6],
               [7, 8]])

# stack vertically:
print(np.vstack((a1,a2)) )
# stack horizontally:
print(np.hstack((a1,a2)) )

# you can split a large array:
s = np.arange(1, 25).reshape(2,12)
print(s)
# split into three equal parts (horizontally):
print(np.hsplit(s, 3))
# split after the 3rd and 4th column:
print(np.hsplit(s, (3,4)))

# create an vIEW of a section of an array
# to reference the same data in memory:
s = np.reshape(s, (4,6))
b1 = s[0]
b2 = s.copy()[0, :]
print(s)
# notice how the view affects the original item
b1[0] = 99
print(s)
# using copy actually copies the data wanted
print(b2)