"""
Notes:

- In short, class methods and attributes only work on the class itself.

- The attributes inside the constructor function (the ones that use "self") are "instance attributes" not "class attributes"; instance attributes bind to an object

- Any value that when changed somewhere you want to be changed everywhere (including in instances) can be declared as a class attribute.

- Class attributes work for a specific class and all of its instances (objects of the class)

- If there exists an instance attribute that is the same as a class attribute, to an object (instance), the instance attribute takes priority.

- Class attributes are typically declared at the top of the class in the body of the class.

- Class methods are methods that have the "@classmethod" decorator above them in code and they have a mandatory "cls" parameter; the "cls" parameter references the class itself when used.
"""

# Class method and attributes example:

# class Circle:
#   pi = 3.14

#   @classmethod
#   def get_area(cls, radius):
#     return cls.pi * (radius ** 2)

#   @classmethod
#   def get_perimeter(cls, radius):
#     return 2 * cls.pi * (radius ** 2)

#   @classmethod
#   def add_area_to_perimeter(cls, radius):
#     return cls.get_area(radius) + cls.get_perimeter(radius)


# area = Circle.get_area(3)    
# perimeter = Circle.get_perimeter(3)
# sum_of_area_and_perimeter = Circle.add_area_to_perimeter(3)

# print(area, perimeter)  # 28.26 56.52
# print(sum_of_area_and_perimeter)  # 84.78



# Class Method:

# class Car:
#   number_of_cars = 0
#   wheels = 4

#   def __init__(self, make, model):
#     self.make = make
#     self.model = model

#   @classmethod
#   def update_number_of_cars(cls, cars):
#     cls.number_of_cars = cars


# Car.update_number_of_cars(10)

# car_one = Car("Honda", "Civic")
# car_two = Car("Madza", "Direct")

# print(car_one.number_of_cars)  # 10
# print(car_two.number_of_cars)  # 10
# print(Car.number_of_cars)  # 10


  
# Class attributes:

# class Car:
#   number_of_cars = 0
  
#   def __init__(self, make, model):
#     self.make = make
#     self.model = model
#     Car.number_of_cars += 1



# car_one = Car("Honda", "Civic")    
# car_two = Car("Toyota", "Muscle")

# print(car_one.number_of_cars)  # 2
# print(car_two.number_of_cars)  # 2
# print(Car.number_of_cars)  # 2
    


# class Car: 

#   number_of_cars = 0

#   def __init__(self, make, model):
#     self.make = make
#     self.model = model
#     self.number_of_cars = 0



# Car.number_of_cars += 5

# car_one = Car("Honda", "Civic")
# car_two = Car("Dodge", "Dare")


# print(car_one.number_of_cars)  # 0
# print(car_two.number_of_cars)  # 0
# print(Car.number_of_cars)  # 5



# class Car:
#   number_of_cars = 0

#   def __init__(self, make, model):
#     self.make = make
#     self.model = model



# Car.number_of_cars += 3

# car_one = Car("Honda", "Civic")

# print(Car.number_of_cars)  # 3
# print(car_one.number_of_cars) # 3



# Instance attributes:

# class Car:
#   def __init__(self, make, model):
#     self.make = make
#     self.model = model



