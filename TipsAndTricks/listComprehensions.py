nums = [18, 16, 22, 99, 23, 11, 54]

new_list = []
for num in nums:
    if num % 2 == 0:
        new_list.append(num)

print(new_list)

# More right way
new_list_2 = [num for num in nums if num % 2 == 0]
print(new_list_2)

# manupulating with result
numbers = [1,2,3,4,5,6,7]
powers_of_two = [2**x for x in numbers]
print(powers_of_two)

words = ["auto", "car", "anger", "fox", "anchor"]
words = [word.upper() if word.startswith('a') else word for word in words]
print(words)
