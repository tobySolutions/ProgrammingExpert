"""
Notes:

- The "Standard Library" of a language are the libraries that the language comes with by default. In Python, this includes modules like "math", "random"

- abs(number) function returns the absolute value of the argument.

- max(iterable or multiple integers) function returns the maximum of any amount of arguments passed into it or any iterable like a list, tuple, set, dict, string.

- min(iterable or multiple integers) function returns the minimum of any amount of arguments passed into it or any iterable like a list, tuple, set, dict, string.

- sum(iterable) function returns the sum of values of an iterable like a list, tuple, set, dict, string, but, it takes at most 2 arguments.

- round(number, ndigits) function rounds a number to a given precision in decimal digits. The return value is an integer if ndigits is omitted.

- The trigonometric functions in the "math" module work with radians not degrees.

- random.randint(start, stop) returns a random number within the range of "start" and "stop" including both "start" and "stop"

- random.randrange(start, stop, step) returns a random number within the range of "start" and "stop" excluding "stop"

- random.choice(iterable) returns a random value from the passed in iterable.
"""

# random Module:
# import random


# choices = ["hey", "hello", True, 1, "get out!", "Hola"]
# random_choice = random.choice(choices)

# print(random_choice)

# random_range = random.randrange(1, 10, 3)

# print(random_range)


# random_number = random.randint(1, 10)

# print(random_number)




# math Module:

# import math

# print(math.cos(0))
# print(math.sin(180))
# print(math.tan(30))
# print(math.pi)




# round() function:

# print(round(3.67))  # 4
# print(round(3.2))  # 3
# print(round(3.435, 1))  # 3.4
# print(round(3.435, 2))  # 3.44
# print(round(3.888888, 4))  # 3.8889



# sum() function:

# sum_of_values = sum([1, 3])  # 4
# sum_of_values = sum({1: 3, 2: 4})  # 1 + 2 = 3
# sum_of_values = sum({1, 3, 4, 5})  # 13
# sum_of_values = sum((10, 20, 30))  # 60

# print(sum_of_values)


# min() function:

# minimum_value = min(1, 3, 5, 6, 9)  # 1
# minimum_value = min("a", "b", "c", "d", "jekaplay")  # a
# minimum_value = min([1, 2, 4, 5, 8], [1, 3])  # [1, 2, 4, 5, 8]
# minimum_value = min([1, 3, 4, 5, 7, 9, 10])  # [1]



# print(minimum_value)




# max() function:

# maximum_value = max(1, 3, 5, 6, 9)  # 9
# maximum_value = max("a", "b", "c", "d", "jekaplay")  # "jekaplay"
# maximum_value = max([1, 2, 4, 5, 8], [1, 3])  # [1, 3]
# maximum_value = max([1, 3, 4, 5, 7, 9, 10])  # [10]


# print(maximum_value)


# abs() function:

# print(abs(-8))  # 8
# print(abs(-23.7))  # 23.7
# print(abs(-10))  # 10
# print(abs(0))  # 0
# print(abs(11))  # 11



