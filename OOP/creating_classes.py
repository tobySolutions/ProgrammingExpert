"""
Notes:

- An attribute is data associated with an instance of an object.

- All Datatypes are classes. When we use them, we are actually instantiating a class.

- Attributes can be referenced using the dot notation:
    const my_person = Person("tolu") 
    print(my_person.name)

- "Class attributes" are shared by all instances (objects) of a class.

- "Instance attributes" may have a different value for each and every instance (object) that was created.

- "self" binds to an instance of a class. It references it.

- A "constructor" is a function that will be called when a new instance (object) is created. We use the "__init__" method to declare such functions; the __init__ method is called on instantiation of an object.

- "Encapsulation" in OOP refers to how one can prevent outside access to the details of a class. 
It could be to abstract implementation thereby simplifying or to just prevent misuse of attributes and methods.
"""

# Classes examples:

# class Fruit:
#   def __init__(self, name, calories):
#      self.name = name
#      self.calories = calories


# my_fruit = Fruit("Apple", 12483)    

# print(my_fruit.name, my_fruit.calories)  # Apple 12483
    
    

# Creating and accessing attributes:

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age


# person_one = Person("Tobi", 21)    
# person_two = Person("Solutions", 29)

# person_one.gender = "Male"
# person_two.gender = "Female"
# person_one.name = "Tobiloba"

# print(person_one.name, person_one.age, person_one.gender)  # Tobiloba 21 Male
# print(person_two.name, person_two.age, person_two.gender)  # Solutions 29 Female


# __init__ method:

# class Person:
#   def __init__(self, value):
#     self.value = value


# person_one = Person(10)    
# person_two = Person(25)

# print(person_one.value)  # 10
# print(person_two.value)  # 25
    

# class Person:
#   def __init__(self):
#     print("Bawo ni")

# person_one = Person()


# Creating classes:

# class Person:
#   pass


# person_one = Person()

# print(person_one)  # <__main__.Person object at 0x7fe3e8619df0>

# print(type(person_one))  # <class '__main__.Person'>


