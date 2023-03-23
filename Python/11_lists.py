"""
Notes:

- A list is a data type that stores an ordered collection of elements.

- To access values in a list, indices are used (Python is also zero-indexed)
 
- The "in" keyword in Python is used to check whether a value exists in a collection (sets, list, dict, and so on)

- The len() function also works on strings

- Methods follow the format: "object.method()", while functions 
follow the format: "function(object)"

- True == 1 and False == 0

- The list() function exists
"""

# List function
# list_object = list()
# print(type(list_object))  # <class 'list'>

# Nested lists- Multidimensional lists: 

# list = [[2, 4, [str(1003)]], [3, 7, 9], [100, 200, 50]]
# print(list[0][2][0][3])  # 3, Strings are iterable
        


# .extend() method:

# first_list = [2, 5, 9]
# second_list = [7, 9, 10]

# first_list.extend(second_list)  # [2, 5, 9, 7, 9, 10]
# first_list[0] = 200
# second_list.extend(first_list)  # [7, 9, 10, 200, 5, 9, 7, 9, 10]
# second_list.extend(second_list)  # [7, 9, 10, 200, 5, 9, 7, 9, 10, 7, 9, 10, 200, 5, 9, 7, 9, 10]
# print(second_list)
# print(first_list)


# Adding lists - using the "+":

# first_list = [2, 5, 9]
# second_list = [7, 9, 10]

# combined_list = first_list + second_list
# combined_list[1] = 10
# print(combined_list)  # [2, 5, 9, 7, 9, 10]
# print(first_list)  # [2, 5, 9]
# print(second_list)  # [7, 9, 10]

# The "in" operator- checks if a value is contained in the list: 
# list = [1, 1, 1, 1, 2, 4, "Hello", True, 1, 5]

# value_exists = 5 in list  # True
   # or
# value_exists = list.count(5) > 0

# print(value_exists)


# .remove() method - Remove an element from a list based on the order of its occurrence:

# list = [1, 1, 1, 1, 2, 4, "Hello", True, 1]
# list.remove(1)  # list = [1, 1, 1, 2, 4, "Hello", True, 1]
# list.remove(1)  # list = [1, 1, 2, 4, "Hello", True, 1]
# list.remove(1)  # list = [1, 2, 4, "Hello", True, 1]
# list.remove(1)  # list = [2, 4. "Hello", True, 1]
# list.remove(1)  # list = [2, 4, "Hello", 1]
# print(list)




# .index() method - Returns the index of the first occcurrence of an element:

# list = [1, 1, 1, 1, 2, 4, "Hello", True, 1]
# index_first_found_at = list.index(1)  # 0
# print(index_first_found_at)  # 0
 
 


# .count() method:

# list = [1, 1, 1, 1, 2, 4, "Hello", True, 1]
# element_frequency = list.count(1)  # 6
# print(element_frequency)




# .pop() method-returns the popped value:

# list = [1, 2, 4, "Hello", True]
# popped = list.pop()  # True; list = [1, 2, 4, "Hello"]
# print(list)
# print(popped)  # True



# Minor operations on strings:

# test_string = "Hola Amigos"
# test_string[5] = "O"  # Error, strings are immutable
# print(test_string[5])  # "A"



# len() function:

# list = [1, 2, 4, "Hello bobo", True]
# print(len(list))  # 5
# print(len(list[3])) # 5, len() also works on strings




# .append() method - Add values to the end of a list; resizing it:

# list = [1, 2, 4, "Hello", True]
# list.append(20)  # list = [1, 2, 4, "Hello", True, 20]
# list.append(300)  # list = [1, 2, 4, "Hello", True, 20, 300]
# print(list)


# List Indexing:

# list = [1, 2, 4, "Hello", True]
# print(list[4])  # True
# list[4] = False  # "True" at that index changes to "False"
# print(list[-1])  # Negative indexing works and (in this case) returns False.








