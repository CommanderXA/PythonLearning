# "any" function checks a collection and if one element of this collection 
# returns True then "any" returns True

# "all" function returns True if all elements of given collection are True

x = [True, True, False, True]
print(all(x)) # False
print(any(x)) # True

nums = [1, 5, 7, 9]

even = lambda x: x % 2 == 0

result = [even(num) for num in nums]
if any(result):
    print("At least one number is even.")
else:
    print("No number is even.")

if all(result):
    print("All numbers are even.")