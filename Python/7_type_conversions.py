"""
Convert:

- str to int -- use int() function
- float-like string (e.g "4.5") to number -- use float() function
- float to int -- use int()
- int to float -- use float()
- to str -- use str()
- to bool -- use bool()
"""

# Example:
# Write a simple program that takes input from a user (The program assumes the input is an integer or float) and then adds 4 to it


input_number = input("Enter your number: ")
input_plus_four = float(input_number) + 4
print("The result is:", input_plus_four)




# Converting to str:

# x = str(0) + "0"
# print(x)


# Converting to bool: This follows Truthy and Falsy as in Javascript
"""
Truthy: "0", 23, True, 1, -7
Falsy: "", 0, False
"""
# x = bool("0") // returns True
# print(x)



# Converting to int:

# x = "4"
# y = int(x)

# print(type(y))
# print(type(x))

# y = int("4  ") + 4  # returns 8
# print(y)


# x = int(4.5)  # TypeError
# print(x)



# Converting to float:

# x = float("4.5") + 4
# print(x)

# x = float(4) + 4
# print(x)
