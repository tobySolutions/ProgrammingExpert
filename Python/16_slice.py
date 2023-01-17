"""

Notes:

- A slice is an operator that we can use on a "collection datatype" (lists, tuples, strings, and so on)

- It returns a new object

- It works similarly to the range function

- Syntax: 
    [start:stop:step]
    [::-1] reverses the collection
    [::2] adds a default start and stop from the 
       original collection
    [:stop]
"""


# Slicing Tuples
# my_tuple = 1, 2, 3, 4, 2, 3
# new_tuple = my_tuple[1:6:2]  # (2, 4, 3)
# new_tuple = my_tuple[::-1]  # (3, 2, 4, 3, 2, 1)


# print(new_tuple)



# Slicing strings:

# my_string = "tobiloba"
# new_string = my_string[::-1]  # abolibot
# new_string = my_string[::2]  # tblb
# new_string = my_string[1:3]  # ob


# print(new_string)


# Reversing with slice:

# my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]

# new_list = my_list[::-1]  # [22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]



# print(new_list)


# Copying with slice:

# my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
# new_list = my_list[:]  # copies list

# new_list = my_list[:-1]  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# new_list = my_list[::2]  # [2, 6, 10, 14, 18, 22]


# print(new_list)



# Negative index slicing:

# my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]

# new_list = my_list[8:0:-1]  # [18, 16, 14, 12, 10, 8, 6, 4]

# new_list = my_list[-4::-1]  # [16, 14, 12, 10, 8, 6, 4, 2]


# print(new_list)



# What are slices:

# my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
# new_list = my_list[0:2]  # [2, 4]
# new_list = my_list[:2]  # [2, 4]
# new_list = my_list[:4]  # [2, 4, 6, 8]
# new_list = my_list[1:6:2]  # [4, 8, 12]
# new_list = my_list[:8:3]  # [2, 8, 14]


# print(new_list)