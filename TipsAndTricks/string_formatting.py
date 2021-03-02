name = "Mike"
age = 25
number = 3.14 

# String Formating
print("Hello my name is " + name + " and I am " + str(age) +  " years old!")
print("Hello my name is %s and I am %d years old! The PI number is %.2f"% (name, age, number))
print("Hello my name is {} and I am {} years old!".format(name, age))

# F Strings
print(f"Hello my name is {name} and I am {age} years old!")
# Cut digits after comma
print(f"Hello my name is {name} and I am {age} years old! The PI number is {number:.2f}")
# The code in the breckets alse works
print(f"Hello my name is {name} and I am {age if age % 2 == 0 else 0} years old!")