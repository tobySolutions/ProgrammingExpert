"""
Notes:

- A condition is an expression that evaluates to True or False
- ASCII - American Standard Code For Information Interchange
- Use ord() function to check the ASCII code of a character
- Use chr() function to check the character represented by an integer.
- When comparing strings, the ASCII codes of each character in the strings is compared starting from the first character.
"""

# What are Conditions

# Equal-to operator (Equivalence operator)
# is_false = 3.1 == 3.0
# is_true = 3 == 3
# is_also_true = 3.0 == 3


# Not-equal-to operator
# is_false = 3.0 != 3  # False
# is_true = 3.1 != 3.0  # True



# Less than operator
# x = 5
# y = 4

# condition = x < y + 4  # RHS is greater


# Greater than operator
# x = 5
# y = 4

# condition = x + 10 > y + 4  # LHS is greater


# Less than or equal to
# x = 5
# y = 4

# condition = x + 3 <= y + 4  # It is equal to but not less than; so True
# condition = y <= x  # True


# Greater than or equal to
# x = 10
# y = 16
# z = 16

# condition = y >= x  # True
# condition = y >= z  # True


# Comparing Different Types

# condition =  6 >= '6'  # Error, you can't compare two different datatypes

# condition = "4" == 4  # False, they are of different types

# condition = "4" != 4  # True




# Comparing Strings
# first_string = "hello"
# second_string = "Hello"
# third_string = "hello "
# fourth_string =  "aBc"
# fifth_string = "ABc"

# condition = second_string > first_string  # False
# condition = first_string > second_string  # True
# condition = first_string == second_string  # False
# condition = first_string != second_string  # True
# condition = first_string == third_string  # False
# condition = second_string <= first_string  # True
# condition = third_string >= first_string  # True

# condition = fifth_string > fourth_string  # False
# print(ord(" ")) # 32




# Strange Comparisons
# condition = True == 1  # True
# condition = False == 0  # True

# print(is_false)  # False, they're not equal
# print(is_true)  # True, they're equal
# print(is_also_true)  # True, the values match
# print(condition)