"""
Notes: 

- An exception in Python is "raised" when something unexpected happens during the execution of your program.

- You can use a try-except block to handle exceptions and prevent your program from crashing only when you've anticipated that it might happen; not just for fun.

- You can handle specific exceptions in your "except" block.

- The finally block is used for cleanup operations most times.

- YOU SHOULDN'T ALWAYS SURROUND EVERYTHING WITH TRY-EXCEPT BLOCKS, ONLY WHEN YOU KNOW A SPECIFIC ERROR COULD OCCUR.

- It's not good practice to accept "General exceptions".

- Compile-time exceptions occur and are raised even before the program is run (mostly syntactical related)

- Runtime exceptions occur while the program is running (most of them have exception classes that they're raised by.).

- Exceptions are caught by the except block in-order (whichever comes first). When an exception is encountered, it terminates the program
"""

# Exception Examples:

# program that asks for an input from a user and runs until a float is input by the user
# while True:
#   number = input("Enter a number: ")
#   try:
#     number = float(number)
#     break
#   except ValueError:
#     print("Not a valid float, try again")


# number = input("Enter a number: ")

# if not number.isdigit():
#   raise ValueError("This is not a valid Integer!")



# raising exceptions:

# raise Exception("This could be any exception.")
# raise ValueError("This is a value error exception.")
# raise ZeroDivisionError("This is a zero division error.")
# raise KeyError("This is a key error")



# finally block:

# try:
#   int("Hola!")
#   2 / 0
# except Exception as e:
#   print("There is an exception of:", e)
# finally:
#   print("We're done! Code here runs regardless sha.")
#   print("Code here can also be used to handle cleanups")



# Handling General exceptions:

# try:
#   int("Hola!")
#   2 / 0
# except Exception as e:
#   print("There is an exception of:", e)



# Handling specific exceptions:

# try:
#   2 / 0
#   int("Hola!")
# except ValueError as e:
#   print("Value Exception:", e)
# except ZeroDivisionError as e:
#   print("Zero Division Exception", e)
  
# print("Done!")



# Handling Exceptions:

# try:
#   int("hello")
# except:
#   print("Exception dey o!!")

# print("Done.")