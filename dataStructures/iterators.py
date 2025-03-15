# iterators are objects with a countable number
# of values. Objects that can be iterated over
# contain __iter__ and __next__ methods that
# enable going through all the items in the object

import math

items = ["cow", "pork", "apple"]

# lists are iterable
# You can make a list iterator using iter()
it = iter(items)
# and traverse the list using the new keyword
print(next(it))
print(next(it))
print(next(it))

# example class:
class Array:
    def __iter__(self):
        self.val = 0
        return self

    def __next__(self):
        nw = math.sqrt(self.val)
        nw += 1
        self.val = int(pow(nw, 2))
        return self.val

arr = Array()
it = iter(arr)
# print the next statements
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))