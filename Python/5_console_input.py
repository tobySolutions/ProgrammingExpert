"""
- The input function only returns a string, so if you need to use an int, you will have to convert it

- The input function takes in a prompt (only one string argument) and allows you to type stuff.

- Though the input function takes in just one argument, it allows you to concatenate with the "+" in case you want to use variables that you created elsewhere.

- The input doesn't capture anything until you hit Enter.
"""

# input("Number: ")

# using variables
# number = input("Number: ")
# print(number)


# print can take more than one argument, input can't
# name = input("Enter your name: ")
# print("Hello,", name) 

# You can check the types of the return values to confirm
# number = input("Enter a number: ")
# print(type(number))


# Multiple inputs
input("Press Enter to begin")
name = input("Enter your name: ")
age = input("Enter your age " + name + ": ") # concatenation with "+" works in the input function

print("Hello " + name + "!" + " Your age is ", age) # The comma provides default spacing