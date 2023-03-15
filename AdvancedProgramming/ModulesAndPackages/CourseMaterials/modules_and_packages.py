"""
Notes:

- The "main" module is the one that is invoked or run directly.

- Python will automatically set the "__name__" variable of that module to the string '__main__' when it is run directly.

- In modules, it is best practice to run some parts of the code conditionally based on that "__name__" variable

- A Python "module" is simply any Python file (ending in .py) and a Python "Package" is simply a directory that contains Python "modules".

- When importing a Python "Package" the code inside of the "__init__.py" file will run once.

- It is always important to pay attention to name-confliction when it comes to imports

- When using "import *" to make an import of everything in a a module, it is best to be wary of name conflicts that may arise.

- "Circular imports" occur when a module is importing another module and the module that is importing is also being imported by the other module (modules importing each other basically)

- In Python, when a module is imported; the code inside of the imported module is run automatically.

- To avoid "Circular imports" it is best to have one "main module" that imports all the modules. The "main module" is then run / executed.

- Doing relative imports in packages, the imports don't really run in the files making the imports, but in the module importing the package itself.

- It is against best practices to use relative imports
"""



# Creating packages:

# import code.a 


# from code import A, B

# A()  # a b A
# B()  # a b B


# import code

# code.A()  # a b A
# code.B()  # a b B


# from code.a import A  # __init__.py file gets called once
# from code.b import B  # __init.py file gets calles once

# A()  # a b A
# B()  # a b B


# import code.a  # "a" is printed to the console. Code in the "__init__.py" file gets run too.

# import code.b  # b


# import code  # Code in the "__init__.py" file gets run.


# import code  # init









# if __name__ == "__main__":

# -----------------------

# from functions import * 

# foo()  # foo
# bar()  # bar


# def func():
#   print("Func")

# print(__name__)  # __main__

# if __name__ == "__main__":
#   print("modules and packages")

# -----------------------


# from functions import *  # returns "functions"

# foo()  # foo
# bar()  # bar


# def func():
#   print("Func")

# -----------------------




  
# Circular imports:

# from functions import *

# foo()
# bar()

# def func():
#   print("Func")



  

# import *:

# from functions import *

# foo()  # foo
# bar()  # bar

# my_test = Test()

# print("run")  # run
# print(my_test)  # <functions.Test object at 0x7f7d3c477d60> 





# Special imports:

# ---------------------------

# from functions import foo, bar, Test

# foo()  # foo
# bar()  # bar

# my_test = Test()

# print("run")  # run
# print(my_test)  # <functions.Test object at 0x7f7d3c477d60> 


# ---------------------------
# import functions as f

# f.bar() # bar
# f.foo()  # foo

# my_test = f.Test()

# print("run")  # run
# print(my_test)  # <functions.Test object at 0x7f7d3c477d60>

# ------------------------------






# Creating and Importing Modules:

# import functions

# functions.bar() # bar
# functions.foo()  # foo

# my_test = functions.Test()

# print("run")  # run
# print(my_test)  # <functions.Test object at 0x7f7d3c477d60>
