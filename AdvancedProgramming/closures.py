"""
Notes:

- Closures have to do with nested functions

-   Enclosing Functions -----> def outer(x):
     Nested Functions   ----->   def inner(y):
                                     print(x + y)
                                  return inner

- Nested functions when called always have different return values based on how many different times they're called. Each call is separated from every other one basically, for example:
    
          def outer(x):
            def inner(y):
              print(x + y)
            return inner
          
          
          execute_inner = outer(10)
          execute_inner(5)  # 15
          execute_inner(10) # 20
          execute_inner(20) # 30
          


- Functions are objects in Python

- A "free variable" is a variable that is not local to the scope of a function.


- The "nonlocal" keyword is added to the front of a variable to ensure that it should be declared in the scope directly above the current one.
"""



# Advanced Closure Example:

# =======================

# def outer():
#   def inner():
#     def innermost():
#       nonlocal x
#       x = 4
#       print('Innermost:', x)  # 'Innermost:', 4

#     nonlocal x
#     x = 10
#     innermost()
#     print('Inner:', x) # 'Inner:', 4

#   x = 50
#   inner()
#   print('Outer:', x)  # 'Outer:', 4


# outer()

# =======================

# def counter(start):
#   count = start


#   def increment(value):
#     nonlocal count
#     count += value
#     return count

#   return increment


# count = counter(4)
# print(count(10)) # 14
# print(count(10)) # 24
  
# ============================




# Closures:

# def collection():

#   my_list = []


#   def inner(value):
#     my_list.append(value)
#     return my_list

#   return inner



# add_to_collection = collection()

# print(add_to_collection(1))
# print(add_to_collection(10))
# print(add_to_collection(30))
# print(add_to_collection(50))
# print(add_to_collection(100))






# Nested Functions:

# ======================

# def outer(x):
#   def inner(y):
#     def innermost(z):
#       sum = x + y + z
#       print(x + y + z)
#       return sum
#     return innermost
#   return inner


# result = outer(5)(10)(5)
# print(result) # 20


# =======================

# def outer(x):
#   def inner(y):
#     print(x + y)

#   inner(5)


# outer(10) # 15


# =======================
# def outer(x):
#   def inner(y):
#     print(x + y)
#   return inner


# execute_inner = outer(10)
# execute_inner(5)  # 15
# execute_inner(10) # 20
# execute_inner(20) # 30




# Functions as Objects:

# def foo(x):
#   print(x)


# def call_func(func, x):
#   func(x)


# call_func(foo, 19)  # 19