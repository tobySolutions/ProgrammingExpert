"""
Notes:

- A method is a function defined inside of a class definition.

- A method is a function that acts on an instance of a class.

- There are three important kinds of methods: 
    - Instance methods
    - Class methods
    - Static methods

- Methods inside of a class require that "self" be the first parameter so that they can bind to a specific instance of that class
"""



# Method examples:

# class Counter:
#   def __init__(self):
#     self.count = 0
#     self.locked = False

#   def toggle_lock(self):
#     self.locked = not self.locked  

#   def increment(self):
#     if self.locked:
#       raise Exception("The counter is locked!")
#     self.count += 1
    
#   def decrement(self):
#     if self.locked:
#       raise Exception("The counter is locked!")
#     self.count -= 1

#   def print_count(self):
#     print(f"The current count is {self.count}")

# counter_one = Counter()
# counter_two = Counter()


# counter_one.increment()
# counter_one.decrement()

# counter_one.increment()
# counter_one.increment()
# counter_one.increment()

# counter_one.print_count()  # The current count is 3


# counter_two.increment()
# counter_two.decrement()

# counter_two.increment()
# counter_two.increment()

# counter_two.print_count()  # The current count is 2
    




# Getter methods:

# class Person:
#   def __init__(self, name):
#      self.name = name
#      self.age = None

#   def say_hello(self):
#     print(f"Hello, my name is {self.name} and my age is {self.age}. Nice to meet you.")

#   def set_age(self, age):
#     self.age = age

#   def get_age(self):
#     return self.age



# person_one = Person("Tobiloba")    
# person_two = Person("Francesco")


# person_one.set_age(29)
# print(person_one.get_age())
# person_one.say_hello()


# person_two.set_age(34)
# print(person_two.get_age())
# person_two.say_hello()





# Setter methods:

# class Person:
#   def __init__(self, name):
#      self.name = name
#      self.age = None

#   def say_hello(self):
#      print(f"Hello, my name is {self.name} and my age is {self.age}")

#   def set_age(self, age):
#     self.age = age


# person = Person("Tobiloba")    
# person.set_age(29)
# person.say_hello()
    


  

# Creating Methods:

# class Person:
#   def __init__(self, name):
#     self.name = name

#   def say_hello(self):
#     print(f"Hello, my name is {self.name}")


# person = Person("Tobiloba")
# person.say_hello()
