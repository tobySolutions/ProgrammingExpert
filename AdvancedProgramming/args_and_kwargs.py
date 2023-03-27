"""
Notes:

- args = arguments; kwargs = keyword_arguments

- By passing "*args" and "**kwargs" as arguments to your function, you can ensure that the variable "args" and "kwargs" will contain all the previously unused arguments that were passed into your function.

- You must remember that "args" will be a "tuple" containing all "positional arguments" that were passed, and "kwargs" will be a "dictionary" containing all of the "keyword arguments"

- The "*" before the "args" in "*args" makes the "args" to be able to store every single "Positional argument" passed into the function as a tuple in the variable "args".

- The "Splat operator" (*) splats an iterable object like a list into individual elements and passes these as arguments to a function.

- "Splat" a.k.a "Unpack"

- Two asterisks (**) "unpacks" a dictionary where as one asterisk (*) unpacks / splats any iterable collection / data structure like a list, tuple; strings too.

- The print() function internally has a "*args" parameter that helps it to print out any number of arguments passed in.

- The "*args" and "**kwargs" can work as "parameters" and "arguments" with functions in Python.
"""


# *args and **kwargs with Mandatory parameters:

# def test(a, *args, **kwargs):
#   print(a, args, kwargs)




# arguments = [1, 2, 5]
# keyword_arguments = {'b': 2, 'c': 4}
# test(1, *arguments, **keyword_arguments)





# Splat / Unpack operator:

# values = [1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 16, 18]
# print(*values) # 1 3 4 5 6 7 8 10 11 12 14 16 18



# def sum_items(position_one, position_two, a=None, b=None, c=None):
#   print(position_one, position_two, a, b, c)
#   return position_one + position_two + a + b + c



# arguments = [1, 2]
# keyword_arguments = {'a': 2, 'b': 4, 'c': 6}
# print(sum_items(*arguments, **keyword_arguments))  # 1 2 2 4 6 /n 15




# def sum_items(a, b, c):
#   print(a, b, c)
#   return a + b + c


# keyword_arguments = {'a': 2, 'b': 4, 'c': 6}
# print(sum_items(**keyword_arguments))  # 2 4 6 /n 12




# def sum_items(a, b, c):
#   print(a, b, c)
#   return a + b + c


# arguments = "457"
# print(sum_items(*arguments))  # 4 5 7 /n 457




# def sum_items(a, b, c):
#   print(a, b, c)
#   return a + b + c


# arguments = (4, 5, 7)
# print(sum_items(*arguments))  # 4 5 7 /n 16




# def sum_items(a, b, c):
#   print(a, b, c)
#   return a + b + c


# arguments = [4, 5, 7]
# print(sum_items(*arguments))  # 4 5 7 /n 16





# **kwargs:

# def sum_items(*args, **kwargs):
#   print(args)
#   print(kwargs['k'])


# sum_items(1, 2, 3, 4, 5, k=2, w=8)  # (1, 2, 3, 4, 5)/n 2



# def sum_items(*args, **kwargs):
#   print(args)
#   print(kwargs)



# sum_items(1, 2, 3, 4, 5, k=2, w=8)  # (1, 2, 3, 4, 5)/n  {'k': 2, 'w': 8}
# sum_items(1, 2, 3, a=4, b=10)  # (1, 2, 3)/n {'a': 4, 'b': 10}
# sum_items(1)  # (1,)/n {}






# *args:

# def sum_items(*args):
#   print(sum(args))


# sum_items(1, 2, 3, 4, 5)  # 15
# sum_items(1, 2, 3)  # 6
# sum_items(1)  # 1




# def sum_items(*args):
#   print(args)



# sum_items(1, 2, 3, 4, 5)  # (1, 2, 3, 4, 5)
# sum_items(1, 2, 3)  # (1, 2, 3)
# sum_items(1)  # (1,)