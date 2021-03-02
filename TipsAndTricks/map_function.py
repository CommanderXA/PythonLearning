nums = [14, 23, 8, 12, 2, 5, 90]

def square(x):
    return x * x

new_list = []
for i in nums:
    new_list.append(square(i))

print(new_list)

# The same result
new_list = [square(i) for i in nums]
print(new_list)

new_list = map(square, nums)
print(list(new_list))
