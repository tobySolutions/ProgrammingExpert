"""
Notes:

- A "static method" is defined inside of a class, but, should not reference anything relevant to that class except for other static methods.

- Static methods should be "Pure functions". Pure functions do not use temporary variables outside of their own scope and they exclusively transform a set of inputs into some outputs.

- Static methods use the "@staticmethod" decorator above them inside a class.

- A static method is a method that sits inside of a class, but, does not have accesss to the "cls" keyword or to the "self" keyword.

- Static methods help better organize your code.

- We call "static methods" the exact same way we call "class methods"; either on the Class itself or on any instance of the class.

- "static attributes" in Python are the same as "class attributes".

- A "static method" shouldn't rely on any values or variables outside of it.
"""


# Instance vs static vs class methods:

# class Student:
#   grade_bump = 2.0
  
#   def __init__(self, name, grades=[]):
#     self.name = name
#     self.grades = grades

#   # Instance method
#   def average(self):
#     return sum(self.grades) / len(self.grades)
  
#   @classmethod
#   def average_from_grades_plus_bump(cls, grades):
#     average = cls.average_from_grades(grades)  
#     return min(average + cls.grade_bump, 100)

  
#   @staticmethod
#   def average_from_grades(grades):
#     return sum(grades) / len(grades)



# student_one = Student("Tobiloba", [65, 90, 100, 80]) 
# student_two = Student("Solutions", [100, 100, 100, 100])


# print(Student.average_from_grades_plus_bump(student_one.grades))







    
# Static vs Class Attributes:

# class Student:
  
#   gravity = 9.8
#   number_of_students = 200
  
#   def __init__(self, name, grades=[]):
#     self.name = name
#     self.grades = grades


#   @staticmethod
#   def average_from_grades(grades):
#     return sum(grades) / len(grades)



    
    
# Creating static methods:

# class Student:
    
#   def __init__(self, name, grades=[]):
#     self.name = name
#     self.grades = grades


#   @staticmethod
#   def average_from_grades(grades):
#     return sum(grades) / len(grades)


# student_one = Student("Tobiloba", [65, 90, 100, 80]) 
# student_two = Student("Solutions", [100, 100, 100, 100])

# student_one_average = student_one.average_from_grades(student_one.grades)
# student_one_average = Student.average_from_grades(student_one.grades)

# student_two_average = student_one.average_from_grades(student_two.grades)

# print(student_one_average)  # 83.75
# print(student_two_average)  # 100.0

