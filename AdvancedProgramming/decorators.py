"""
Notes:

- "Decorators" describe a special kind of function that is meant to "wrap" another function.

- The "wrapper" function inside the "decorator" is what we actually working with when we use a decorator on a function:

    def decorator(func):
      def wrapper(x):
        print("Wrapper function called func!")
        result = func()
        
        return result

       return wrapper



- A particular "@ notation" is used to indicate that a function should be wrapped by one or more decorators.
   @timer
   def run_simulation():

- Decorators take in a function as a parameter, perform some checks on it, force some specific behavior and then they call the function if everything is correct.

- When using multiple decorators the modifications of the second decorator (one furthest to the function) will be applied to the modifications of the first decorator (one closest to the function)

- The "Placeholder variable" in Python is "_".
"""


# Using Multiple decorators:

# import time

# def timer(func):
#   def wrapper(*args, **kwargs):
#     start_time = time.time()
#     result = func(*args, **kwargs)
#     end_time = time.time()

#     total_time = end_time - start_time
#     print(f"Time taken to execute {total_time}")
#     return result
#   return wrapper


# def pretty_printer(func):
#   def wrapper(*args, **kwargs):
#     print("start")
#     result = func(*args, **kwargs)
#     print("end")
#     return result

  
#   return wrapper


# @timer
# @pretty_printer
# def print_numbers(num):
#   for i in range(num):
#     print(i)

# The above is the same as:
# print_numbers = timer(pretty_printer(print_numbers))


# print_numbers(100)


# Decorator examples:

# =========================

# import time

# def timer(func):
#   def wrapper(*args, **kwargs):
#     start_time = time.time()
#     result = func(*args, **kwargs)
#     end_time = time.time()

#     total_time = end_time - start_time
#     print(f"Time taken to execute {total_time}")
#     return result
#   return wrapper


# @timer
# def loop():
#   for _ in range(1000000):
#     pass


# @timer
# def get_max(x, y, z):
#   loop()
#   return max(x, y, z)


# print(get_max(1, 2, 3))

  
# =========================

# import time

# def timer(func):
#   def wrapper(*args, **kwargs):
#     start_time = time.time()
#     result = func(*args, **kwargs)
#     end_time = time.time()

#     total_time = end_time - start_time
#     print(f"Time taken to execute {total_time}")
#     return result
#   return wrapper


# @timer
# def loop():
#   for _ in range(100000000):
#     pass


# loop()






# Create Dynamic Decorators:


# def decorator(func):
#   def wrapper(*args, **kwargs):
#     print("Wrapper function called func!")
#     result = func(*args, **kwargs)
    
#     return result

#   return wrapper



# @decorator
# def test_function(x, y, z=None):
#   print(x, y, z)


# test_function(10, 20, z=40)  # Wrapper function called func!
                               # 10 20 40




# Using decorators:

# ===================================

# Without decorators: 

# def decorator(func):
#   def wrapper(x):
#     print("Wrapper function called func!", x)
#     result = func()
    
#     return result

#   return wrapper




# def test_function():
#   print("tester")

# test_function = decorator(test_function)

# test_function(1) 

# ===================================

# def decorator(func):
#   def wrapper(x):
#     print("Wrapper function called func!", x)
#     result = func()
    
#     return result

#   return wrapper



# @decorator
# def test_function():
#   print("tester")


# test_function(1)  # Wrapper function called func! 1
                  # tester


# ======================================

    


# Create a basic decorator:

# def decorator(func):
#   def wrapper(x):
#     print("Wrapper function called func!")
#     result = func()
#     return result
    
#   return wrapper