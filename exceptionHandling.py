# python exception handling keywords:
#   raise
#   try
#   except

# error examples: ValueError, NameError, Type Error
#                 IndexError

def verifyAge(age: int):
    if age < 0:

        # raise signals an error 
        # and disrupts the program
        raise ValueError("Age cannot be negative")
    
    print(f"You are {age} years old.")

# try blocks are used for attempting
# execution and catching errors
try:
    verifyAge(-3)
# exceptions handle edge cases
# and enable the program to keep functioning
except ValueError as e:
    print(e)