"""
Notes:

- Whenever you add, subtract, multiply and divide a "float" with/by an "int" the result is always going to be a "float"

- The integer division operator "//" just chops off the decimal part. It doesn't round up or down.

- Operator precendence in Python is PEMDAS or BODMAS

- When you face operators that have the same precedence, whichever comes first in the expression is executed first.

- In Python, True === 1 and False === 0

- You'll get "ZerODivisionError" if you try to divide by "0" or "False", and if you mod another number by  "0"
"""


# Operands
# x = 5
# y = 3

# result = x + y  # "+" is an operator, "x" and "y" are operands, result is an expression.

# print(result)

# Addition

# x = 1.0
# y = 2

# result = x + y  # 3.0, float + int = float

# print(result)



# Subtraction

# x = -2.0
# y = -4

# result = x - (-y) # -6.0, float - int = float  
              #or
# result = x - -y  # -6.0, float - int = float  
# print(result)


# Multiplication

# x = 5.0
# y = 3

# result = x * y  # 15.0,  float * int = float  

# print(result)




# Division

# Float division operator
# x = 35.2
# y = 7.4

# result = x / y
# print(result)


# Integer division operator

# x = 33
# y = 7

# result = x // y # This will return just "4", it will chop off the decimals
# print(result)

# However

# x = 33.0
# y = 7

# result = x // y  # returns 4.0,  float // int = float  

# print(result)




# Exponential

# x = 5
# y = 3

# result = 5 ** 3

# print(result)


# Modulus

# x = 19
# y = 3
# z = 0
# j = 1

# result = x % y  # returns 1
# result = x % z  # ZeroDivisionError
# result = z % x  # returns 0
# result = j % x  # returns 1

# print(result);



# Operator Precedence

# x = 11
# y = 2

# result = x % y + 4 - 7 ** (2 / 3)

"""
 Operator precedence in Python:
 PEMDAS
 
 - Bracket/Parantheses
 - Exponent
 - Multiplication, Division, Modulus
 - Addition, Subtraction
"""

# print(result)


# Using Operators with the wrong data types:

answer = "5" + 6  # can only concatenate str (not "int") to str

# print(answer)