"""
Notes:

- "Scope" has to do with where specific values and variables are accessible from.

- We can look outside our scope (from a fuction scope or a block scope), but, the outside (global scope) can't look inside our scope.

- The usage of the "global" keyword is considered bad practice.

- Using the "global" keyword within a function in your program introduces a "side effect" in your program and can cause bugs that might be hard to trace when you have a bigger codebase.
"""


# "global" keyword:

# value = 10

# def change_global_value():
#   global value
#   value = 20
#   print(value)


# print(value)  # 10 
# change_global_value()  # 20
# print(value)  # 20



# Scope with mutable objects:

# def append_5(any_list):
#   any_list.append(5)
#   print(any_list)


# my_list = []  

# print(my_list)  # []
# append_5(my_list)  # [5]
# print(my_list)  # [5]


# Scope examples:

# def add_5(x):
#   x = x + 5
#   print(x)

# x = 10

# print(x)  # 10
# add_5(x)  # 15
# print(x)  # 10



# def check_numbers_greater_than_5():
#   if user_input > 5:
#     value = "Number is greater than 5!"
#   else:
#     value = "Number is less than or equal to 5!"
#   print(value)


# user_input = int(input("Enter a number: "))
# check_numbers_greater_than_5()




# Block scope:
  
# any_input = int(input("Enter a number: "))

# if any_input > 5:
#   value = "Number is greater than 5!"   # "value" will be created when "any_input" is greater than 5.

# print(value) 



# Function scope:

# x = 1

# def access_from_right_scope():
#   print(x)
  
# access_from_right_scope()  # 1
# print(x)  # 1


# x = 1

# def access_from_right_scope():
#   x = 12
#   print(x)
  


# print(x)  # 1
# access_from_right_scope()  # 12
