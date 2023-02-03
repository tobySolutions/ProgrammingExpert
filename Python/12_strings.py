"""
Notes:

- The "str" datatype (String) represents a sequence of characters.

- Strings are immutable

- "\n" the newline character is used to to move the cursor to the next line and it is invisible

- Escape characters begin with a backslash ("\")

- .find() method- Returns the index of the first occurrence of a character if it exists or else it returns "-1"

- .count() method - Returns the frequency of the character in the original string

- .upper() method - Converts each character in the origin string to uppercase.

- .lower() method - Converts each character in the origin string to lowercase.

- .capitalize() - Capitalizes the first letter of a string

- .isdigit() - Checks whether a string when converted to an int is a valid int.

- .split(delimiter) - Takes in a delimiter/separator (stuff to split based on) and then returns an array of strings with the delimiter removed.

- .replace(existing_value, new_value) - Replaces every occurrence of a value with another value

- .join(delimiter) - Takes in a delimiter/separator (stuff to join based on) and then returns a string with the delimiter removed.
"""

# .join() method:

# name = ["Type", "any", "string","you", "want"]
# joined_string = "hello".join(name)
# print(joined_string)  # Typehelloanyhellostringhelloyouhellowant



# Escape character:
# name = input("What is your name? ")
# print(f'{name}\'s name is correct!')


# Multiline strings:

# string = """
# Hello, I am a multiline string!
# """

# print(string)



# string multiplication:

# word = input("Enter a word: ")
# print(word * 4)  #numbernumbernumber


# f-strings:

# number = int(input("Enter a nunmber: "))
# output_text = f"Number plus 10 is {number + 10}"
# print(output_text)


# .replace(existing_value, new_value):

# string = "hello,my,name,,,is,tim"
# new_string = string.replace(",", "|")
# print(new_string)  



# .split() method:

# string = "hello,my,name,is,tim"
# words = string.split(",")  # ["hello", "my", "name", "is", "tim"]

# string = "hello,my,name,,,is,tim"
# words = string.split(",")  # ["hello", "my", "name", "", "", "is", "tim"]

# print(words)  





# Practice example:

# number = input("Input a number: ")

# if number.isdigit():
#   print("It is a number")
#   number = int(number)
#   print(number + 5)
# else:
#   print("This is not an int")



# .isdigit():

# string = "19"
# string_not_int = "19h"
# string_float = "19.7"

# print(string_float.isdigit())  # False
# print(string_not_int.isdigit())  # False
# print(string.isdigit())  # True



# in operator:

# string = "Tobiloba"
# contains = "h" in string  # False
# contains = "i" in string  # True
# print(contains)


# .capitalize():

# string = "tobiloba"
# print(string.capitalize())


# Practice example - (Using lower() method):
# answer = input("What is your name? ")

# if answer.lower() == "tobiloba":
#   print("Correct!")
# else:
#   print("Incorrect!")



# .lower() method:

# string = "Tobiloba"
# lower = string.lower()
# print(lower)


# .upper() method:

# string = "Tobiloba"
# upper = string.upper()
# print(upper)


# .find() method: 

# string = "Tobiloba"
# index = string.find("o")  # 1
# index = string.find("q")  # -1
# print(index)  # 1


# .count() method:

# string = "Tobiloba"
# count = string.count("b")  # 2
# print(count)  # 2



# String Recap:

# string = "Tobiloba"
# print(string[2])  # "b"
# print(string[-3])  # "o"
# print(len(string))  # 8






