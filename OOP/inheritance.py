"""
Notes: 

- In inheritance, we have:
   - Parent class / Super class / Base class : The class that is inherited from.
   
   - Child class / Sub class / Derived class : The class that inherits from another.

   
-  "Polymorphism" is the ability of an object to behave in different ways and show different behaviors based on the context it is used in.

- "Method overriding" is when a programmer re-defines a method on a child class that has already been declared on its parent.

- Python works with inheritance a little bit different than other Programming Languages.

- Inheritance allows you to not duplicate code around your program.

- When we use "super()", we implicitly pass the "self" argument into the operation being performed.

- isinstance(object, class) function returns a boolean (True or False) which tells us whether or not an object is a descendant of any class.

- Python can do "Multiple inheritance". 

- If the class that inherits has no methods inside of it (including constructor function), we use the MRO (Method Resolution Order) to decide what class whatever methods we're calling is coming from (including the constructor function); it's always in order from the first class in the parantheses. For example:

class Person: 
  def __init__(self, first_name):
    self.first_name = first_name
    print("Person!!")

class Human:
  def __init__(self, first_name):
    self.first_name = first_name
    print("Human!!")

class Tobiloba(Human, Person):
  pass


my_tobiloba = Tobiloba("Solutions")  # Human!!



- Duck Typing is sort of like a Python thing: "If it acts like a Duck, then it's probably a Duck, it isn't a Duck whenever it stops acting like a Duck"

- Inheritance in Python is not Prototypal as in Javascript.

- "is-a" rule: If a class inherits from another class, then the class inheriting is of the type of its parent.

"""


# Duck typing:

# -- The program only breaks when stuff doesn't work out---

# class Duck:
#   def swim(self):
#     print("Swimming Duck")

#   def fly(self):
#     print("Flying Duck")


# class Whale:
#   def swim(self):
#     print("Swimming Whale")
    


# animals = [Duck(), Duck(), Whale()]

# for animal in animals:
#   animal.swim()
#   animal.fly()



# Multiple inheritance:

# "Just a demo to show multiple inheritance in Python and demonstrate Method Resolution Order (MRO)"

# ------------
# class A:
#   pass


# class B:
#   def __init__(self):
#     print("B")

# class C(A, B):
#   def __init__(self):
#     super().__init__()


# c_class = C()  # B

# -------------

# class A:
#   def __init__(self):
#     print("A")


# class B:
#   def __init__(self):
#     print("B")


# class C(A, B):
#   pass



# c_class = C()  # A

# -------------


# isinstance() function:

# "parent class"
# class Person:
#   def __init__(self, first_name, last_name):
#     self.first_name = first_name
#     self.last_name = last_name


#   def say_hello(self):
#      print(f"Hello!! I am {self.first_name} {self.last_name}")


# "child class"
# class Employee(Person):
#   def __init__(self, first_name, last_name, salary):
#     super().__init__(first_name, last_name)
#     self.salary = salary
    
#   def say_hello(self):
#     super().say_hello()
#     print(f"My salary is {self.salary}")


# "A manager can be an employee"
# class Manager(Employee):
#   def __init__(self, first_name, last_name, salary, department):
#     super().__init__(first_name, last_name, salary)
#     self.department = department


# "An owner can't be an employee; not a general occurrence"
# class Owner(Person):
#   def __init__(self, first_name, last_name, net_worth):
#     super().__init__(first_name, last_name)
#     self.net_worth = net_worth

  


# my_manager = Manager("Tobiloba", "Solutions", 50000, "Software Engineering")
# my_owner = Person("Ella", "Oge")


# print(isinstance(my_manager, Person))  # True
# print(isinstance(my_owner, Employee))  # False
# print(isinstance(my_owner, Person))  # True




# Inheritance Hierarchies:

# "parent class"
# class Person:
#   def __init__(self, first_name, last_name):
#     self.first_name = first_name
#     self.last_name = last_name


#   def say_hello(self):
#      print(f"Hello!! I am {self.first_name} {self.last_name}")


# "child class"
# class Employee(Person):
#   def __init__(self, first_name, last_name, salary):
#     super().__init__(first_name, last_name)
#     self.salary = salary
    
#   def say_hello(self):
#     super().say_hello()
#     print(f"My salary is {self.salary}")


# "A manager can be an employee"
# class Manager(Employee):
#   def __init__(self, first_name, last_name, salary, department):
#     super().__init__(first_name, last_name, salary)
#     self.department = department


# "An owner can't be an employee; not a general occurrence"
# class Owner(Person):
#   def __init__(self, first_name, last_name, net_worth):
#     super().__init__(first_name, last_name)
#     self.net_worth = net_worth

  


# my_manager = Manager("Tobiloba", "Solutions", 50000, "Software Engineering")
# my_owner = Person("Ella", "Oge")


# my_manager.say_hello()  # Hello!! I am Tobiloba Solutions My salary is 50000
# my_owner.say_hello()  # Hello!! I am Ella Oge





# Overriding the constructor:

# "parent class"
# class Person:
#   def __init__(self, first_name, last_name):
#     self.first_name = first_name
#     self.last_name = last_name


#   def say_hello(self):
#      print(f"Hello!! I am {self.first_name} {self.last_name}")


# "child class"
# class Employee(Person):
#   def __init__(self, first_name, last_name, salary):
#     super().__init__(first_name, last_name)
#     self.salary = salary
    
#   def say_hello(self):
#     super().say_hello()
#     print(f"My salary is {self.salary}")


# my_employee = Employee("Tobiloba", "Solutions", 50000)
# my_person = Person("Ella", "Oge")


# my_employee.say_hello()  # Hello!! I am Tobiloba Solutions My salary is 50000
# my_person.say_hello()  # Hello!! I am Ella Oge




# Method Overriding:

# "parent class"
# class Person:
#   def __init__(self, first_name, last_name):
#     self.first_name = first_name
#     self.last_name = last_name


#   def say_hello(self):
#      print(f"Hello!! I am {self.first_name} {self.last_name}")


# "child class"
# class Employee(Person):
#   def say_hello(self):
#     print("-----------")
#     super().say_hello()
#     print("-----------")


# my_employee = Employee("Tobiloba", "Solutions")
# my_person = Person("Ella", "Oge")


# my_employee.say_hello()  # Hello!! I am Tobiloba Solutions
# my_person.say_hello()  # Hello!! I am Ella Oge




# Super / Sub, Base / Derived, Parent / Child:

# "parent class"
# class Person:
#   def __init__(self, first_name, last_name):
#     self.first_name = first_name
#     self.last_name = last_name


#   def say_hello(self):
#      print(f"Hello!! I am {self.first_name} {self.last_name}")


# "child class"
# class Employee(Person):
#   def test(self):
#     print("test")


# my_employee = Employee("Tobiloba", "Solutions")
# my_person = Person("Ella", "Oge")

# # my_person.test()  # AttributeError
# my_employee.test()  # test
# my_employee.say_hello()  # Hello!! I am Tobiloba Solutions
# my_person.say_hello()  # Hello!! I am Ella Oge




