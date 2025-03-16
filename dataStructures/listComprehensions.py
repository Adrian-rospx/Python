# list comprehensions are a way of making
# lists using a single line of code

# example: creating a list of all squares from 1 to 40
squares = [x**2 for x in range(1,41)]
print(squares)

# selecing only the numbers divisible by 6 from the list
sixdiv = [num for num in squares if num % 6 == 0]
print(sixdiv)

# compute cartesian product of two sets:
A = [1, 5, 12]
B = [4, 6, 9]

cart = [(a, b) for a in A for b in B]
print(cart) # outputs 9 sets (3x3)