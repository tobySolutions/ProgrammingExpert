"""
Notes:

- The map() and filter() functions are used to map elements in an "iterable object" to a specific value and filter an existing "iterable object" for a specific value respectively.

- An "iterable object" is anything you can loop through (collections).

- They both return new values

- The map() function returns to you; a "map object" (iterable object). You can then convert it to whatever you want.

- filter() gives you values that satisfy a specific constraint. It returns a "filter object". You can then convert it to whatever you want.

- It is very much easier to work with these functions using "lambda functions".
"""


# Map and Filter together:

# my_list = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 4]]

# new_list = filter(lambda y: y % 2 == 0, map(lambda x: sum(x), my_list))

# print(list(new_list))  # [6, 6]




# Filter function:


# my_list = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 4]]

# new_list = list(filter(lambda x: len(x) > 2, my_list))

# print(new_list)  # [[1, 2, 3], [4, 5, 6], [1, 2, 3]]



# my_list = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 4]]

# new_list = list(filter(lambda x: False, my_list))

# print(new_list)  # []



# my_list = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 4]]

# new_list = list(filter(lambda x: sum(x) > 6, my_list))

# print(new_list)  # [[4, 5, 6], [3, 4]]





# Map function:

# my_list = [[1, 2], [3, 4, 5], [6, 3, 4], [7, 5, 6]]

# new_list = list(map(lambda x: sum(x), my_list))
# print(new_list)  # [3, 12, 13, 18]




# import math

# my_list = [1, 2, 3, 4, 5, 6, 3, 4, 7, 5, 6]

# new_list = list(map(lambda x: math.sqrt(x), my_list))

# print(new_list)  # [1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 1.7320508075688772, 2.0, 2.6457513110645907, 2.23606797749979, 2.449489742783178]




# my_list = [1, 2, 3, 4, 5, 6, 7]

# new_list = list(map(lambda x: x**2, my_list))

# print(new_list)  # [1, 4, 9, 16, 25, 36, 49]