# Python basic data structures (collections):
# lists, tuples, sets

#   lists are similar to dynamic arrays
# They store POINTERS to objects instead
# of values directly
items = ["apple", "pear", 3.14]
print(type(items))

#   Tuples are read-only data structures
# implemented as fixed arrays of references
# faster, use less memory
fixed = ("badger", 281, 2.71)

#   Sets are unordered collections of unique
# elements, implemented as a hash table
# Fast membership testing; enables set operations
setted = {125, "Hyphen", 8.08}

# example operations:
items.append("caramba")
items.insert(1, 888)
items.pop()
items.reverse()

print(items)