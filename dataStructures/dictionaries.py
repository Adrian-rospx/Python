# dictionaries are a hash map-like 
# data type used for storing 
# key-value pairs

Cars = {'Toyota' : ['Hilux','Corolla'], 
        'Dodge'  : ['Charger', 'Challenger'],
        'Dacia'  : ['Duster', 'Sandero', 'Logan']}
Cars['Ford'] = 'Mustang'
# .update(new lists) method enables changing 
# multiple elements of a dictionary
print(Cars)

# can be indexed by their key:
print(Cars['Dacia'])
# but also using the get method which
# returns none if the index is not found
print(Cars.get('Chevrolet'))

# the length is the number of keys
print(len(Cars))

# traversing a dictionary:
for key, value in Cars.items():
    print(key, value)