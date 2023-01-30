"""
Notes:

- Comprehensions: A way of initializing a datatype / data structure on one line.

- Multiple assignment, for example:
   - x = y = 1
   - x, y = (1, 2)

- Unpacking: 
   x, y = (1, 2)

- Docstring:
   This is like a comment for a function or a class. The point of the Docstring is to document a function, class, object.

- help(): This is a function that returns a documentation on a class, function and object.

- Comprehensions on Tuples always returns a generator object.

"""

# Docstrings and help() function:

# help(set)
# help(tuple)
# help(1)
# help(int)


# def print_foo():
#   """
#    This function simply prints foo
#   """
#   print("foo")  


# help(print_foo)


# Unpacking:

# x, y, z = 10, 10, 10

# print(x, y, z)  # 10 10 10



# Multiple assignment:

# --1
# x, y, z = 10, 10, 10

# print(x, y, z)  # 10 10 10


# --2 
# x = y = z = 10

# print(x, y, z)  # 10 10 10



# Comprehensions:

# --1
# my_tuple = (i for i in range(1, 11) for j in range(1, 5))

# print(my_tuple) <generator object <genexpr> at 0x7f5c61496510>


# --2
# my_dictionary = {i : j for i in range(1, 11) for j in range(1, 5)}

# print(my_dictionary)


# --3
# my_list = [i / 2 for i in range(1, 11) if i % 2 == 0]

# print(my_list)