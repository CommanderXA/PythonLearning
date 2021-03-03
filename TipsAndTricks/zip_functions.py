names = ['John', 'Ann', 'Rayan', 'Lucy', 'Robert']
ages = [17, 23, 78, 34, 53]

# 1
for i in range(len(names)):
    print(f"Name: {names[i]}, Age: {ages[i]}")

# 2
for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")

sales = [500, 800, 300, 1200, 600]
costs = [200, 600, 200, 1000, 800]

for sale, cost in zip(sales, costs):
    print(sale - cost)

# "*" used for unzipping
zipped = [('Mike', 50), ('Bob', 20), ('Ann', 20), ('Robert', 34)]
names, ages = zip(*zipped)

print(list(names))
print(list(ages))

letters = ['b', 'd', 'a', 'c']
nums = [3, 2, 4, 1]

data = sorted(zip(letters, nums))
print(data)

letters, nums = zip(*data)
print(letters)
print(nums)

mydict = dict(zip(letters, nums))
print(mydict)
