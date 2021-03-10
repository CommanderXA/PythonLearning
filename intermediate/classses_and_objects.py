class Person:

    amount = 0

    # Constructor
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        # Person because we reffering to the whole class
        Person.amount += 1

    # Destructor
    def __del__(self):
        Person.amount -= 1
        print('Object has been deleted.')

    # str function
    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nHeight: {self.height}"


person1 = Person("John", 25, 190)
print(person1.name, person1.age, person1.height)

person1.age = 26
print(person1)

person2 = Person("Ann", 22, 170)

print(Person.amount)

# Deletes object
del person1

print(Person.amount)
