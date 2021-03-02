age = 18

if age >= 18:
    adult = True
else:
    adult = False

# Gives the same result as above
adult = True if age >= 18 else False

if adult:
    print("You're an adult")
else:
    print("You're not an adult")

# Gives the same result as above
print("You're an adult" if adult else "You're not an adult")

# Many ternary operators
num = 1000
print("The number is very large" if num >= 1000 else "The number is big" if num >= 100 else "Number isn't large but still positive" if num > 0 else "Number is negative")
