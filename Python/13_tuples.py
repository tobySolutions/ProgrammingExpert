"""
Notes:

- A Tuple is basically a List that can't be modified (It is immutable)

- Tuple elements are accessed by their indices like Lists and they share same methods as Lists

- "tuple()" is the tuple constructor

- .count() method - Returns the frequency of a certain element if it exists in the tuple

- len() function - Returns number of elements in the tuple

-.index() method - Returns the index of the first occurrence of a certain element if it exists
"""

# Modifying Tuples:
# my_tuple = (1, 4, 4, 5, 8)
# modified_tuple = (my_tuple[0], my_tuple[1], 6, 9, my_tuple[4])

# print(modified_tuple)  # (1, 4, 6, 9, 8)



# Creating tuples:

# my_tuple = 1, 4, 4, 5, 8  # Is actually a Tuple

# my_tuple = (1)  # Not a tuple

# my_tuple = (1, )   # Is a Tuple, my_tuple[1] is "out of range"


# print(my_tuple[0])
# print(my_tuple)




# Multiplying Lists:
# my_tuple = (1, 2)

# increased_list = my_tuple * 4
# print(increased_list)  # (1, 2, 1, 2, 1, 2, 1, 2)





# Adding Lists:
# first_tuple = (7, 8)
# second_tuple = (9, 10)

# combined = first_list * second_list
# print(combined)  # (7, 8, 9, 10)


# Nested Tuples:
# my_tuple = (1, 2, 4, (4, 5, 1), 9, (10, 11, 9.5))

# print(my_tuple[-1][-1])  # 9.5


# "in" operator:
# my_tuple = (1, 2, 1, 6, 8, 1)
# contains_element = 6 in my_tuple
# print(contains_element)  # True


# .index():
# my_tuple = (1, 2, 1, 6, 8, 1)

# number_first_index = my_tuple.index(1)
# print(number_first_index)  # 0


# .count():
# my_tuple = (1, 2, 1, 6, 8, 1)

# number_count = my_tuple.count(1)
# print(number_count)  # 3


# len() function:

# my_tuple = (1, 2, 4, 6, 8)

# print(len(my_tuple))  # 5


# Tuple Indexing:

# my_tuple = (1, 2, 3)

# my_tuple[1] = 4  # Error! Tuples are immutable remember?
# print(my_tuple[2], my_tuple[-2])  # 3 2
