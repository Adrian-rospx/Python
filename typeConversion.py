# In python, type conversion can be 
#   explicit: i.e. using int()
#   implicit: 1/2

def half(num):
    return num/2

response = input("type a number: ")

print("Initial data type:")
print(type(response))

# explicitly converting a string to a number:
response = int(response)

print("After conversion:")
print(type(response))

# intager implicitly converted to a float
print(f"The type of {half(response)} is:")
print(type(half(response)))

