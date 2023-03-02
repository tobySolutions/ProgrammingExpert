"""
Notes:

- Interfaces are designed to be used as abstract datatypes that enforce that classes that implement them define specific methods and behaviors.

- Interfaces don't technically exist in Python just like abstract classes.

- Interfaces in Python are "abstract classes" that only have "abstract methods" (remember abstract methods have no implementation).

- It is mandatory that classes redefine all the methods defined in an interface that they implement.

- Interfaces can be used as a datatype in programming.

- We don't have a technical way to use or enforce interfaces in Python, but, you can follow the naming convention of using the suffix "Interface" to identify them:
    class GameInterface:
      pass

- When you're inheriting from a proper class and an interface, the proper class should come first, then the interface:
    class Sudoku(Game, GameInterface):
      pass
"""


# Using an Interface as a type:

# class RunCodeInterface:
#   def compile_code(self):
#     raise NotImplementedError("You must implement compile_code().")

#   def execute_code(self):
#     raise NotImplementedError("You must implement execute_code().")


# class GoCode(RunCodeInterface):
#   def compile_code(self):
#     print("Compile Go code")

#   def execute_code(self):
#     print("Execute Go code")


# class JavaCode(RunCodeInterface):
#   def compile_code(self):
#     print("Compile Java code")

#   def execute_code(self):
#     print("Execute Java code")



# def run_code(code : RunCodeInterface):
#   code.compile_code()
#   code.execute_code()

# go = GoCode()
# java = JavaCode()

# # Taking Ducktyping into account:
# run_code(java)  # Compile Java Code
#                 # Execute Java code


# Implementing an interface:

# class RunCodeInterface:
#   def compile_code(self):
#     raise NotImplementedError("You must implement compile_code().")

#   def execute_code(self):
#     raise NotImplementedError("You must implement execute_code().")


# class GoCode(RunCodeInterface):
#   def compile_code(self):
#     print("Compile Go code")

#   def execute_code(self):
#     print("Execute Go code")


# class JavaCode(RunCodeInterface):
#   def compile_code(self):
#     print("Compile Java code")

#   def execute_code(self):
#     print("Execute Java code")




# Creating interfaces:

# class RunCodeInterface:
#   def compile_code(self):
#     raise NotImplementedError("You must implement compile_code().")

#   def execute_code(self):
#     raise NotImplementedError("You must implement execute_code().")




