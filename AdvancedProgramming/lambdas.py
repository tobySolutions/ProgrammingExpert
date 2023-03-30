"""

Notes:

- A "Lambda" is an anonymous function that can be defined in-
line without the use of the "def" keyword.

- It comes in handy a lot especially when defining a custom ordering for a collection.
"""


# Lambdas returning lambdas:

# multiply = lambda x: lambda y: x * y

# result = multiply(2)(4)  # 8
# result =  multiply(2)
# print(result(4))




# Lambdas as arguments:

# list = [(1, -2), (2, -6), (0, 4)]

# list.sort(key=lambda x: x[1])

# print(list)



# Calling lambdas:

# sum_three_values = lambda x, y, z: x + y + z

# print(sum_three_values(1, 2, 3))  # 6



# Creating Lambdas:

# sum_three_values = lambda x, y, z: x + y + z