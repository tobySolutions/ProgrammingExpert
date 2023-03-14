"""
Notes:

- The "main" module is the one that is invoked or run directly.

- Python will automatically set the "__name__" variable of that module to the string '__main__' when it is run directly.

- In modules, it is best practice to run some parts of the code conditionally based on that "__name__" variable

- A Python "module" is simply a Python a file and a Python "Package" is simply a directory that contains Python "modules".

- It is always important to pay attention to name-confliction when it comes to imports

- "Circular imports" occur when a module is importing another module and the module that is importing is also being imported by the other module.

- In Python, when a module is imported; the code inside of the imported module is run automatically.

- To avoid "Circular imports" it is best to have one "main module" that imports all the modules. The "main module" is then run / executed.
"""

