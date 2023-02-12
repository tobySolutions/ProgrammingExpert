"""
Notes:

- Properties are special attributes that we can have on our instances and classes that make it so that we can enforce specific behaviors when we are accessing or trying to modify an attribute

- Private attributes have the syntax "_{attribute_name}", they are supposed to be only accessible from within a class (technically). You can still access them from outside a class though in Python.

- Properties only work with private attributes it throws an error with public attributes.

- Know how to properly name your classes such that you use Plural or Singular names at the appropriate times (Class naming rules)

- There are two ways to set up properties:
   - Legacy properties: The legacy way using the "property()" function.
   
   - New properties: Using the decorators "@property" and 
    "@{property_name}.setter" above the getter and setter methods 
     respectively.
     

- Using the legacy method for properties:

  class Person:
    def __init__(self, name):
      self.name = name
      self._salary = 0

    def set_salary(self, salary):
      if salary < 0:
        raise ValueError("Invalid!")
      self._salary = salary

    def get_salary(self):
      return round(self._salary)

    salary = property(get_salary, set_salary)


- Using the decorators:
    class Person:
      def __init__(self, name):
        self.name = name
        self._salary = 0

      @property
      def salary(self):
        return round(self._salary)

      @salary.setter
      def salary(self, salary):
        if salary < 0:
          raise ValueError("Invalid!")
        self._salary = salary 

- When using properties, you still get to run all the checks you've added to your getters and setters.
"""

# Property examples:

# Set a Time class that is instantiated with a number; When you try to change the number, it should throw an error if the number is below 0 or above 60

# ----Using Legacy Properties-----

# class Time:
#   def __init__(self, second):
#     self._second = second

#   def set_second(self, second):
#     if second < 0 or second > 60:
#       raise ValueError("Invalid!")
#     self._second = second

#   def get_second(self):
#     return self._second

#   second = property(get_second, set_second)  
  

# my_time = Time(34)
# my_time.second = 60
# print(my_time.second)  # 60
    
# my_time = Time(35)
# my_time.second = -34
# print(my_time.second)  # ValueError: Invalid!

# my_time = Time(-29)    
# print(my_time.second)  # -29
  


# ----Using New Properties-----

# class Time:
#   def __init__(self, second):
#     self._second = second

#   @property
#   def second(self):
#     return self._second
    
#   @second.setter
#   def second(self, second):
#     if second < 0 or second > 60:
#       raise ValueError("Invalid!")
#     self._second = second  



# my_time = Time(34)
# my_time.second = 60
# print(my_time.second)  # 60
    
# my_time = Time(35)
# my_time.second = -34
# print(my_time.second)  # ValueError: Invalid!

# my_time = Time(-29)    
# print(my_time.second)  # -29





  
# New properties:

# class Person:
#   def __init__(self, name):
#     self.name = name
#     self._salary = 0

#   @property
#   def salary(self):
#     return round(self._salary)

#   @salary.setter
#   def salary(self, salary):
#     if salary < 0:
#       raise ValueError("Invalid!")
#     self._salary = salary 


# person_one = Person("Tobiloba")  
# person_one.salary = 1000
# person_one.salary = -5000  # ValueError: Invalid!
# person_one.salary = 5000
# person_one.salary = 101.50122
# print(person_one.name, person_one.salary)      




# Legacy properties (old way of making properties):

# class Person:
#   def __init__(self, name):
#     self.name = name
#     self._salary = 0

#   def set_salary(self, salary):
#     if salary < 0:
#       raise ValueError("Invalid!")
#     self._salary = salary

#   def get_salary(self):
#     return round(self._salary)

#   salary = property(get_salary, set_salary)


# person_one = Person("Tobiloba")  
# person_one.salary = 1000
# person_one.salary = -5000  # ValueError: Invalid!
# person_one.salary = 5000
# person_one.salary = 101.50122
# print(person_one.salary)  # 102





# Getters and setters:

# class Person:
#   def __init__(self, name):
#     self.name = name
#     self._salary = 0

#   def set_salary(self, salary):
#     if salary < 0:
#       raise ValueError("Invalid!")
#     self._salary = salary

#   def get_salary(self):
#     return round(self._salary)


# person = Person("Tobiloba")
# person.set_salary(-100)  # ValueError: Invalid!
# print(person.get_salary())



