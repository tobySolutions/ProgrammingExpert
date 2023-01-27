"""
Notes:

- A function is a reusable block of code that we call upon to do something.

- "arguments" are values that are passed into a function, while "parameters" are values that are read by that function.

- By default, arguments to functions are passed in positionally, we can also use the keyword syntax:
  do_something(paramater_name = argument)

- You cannot have a parameter that doesn't have a default parameter come after one that does have a default parameter.

- The "return" statement basically ends a function's execution. Everything after the "return" line is not executed.

- Also, you can write functions inside of functions.
"""

# Function examples:

# def sum_lists(list1, list2):
#   list1_sum = sum_list(list1)
#   list2_sum = sum_list(list2)

#   return list1_sum, list2_sum


# def sum_list(my_list):
#   total = 0

#   for value in my_list:
#     total += value
#   return total  



# sum1, sum2 = sum_lists([10, 9, 49, 59, 100], [20, 30, 40])  

# print(sum1, sum2)  # 227, 90
  

  
# def remove_chars(base, chars):
#   new_string = base
#   for char in chars:
#     new_string = new_string.replace(char, "")

#   return new_string

# result = remove_chars("hello world", "lo")

# print(result)  # he wrd
  
  



# Returning multiple values:

# def return_values(x, y):
#   return x + 1, y + 1


# x, y = return_values(1, 2)
# print(x, y)  # 2, 3


# Optional/ Default parameters:

# def new_range(stop, start=0):
#   x = start

#   while x < stop:
#       print(x)  
#       x += 1


# new_range(20) 


# def new_range(start=0, stop=10):
#   x = start

#   while x < stop:
#       print(x)  
#       x += 1


# new_range(12, 20)



# def new_range(start, stop):
#   x = start

#   while x < stop:
#       print(x)  
#       x += 1


# new_range(1, 10)



# return values:

# def get_negative_sum(x, y, z):
#   result = x + y + z + 5
#   if result < 0:
#     return result
    
#   return 1

# x = -3
# y = -5
# z = -3

# result = get_negative_sum(x, y, z)
# print(result)
  
  
# def add_five(x, y, z):
#    result = x + y + z + 5
#    return result

# first_number = 5
# second_number = 5
# third_number = 5

# sum_result = add_five(first_number, second_number, third_number)  # 20

# print(sum_result)




# Multiple function parameters:

# def add_five(first_number, second_number):
#    result = first_number + second_number + 5
#    print(result)

# add_five(5, 5)  # 15




# Function parameters:

# def print_value(value):
#   print(value)


# print_value("Get out!!")  # Get out!!
# print_value("Come here!")  # Come here!
# print_value("Stop that!")  # Stop that!
# print_value("Heya!!")  # Heya!!





# Creating functions:

# def print_value(value):
#   print(value)


# print_value("Hola!!")  # Hola!


