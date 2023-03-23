"""
Notes:
- The "Python.exe" is the Python Interpreter.

- File operations:
  - Creating files
  - Reading files
  - Writing to files
  - Appending to files


- Use the open() function most times to perform operations with files:
  Three modes exist:
    - Write mode ("w")
    - Read mode ("r")
    - Append mode ("a")
    - An additional "read-plus" mode (r+): allows you to read and write to a file; has certain issues with 
      cursor placement.
    
- When you use the open() function, do not forget to use the .close() method later on to close the file after      all your logic

- By default, when you use the open() function, the file is already in "read" ("r") mode.

- The "write mode" ("w") overrides a file with a new version if the name of the file matches the one passed in to the open() function.

- The "append mode" ("a") places the cursor at the last line immediately after the last character of the file.     If you want the cursor to go to the next line, you'll have to use the "\n" (next-line escape character) before   the items to be appended to the file.

- There are 2 ways to open files in Python:

  - Using the regular variable syntax: Open the file with the open() method in a variable, and then use the .read() method to read the file line by line, you can then close the file with the .close() method manually.

  - Use a context manager: In the form of  "with open("file.txt", "r") as file:" which automatically closes the 
    file when it's done.

- When reading files, blank lines are read as "\n" character.

- The .readlines() method returns a list that contains the lines of the file.

- The .strip() method removes any trailing "\n" to the left or right.

- The .seek() method takes one of 3 possible arguments and controls the cursor, they are:
  - 0: Beginning of the file
  - 1: Current position of the cursor
  - 2: End of the file
"""

# Reading specific number of characters:

# ==================

# with open("file3.txt", "r+") as file:
#   print(file.read(3))  # tes


# ==================



# Iterating over a file:

# ==================

# with open("file3.txt", "r+") as file:
#   for i, line in enumerate(file):
#     print(line, end="")

#     if i == 2:
#       break


# ==================




# .seek() method:

# ==================

# with open("file4.txt", "r+") as file:
#   score = file.read()
#   new_score = int(score) + 1
#   file.seek(2) 
#   file.write(str(new_score))


# ==================

# with open("file4.txt", "r+") as file:
#   score = file.read()
#   new_score = int(score) + 1
#   file.seek(1) 
#   file.write(str(new_score))
  
  

# ==================

# with open("file4.txt", "r+") as file:
#   score = file.read()
#   new_score = int(score) + 1
#   file.seek(0)  # moves the cursor to overwrite the file like we wanted
#   file.write(str(new_score))
  
  
# ==================






# r+ file mode:

# ==================

# with open("file4.txt", "r+") as file:
#   score = file.read()
#   new_score = int(score) + 1
#   file.write(str(new_score))
  
  

# ==================

# with open("file3.txt", "r+") as file:
#   file.write("\ntest!")
  

# ==================




# Appending to files:

# ===================

# with open("file3.txt", "a") as file:
#   file.write("\nhello\n")
#   file.write("hello\n")
#   file.write("hello")


# ===================





# Writing to and creating files:

# ===================

# with open("file3.txt", "w") as file:
#   file.write("hello\n")
#   file.write("hello\n")
#   file.write("hello")


# ===================

# ===================

# with open("file2.txt", "w") as file:
#   file.write("Hello world, this is my file 2 created with code and written to as well")


# ===================

# ===================

# with open("file2.txt", "w") as file:
#   file.write("Hello world, this is my file 2 created with code and written to as well")


# ===================

# ===================

# with open("file2.txt", "w") as file:
#   pass

# ===================






# Dealing with escape characters:

# ===================

# with open("file_with_next_line.txt", "r") as file:
#   line1 = file.read()
#   line1 = line1.replace("\n", "")
#   print([line1])


# ===================

# with open("file_with_next_line.txt", "r") as file:
#   line1 = file.readlines()[0]
#   line1 = line1.replace("\n", "")
#   print(line1)

# ===================

# with open("file_with_next_line.txt", "r") as file:
#   line1 = file.readlines()[0]
#   # print([line1])
#   print([line1.strip()])

# ===================

# with open("file_with_next_line.txt", "r") as file:
#   # print(file.read())
#   print(file.readlines())  # ['Hello World!\n', 'add line\n', '\n', '\n']

# ===================






# Reading files:

# ===================

# with open("file.txt", "r") as file:
#   print(file.read())  # Hello world

# ===================

# file = open("file.txt", "r")
# print(file.read())  # Hello World!
# file.close()

# ===================

# file = open("file.txt", "w")  # write mode

# ===================

# file = open("file.txt", "r")  # Same as below

      
# ====================

# file = open("file.txt")

# ====================