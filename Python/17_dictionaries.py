"""
Notes:

- In Python, a "dictionary (or dict)" is a collection that associates immutable keys with values of any type.

- A dictionary is an unordered collection of items.

- .values() method: returns a dict_values object that contains all the values in the dictionary. The values in that object can't be accessed directly unless it is converted to a list with "list()".

- .keys() method: returns a dict_keys object that contains all the keys in the dictionary. The values in that object can't be accessed directly unless it is converted to a list with "list()".

- .items() method: returns a dict_items object that contains all the items in the dictionary. The values in that object can't be accessed directly unless it is converted to a list with "list()".

- .get(key, value_to_assign) method: This method checks whether the passed in "key" has a value in the dictionary;if it does, it returns it, else it assigns "value to assign" to it in the dictionary.
"""

# dictionary examples:

# Program to count the number of entries from a user if "q" is not input by the user.

# counts = {}  

# while True:
#   num = input("Enter a number (press 'q' to quit): ")

#   if num == "q":
#     break

#   num = int(num)

#   counts[num] = counts.get(num, 0) + 1

  
# print(counts)







# characters = {}

# my_string = "hello world!!!"

# for char in my_string:
#   characters[char] = characters.get(char, 0) + 1
  
# print(characters)


# .get() method: 

# dictionary = {
#    "name": "Tobiloba",
#    "role": "Frontend Engineer",
#     "job": "pending"
# }


# dictionary["babe"] = dictionary.get("babe", False) + True

# print(dictionary)

# dictionary = {
#   1: 1,
#   2: 2,
#   3: 3
# }

# dictionary[4] = dictionary.get(4, 0) + 4

# print(dictionary)




# Looping through dictionaries:

# dictionary = {
#    "name": "Tobiloba",
#    "role": "Frontend Engineer",
#     "job": "pending"
# }

# for key in dictionary:
#   value = dictionary[key]
#   print(key, value)

# decomposing-
# for key, value in dictionary.items():
#   print(key, value)


# len() function:

# dictionary = {
#    "name": "Tobiloba",
#    "role": "Frontend Engineer",
#   "skills": ["Javascript", "Typescript", "Reactjs","Nextjs"]
# }

# print(len(dictionary))  # 3




# .items() method:

# dictionary = {
#    "name": "Tobiloba",
#    "role": "Frontend Engineer",
#   "skills": ["Javascript", "Typescript", "Reactjs","Nextjs"]
# }

# items = dictionary.items()


# print(items[0])  # TypeError: 'dict_items' object is not subscriptable

# print(items)  # dict_items([('name', 'Tobiloba'), ('role', 'Frontend Engineer'), ('skills', ['Javascript', 'Typescript', 'Reactjs', 'Nextjs'])])




# .keys() method:

# dictionary = {
#    "name": "Tobiloba",
#    "role": "Frontend Engineer",
#   "skills": ["Javascript", "Typescript", "Reactjs","Nextjs"]
# }

# keys = dictionary.keys()


# print(keys[0])  # TypeError: 'dict_keys' object is not subscriptable

# print(keys)




# .values() method:

# dictionary = {
#    "name": "Tobiloba",
#    "role": "Frontend Engineer",
#   "skills": ["Javascript", "Typescript", "Reactjs","Nextjs"]
# }

# values = dictionary.values()

# print(values[0])  # TypeError: 'dict_values' object is not subscriptable

# print(values)



# "in" operator:

# dictionary = {
#    "name": "Tobiloba",
#    "role": "Frontend Engineer",
#   "skills": ["Javascript", "Typescript", "Reactjs","Nextjs"]
# }

# contains = "role" in dictionary  # True
# contains = "job" in dictionary  # False

# print(contains)




# Deleting keys:

# dictionary = {
#   "name": "Tobiloba",
#   "role": "Frontend Engineer",
#   "skills": ["Javascript", "Typescript", "Reactjs","Nextjs"]
# }

# del dictionary["skills"]

# print(dictionary)


# Adding Keys:

# dictionary = {"name": "Solutions"}
# dictionary["name"] = "Tobiloba"

# print(dictionary)  # ("name": "Tobiloba"}




# Accessing Dictionaries:

# dictionary = {
#   "1": "Tobiloba",
#    2: "Adedeji",
#    3: True
# }

# print(dictionary[3])




# Creating Dictionaries:

# dictionary = {
#   "1": "Tobiloba",
#    2: "Adedeji",
#    3: True
# }

# dictionary = dict()

# dictionary["name"] = "Tobiloba"
# print(dictionary)