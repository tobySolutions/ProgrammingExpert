"""
Notes:

- Conditions that contain the logical operators (not, and, or) are called "Compound conditions".

- Operator precendence with Logical operators:
PEMDASNAO in Python
   - Parantheses/ Brackets
   - Exponents
   - Multiplication
   - Division
   - Addition
   - Subtraction
   - not
   - and
   - or

- De Morgan's Laws:
   - not (x and y) == (not x) or (not y)
   - not (x or y) == (not x) and (not y)


- Truth Tables:
   To determine the amount of combinations of True and False use:
   2^number_of_variables

Variables = S  T  (S,T: 2^2 == 4, so we'll have 4 combinations)
            ----
1            F  F
2            T  F
3            F  T
4            T  T

We'll also have the alternations (False and True pairs) of True and False be based on 1, 2, 4, 8, 16, 32, 64....2n.

- You can use Truth tables to help simplify Boolean Algebra that has been broken down by De Morgan's law (for example)
"""


# and operator:

x = 4
y = 6

# condition = x < y and x + 4 > y  # True


# or operator:

# condition = x < y or x > y or x + y > 10.5  # True



# not operator  # PEMDASNAO
# condition = not (x < y or x > y or x + y > 10.5)


print(condition)