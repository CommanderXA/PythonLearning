# One parameter
mysquare = lambda x: x * x
print(mysquare(5))

# Two parameters
mysum = lambda x, y: x + x
print(mysum(5, 5))

# We can pass collections
mysum = lambda *args: sum(args)
print(mysum(5, 5, 10, 20))

# Saved nowhere. Can be used when neccessery
print((lambda x: x ** 3)(5))

# Passing lambda as a parameter to functions
nums = [8, 66, 12, 14, 15, 7, 99, 109, 88, 76]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)

nums = [8, 66, 12, 14, 15, 7, 99, 109, 88, 76]
even_nums = list(map(lambda x: x ** 2, nums))
print(even_nums)

# Returning a callable function
def myfunction(num):
    return lambda x: x * num

ten_multiplier = myfunction(10)
print(ten_multiplier(20))