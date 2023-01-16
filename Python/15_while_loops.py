"""
Notes: 

- While loops can do the exact same thing as For loops, but, they have some use cases.

- If you know how many times you need to loop, you can use a "For loop", but, if you don't know how many times you need to loop, you can use a while-loop instead.

"""

# While-Else statement:
# list = [1, 2, 4, 6, 7, 9, 1]

# idx = 0

# while idx < len(list):
#   number = list[idx]
#   if number == 2:
#     print("Found it!")
#     break
#   idx += 1
# else:
#   print("E no dey the list o!!!")



# Looping through a list:
# list = [1, 2, 4, 6, 7, 9, 1]

# i = 0
# result = 0

# while result < 9 and i < len(list):
#   number = list[i]
#   result += number
#   i += 1
  
#   print(number, result)  # 1 1
                         # 2 3
                         # 4 7
                         # 6 13




# "break" keyword:

# while True:
#   number = input("Enter a number: ")
#   if number.isdigit():
#     break




# Infinite while loop:

# while True:
#   number = input("Enter a number: ")




# While loop syntax:

# number = 0

# while number < 5:  # same as -- for i in range(5):
#   print(number)
#   number += 1


# -----------------------------------------

# number = input("Enter a number: ")

# while not number.isdigit():
#   number = input("Enter a number: ")