"""
Notes:

- In Python, an "immutable" object is one that cannot be modified once created. Examples of these are:
  - int
  - float
  - str
  - bool
  - tuple
  - None

- In Python, a "mutable" object is one that can be modified once created. Examples are:
  - list
  - set
  - dict

- All data types are also objects in Python

- We can use the "is" keyword to see if an object is the same as another object

- "id" is the memory address location of our object in RAM. You can use the id() function to get the id.

- "Shallow Copy" just copies the external object, but, doesn't copy the objects within the object; it only references the original contents. 

- "Deep Copy" copies the object plus everything it contains.

- Most of the copying in the simple programs is "shallow copying".
"""

# Shallow vs Deep copies:

# Shallow copy (one-level in)
# a = [[1, 2, 3]]
# b = a[:]


# a.append(1)  # [[1, 2, 3, 4], 1]

# c = a[0]
# c.append(10)

# print(a is b)  # False
# print(a, b)  # [[1, 2, 3, 10]] [[1, 2, 3, 10]]




# Creating Copies of mutable objects:

# dictionary_one = {"x" : "10"}
# dictionary_two = dictionary_one.copy()

# dictionary_one["y"] = "16"

# print(dictionary_one)  # {"x": "10", "y": "16"}
# print(dictionary_two)  # {"x": "10"}
# print(dictionary_one is dictionary_two)  # False


# set_one = set()
# set_two = set_one.copy()

# set_one.add(49)
# set_two.add(50)

# print(set_one)  # {49}
# print(set_two)  # {50}
# print(set_one is set_two)  # False


# def append_to_list(any_list, value):
#   new_list = any_list[:]
#   new_list.append(value)
#   print(new_list)


# my_list = []
# append_to_list(my_list, 40)  # [40]
# append_to_list(my_list, 78)  # [78]

# print(my_list)  # []



# x = [1, 2, 3]
# y = x[:]

# print(x is y)  # False


# x = [1, 2, 3]
# y = x[:]

# x.append(4)

# print(x)  # [1, 2, 3, 4]
# print(y)  # [1, 2, 3]




# Mutable sets and dictionaries:

# def add_value_set(any_set, value):
#   any_set.add(value)
#   print(any_set)


# my_set = set()
# add_value_set(my_set, 50)  # {50}


# set_one = set()
# set_two = set_one

# set_one.add(10)
# set_two.add(30)

# print(set_one)  # {10, 30}
# print(set_two)  # {10, 30}
# print(set_one is set_two)  # True


# my_dict = {}

# my_dict["x"] = "boy"

# new_dict = my_dict

# new_dict["y"] = "girl"

# print(my_dict)
# print(new_dict)
# print(my_dict is new_dict)  # True


# Mutability with functions:

# def append_to_list(any_list, value):
#   any_list.append(value)
#   print(any_list)


# my_list = []

# append_to_list(my_list, 30)  # [30]
# append_to_list(my_list, 40)  # [30, 40]
# append_to_list(my_list, 45)  # [30, 40, 45]

# print(my_list)  # [30, 40, 45]



# id() function:


# x = 1
# y = 1

# print(id(x), id(y)) # interpreter is optimizing for memory


# x = 1
# y = x

# print(id(x), id(y))





# "is" keyword:

# x = 1
# y = x

# print(x is y)  # True

# x += 1

# print(x is y)  # False



# first_list = []
# second_list = first_list

# print(first_list is second_list)  # True


# first_list = []
# second_list = []

# print(first_list is second_list)  # False



# Mutable data types:

# x = []
# y = x

# x.append(10)  # mutable

# print(x, y)  # [10] [10]




# Immutable data types:

# x = 1
# y = x

# x += 1  # creates a new object

# print(x, y)  # 2 1