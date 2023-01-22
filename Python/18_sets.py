"""

Notes:

- Sets are collections of unique objects.

- Sets are "unordered" collections of unique elements.

- If you want to make an empty set, use the "set()" function.

- You cannot add a list, dictionary, set; any kind of mutable object in short cannot be added to a set.

- You use a set when you only care if something exists or doesn't exist, not frequency, order or anything else if you care use a dictionary instead.

- .add(item) method: Used to add an item to a set, does not return  a new set.

- .remove(item) method: Used to remove an item from a set, if the item does not exist, it throws an error. Does not return a new set.

- .clear() method: Used to "clear" out a set by removing every item in the set. Doesn't return a new set.

- .union() method: Used to combine 2 sets in a union and returns a new set without duplicates. The symbol "|" can be used to replace the .union() method.

- .intersection() method: Used to find the common elements in two sets and returns a new set that contains those common elements. The symbol "&" can be used to replace the .intersection() method.

- .difference() method: Used to find elements that exist in set one, but, not set two. The elements are returned in a new set. The symbol "-" can be used to replace the .difference() method.

- .symmetric_difference() method: Used to find the differences between both sets and returns them in a new set. The "^" can be used to replace the .symmetric_difference method. 
Hence, 
set_one.symmetric_difference(set_two) == set_two.symmetric_difference(set_one)


- .update() method: Used to modify an existing set to include more items from another set. As expected, all duplicates are removed. Doesn't return a new set.


- .difference_update() method: Used to modify an existing set by changing the set to its difference with another set. Doesn't return a new set, it "modifies". 

For example:
set_one = {1, 2, 3, 4, 3, 1, 2, 8}
set_two = {1, 2, 3, 4, 5, 6, 9}

set_one.difference_update(set_two) == {8}

print(set_one)  # {8}

- .symmetric_difference_update method:  Used to modify an existing set by changing the set to the symmetric differences between it another set. Doesn't return a new set. For example:

set_one = {1, 2, 3, 4, 3, 1, 2, 8}
set_two = {1, 2, 3, 4, 5, 6, 9}

set_one.symmetric_difference_update(set_two) == {6, 8, 9}

print(set_one)  # {5, 6, 8, 9}

- .issuperset(otherset) method: Returns a boolean if the set the method is called on has all the stuff "otherset" has "plus" other stuff. The symbol ">=" can be used to replace the .issuperset() method.

- .issubset(otherset) method: Returns a boolean if the set the method is called on has all its elements existing in "otherset". The symbol "<=" can be used to replace the .issubset() method.

- Proper subset and Proper superset:
 Use the ">" to check if one set is a proper superset of another set and use the symbol "<" to see if one set is a proper subset of another set.

"""


# Set examples:

# my_string = "hello world"

# new_set = set(my_string)

# print(new_set)  # {'h', 'o', 'r', 'd', '', 'l', 'e', 'w'}


# Program that adds numbers to a set and then breaks when a duplicate us entered:

# numbers = set()

# while True:
#   user_number = input("Enter a number: ")

#   if user_number in numbers:
#     break

#   numbers.add(user_number)


# list = [1, 2, 3, 2, 3, 2, 2, 5, 6, 7, 5, 8, 6]

# new_set = set(list)

# print(new_set)  # {1, 2, 3, 5, 6, 7, 8}


# .issubset() method and .issuperset() method:

# set_one = {1, 2, 3, 4, 3, 1, 2, 8}
# set_two = {1, 2, 3, 4, 5, 6, 8, 9}

# print(set_one.issubset(set_two))  # True
# print(set_two.issuperset(set_one))  # True





# .symmetric_difference_update() method:

# set_one = {1, 2, 3, 4, 3, 1, 2, 8}
# set_two = {1, 2, 3, 4, 5, 6, 9}

# set_one.symmetric_difference_update(set_two)

# print(set_one)  # {5, 6, 8, 9}


# .difference_update() method:

# set_one = {1, 2, 3, 4, 3, 1, 2, 8}
# set_two = {1, 2, 3, 4, 5, 6, 9}

# set_one.difference_update(set_two)

# print(set_one)  # {8}



# .update() method:
# set_one = {1, 2, 3, 4, 3, 1, 2, 8}
# set_two = {1, 2, 3, 4, 5, 6, 9}

# set_one.update(set_two)

# print(set_one)  # {1, 2, 3, 4, 5, 6, 8, 9}




# .symmetric_method method:

# set_one = {1, 2, 3, 4, 5, 6, 7, 8}
# set_two = {1, 2, 3, 4, 5, 6, 9}

# symmetric_differences = set_one.symmetric_difference(set_two)

# symmetric_differences = set_one ^ set_two

# print(symmetric_differences)  # {7, 8, 9}



# .difference() method:

# set_one = {7, 8}
# set_two = {1, 2, 3, 4, 5, 6, 9}

# set_difference = set_one.difference(set_two)
# set_difference = set_one - set_two
# settwo_difference = set_two - set_one

# print(set_difference)  # {7, 8}
# print(settwo_difference)  # {1, 2, 3, 4, 5, 6, 9}



# .intersection() method:

# set_one = {1, 2, 3, 4, 5, 6}
# set_two = {2, 5, 10, 11, 19, 20, 22, 12, 7}

# set_intersections = set_one.intersection(set_two)
# set_intersections = set_one & set_two

# print(set_intersections)  # {2, 5}



# .union() method: 

# set_one = {1, 2, 3, 4, 5, 6}
# set_two = {2, 5, 10, 11, 19, 20, 22, 12, 7}

# combined_set = set_one.union(set_two)
# combined_set = set_one | set_two

# print(combined_set)  # {1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 19, 20, 22}



# in operator:

# my_set = {1, 2, 4, 5, 9, 10, "hello", "get this"}

# contains = "get this" in my_set

# print(contains)



# Set restrictions:

# my_set = {1, 2, 3, 4, True, {1, 2, 4}, (1, 2, 3), [1, 2, 3], set()}  # You cannot add mutable data-types to sets, you can only add immutable data types.



# len() function:

# my_set = {1, 2, 3, 2, 2, 1, 3, True, (3, 6), 0.4, 9}

# print(my_set)  # {1, 2, 3, (3, 6), 0.4, 9}
# print(len(my_set))  # 6



# .clear() method:

# my_set = {2, 3, 5, 7}

# my_set.clear()

# print(my_set)  # set() or {}



# .remove() method:

# my_set = {2, 3, 5, 7}

# my_new_set = my_set.remove(3)

# print(my_set)  # {2, 5, 7}
# print(my_new_set)  # Doesn't return a new set.



# .add() method:

# my_set = set({2})

# my_set.add(3)
# my_set.add(5)
# my_set.add(7)

# print(my_set)  # {2, 3, 5, 7}




# Creating sets:

# my_set = set()
# my_other_set = {}  # is empty, hence is a dictionary
# my_new_set = {1, 2, 3, 2, 3, 4, 5}

# print(type(my_set))  # <class 'set'>
# print(type(my_other_set))  # <class 'dict'>
# print(type(my_new_set))  # <class 'set'>
# print(my_new_set)  # {1, 2, 3, 4, 5}