# generators are a python feature that 
# enables creating iterators on-demand ("lazy")
# in a memory efficient way

# use yield instead of return
def count_to(n: int):
    count = 1
    while count <= n:
        yield count
        count += 1

# the function call returns a generator object memory address
gen = count_to(10)
print(gen)
# the next method iterates through the generator
print(next(gen))
print(next(gen))
print(next(gen))
print('')

# usage in loops
for num in count_to(7):
    print(num)

# generators enable making infinite sequences
# they are faster 
# and more efficient