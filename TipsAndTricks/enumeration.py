names = ["John", "Mike", "Ann", "Bob", "Sara"]

# Enumerate assigns indexes
# It creates a list of tuples
print(list(enumerate(names)))
print(dict(enumerate(names)))

for index, name in enumerate(names):
    print(f"{index}: {name}")
