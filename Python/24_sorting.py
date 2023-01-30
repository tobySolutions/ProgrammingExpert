"""
Notes:

- There are 2 ways to sort in Python:

   - sorted() function: returns a new list with the items in ascending order (by default). It doesn't modify the original object.

   - .sort() method: sorts the object in place, doesn't return a new object. Doesn't work on tuples; due to their immutability

- Any of the arguments that you can pass to .sort() can be passed to sorted().

- Whenever you use the sorted() function on tuples, it returns a new list.

- You can pass another "key" argument to both sorting functions and use a helper function to define the criteria for sorting, for example:

   def sort_by_second_item(my_list):
    return my_list[1]

 
  my_list = [1, 2, 5, 5, 12, 8, 0, 19, 7, 4, 3, 8]

  --1
  print(sorted(my_list, key=sort_by_second_item))  

  --2
  my_list.sort(key=sort_by_second_item)
  print(my_list)

- By default, when the .sort() method or sorted() function is called on a multi-dimensional list, the sort happens based on the first items in the sub-lists. This can be changed though with the "key" argument.
"""


# Sorting by key:

# def sort_second_index(item):
#   return item[1]
  


# my_list = [[1, -2], [3, -4], [5, -6], [-1, -2], [0, 0]]

# new_sorted_list = sorted(my_list, key=sort_second_index)

# print(new_sorted_list)  # [[5, -6], [3, -4], [1, -2], [-1, -2], [0, 0]]

# my_list.sort(key=sort_second_index)

# print(my_list)  # [[5, -6], [3, -4], [1, -2], [-1, -2], [0, 0]]




# my_list = [[1, -2], [3, -4], [5, -6], [-1, -2], [0, 0]]

# my_list.sort()  # [[-1, -2], [0, 0], [1, -2], [3, -4], [5, -6]]

# print(sorted(my_list))  # [[-1, -2], [0, 0], [1, -2], [3, -4], [5, -6]]

# print(my_list)




# Sorting Tuples:

# my_tuple = (1, 2, 5, 5, 12, 8, 0, 19, 7, 4, 3, 8)


# print(tuple(sorted(my_tuple)))  # [0, 1, 2, 3, 4, 5, 5, 7, 8, 8, 12, 19]

# print(my_list.sort())  # AttributeError: 'tuple' object has no attribute 'sort'

# print(my_tuple)




# Sorting in Descending order:

# my_list = [1, 2, 5, 5, 12, 8, 0, 19, 7, 4, 3, 8]

# print(my_list.sort(reverse=True))  # None
# print(my_list)  # [19, 12, 8, 8, 7, 5, 5, 4, 3, 2, 1, 0]



# my_list = [1, 2, 5, 5, 12, 8, 0, 19, 7, 4, 3, 8]

# print(sorted(my_list, reverse=True))  # [19, 12, 8, 8, 7, 5, 5, 4, 3, 2, 1, 0]

# print(my_list)  # my_list



# Sorting lists:

#  using sorted() function:

# my_list = [1, 2, 5, 5, 12, 8, 0, 19, 7, 4, 3, 8]

# print(sorted(my_list))  # [0, 1, 2, 3, 4, 5, 5, 7, 8, 8, 12, 19]
# print(my_list)  # my_list



#  using .sort() function:
# my_list = [1, 2, 5, 5, 12, 8, 0, 19, 7, 4, 3, 8]

# print(my_list.sort())  # None
# print(my_list)  # [0, 1, 2, 3, 4, 5, 5, 7, 8, 8, 12, 19]