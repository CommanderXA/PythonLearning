dict1 = {'a': 1, 'b': 7}
dict2 = {'b': 4, 'c': 8}

# Can't assign the value of it into a variable
dict1.update(dict2)
print(dict1)

# -----------------

dict3 = {**dict1, **dict2}
print(dict3)

# -----------------

dict3 = dict(dict1.items() | dict2.items())
print(dict3)

# possible in only python 3.9
dict3 = dict1 | dict2
print(dict3)
