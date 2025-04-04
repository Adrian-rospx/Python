# lambdas are anonymous functions
# used in line for one-off functions that do not repeat
# used in functional programming

def add(x, y):
    return x+y
print(add(4,5))

print((lambda x, y: x+y)(4,5))

(lambda x: print(x))("Hello")