# wrappers are pieces of code used to modify 
# the behavior of an existing function

# decorators are used to extend functions and methods
# without altering the existing code

def f1(func):
    def wrapper(*args, **kwargs):
        print("Start")
        val = func(*args, **kwargs)
        print("End")
        return val
    
    return wrapper

# In Python, functions are objects 
# When printed, they return memory addresses
print(f"f1: {f1}")

def f(a):
    print(f"Hello, {a}")

# the wrapper just adds extra 
# features to a function

f1(f)("Adi") # output: Start  Hello  End

# decorated function:
@f1
def fext(a):
    print(f"Hello, {a}")

fext("Adi") # same output as the last mix of functions

@f1
def fext2(x,y):
    return x + y

print(fext2(12, 65)) # example with return values