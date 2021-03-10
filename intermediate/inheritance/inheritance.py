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


# Class inheritance
class Student(Person):

    def __init__(self, name, age, height, scholarchip):
        super(Student, self).__init__(name, age, height)
        self.scholarchip = scholarchip
    
    # Overriding
    def __str__(self):
        text = super(Student, self).__str__()
        text += f"\nScholarship: {self.scholarchip}"
        return text

    def calc_yearly_scholarship(self):
        return self.scholarchip * 12


person1 = Person("John", 25, 190)
print(person1.name, person1.age, person1.height)

person1.age = 26
print(person1)

person2 = Person("Ann", 22, 170)
print(Person.amount)

# Deletes object
del person1

print(Person.amount)

print("--------------------------")

student1 = Student("Rayan", 19, 185, 1000)
print(student1)