"""
Notes:

- range(start, stop, step): The range() function creates an iterator that returns integers one by one from start (inclusive) to stop(exclusive), incrementing the last value by "step" everytime.

- Representations of the range() function:
   - range(num): "num" is the "stop" argument and 0 is the "start"
   - range(start, stop)

- There are different ways to iterate using "for loops":
  - Using the range() function
  - Iteration by item
  - Using the enumerate() function

- You use the "pass" keyword when you don't want any operation to be performed when you're in a loop.  
"""

# For Else statement:
# For example, without For Else statement:

# words = ("hello", "oya", "kilode", "what's up")
# target = "kiloshele"

# found = False

# for element in words:
#   if element == target:
#     print("Found it!")
#     found = True

    
# if not found:
#   print("The word no dey there!!")


# With For else statement:

# words = ("hello", "oya", "kilode", "what's up")
# target = "kiloshele"

# for word in words:
#   if word == target:
#      print("Found it!")
#      break

# else:
#   print("The word no dey there!!")



# pass keyword:

# for i in range(3):
#   pass



# for loop examples:

# numbers = []

# for i in range(3):
#   num = input("Enter a number: ")
#   numbers.append(int(num))
  
# print(numbers)  # [4, 4, 8]



# Nested for loops:
# nested_list = [[0, 3], [0, 5], [8, 18]]

# for i in range(len(nested_list)):
#   interior_list = nested_list[i]
#   for element in interior_list:
#     print(element)  # [0, 3, 0, 5, 8, 18]


# for i in range(10):
#   for j in range(10):
#     for w in range(2):
#       print(i, j, w)

      

# continue keyword:
# list = [1, 2, 3, 4, 5, True, False]

# for num in list:
#   if num == 4:
#      continue  # Skip the step
#   print(num)  

# print("Done!")  



# break keyword:
# list = [1, 2, 3, 4, 5, True, False]

# for num in list:
#   if num == 4:
#     break  # break out of the loop
#   print(num)  

# print("Done!")  



# looping through strings:
# string = "my very long string"

# for i in range(0, len(string), 2):
#   print(string[i])


# looping through tuples:

# tuple = (1, 2, 3, 4, 5, True, False)

# for i in range(len(tuple)):
#   print(i, tuple[i], "Yay") 

# for element in tuple:
#   print(element)

# for i, element in enumerate(tuple):
#   print(i, element)



# Using the enumerate() keyword:

# list = [1, 2, 3, 4, 5, True, False]

# for i, element in enumerate(list):
#   print(i, element)


# Iteration by item:

# list = [1, 2, 3, 4, 5, True, False]

# for element in list:
#   print(element)


# Looping through lists:

# list = [1, 2, 3, 4, 5, True, False]

# for idx in range(len(list)):
#   print(list[idx])




# range() function:

# sum_to_ten = 0
# for i in range(11):  # Sum numbers from 1 to 10:
#   sum_to_ten += i
# print(sum_to_ten)  
  
  
# for i in range(10, -20, -5):
#   print(i)

# for i in range(-5, -20, -5):
#   print(i)

# for i in range(5, 30, 3):
#   print(i)

# for i in range(5, 30):
#   print(i)




# For loop syntax:

# for i in range(30):
#   print(i, "hello")


