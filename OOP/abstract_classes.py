"""
Notes:

- An "abstract class" is a class that contains at least one "abstract method" and is not meant to instantiated. Abstract classes are meant to be the parent / base class in an inheritance hierarchy.

- An "abstract method" is a method that is defined inside an "abstract class" or interface and does not have an implementation; abstract methods are designed to be overriden by it's sub-classes (classes that inherit from it).

- Abstract methods have no implementation whatsoever, you can maybe raise exceptions wih them (NotImplementedError()).

- Abstract classes can contain "instance methods", "class methods", "static methods" as well.

- In Python, since there is no way to denote "abstract classes" or enforce them, we use the naming covention of prefixing the class with "Abstract-", for example: 
    class AbstractBoy:
      pass
"""


# Another Example of Abstract class implementation:
# import random

# class AbstractGame:

#   def start(self):
#     while True:
#       start = input("Would you like to play? ")
#       if start.lower() == "yes":
#         break
#     self.play()

#   def end(self):
#     print("The game has ended.")
#     self.reset()

#   # The abstract methods
#   def play(self):
#     raise NotImplementedError("You must provide an implementation for play()")

#   def reset(self):
#     raise NotImplementedError("You must provide an implementation for reset()")


# class AnotherGame(AbstractGame):
#   pass


# class RandomGuesser(AbstractGame):
#   def __init__(self, rounds):
#     self.rounds = rounds
#     self.round = 0

#   def reset(self):
#     self.round = 0
    
#   def play(self):
#     while self.round < self.rounds:
#       self.round += 1

#       print(f"Welcome to round {self.round}. Let's begin!")
    
  
#       random_number = random.randint(0, 10)
#       while True:
#         guess = input("Guess a number from 1-10: ")
#         if random_number == int(guess):
#           print("You got it!")
#           break
      

#     self.end()

  

# my_games = [AnotherGame(), RandomGuesser(2)]    

# for game in my_games:
#   game.start()  # NotImplementedError: Ypu must provide an implementation for play()
    
    



# Implementing an Abstract class; build a Guessing Game:
# import random

# class AbstractGame:

#   def start(self):
#     while True:
#       start = input("Would you like to play? ")
#       if start.lower() == "yes":
#         break
#     self.play()

#   def end(self):
#     print("The game has ended.")
#     self.reset()

#   # The abstract methods
#   def play(self):
#     raise NotImplementedError("You must provide an implementation for play()")

#   def reset(self):
#     raise NotImplementedError("You must provide an implementation for reset()")




# class RandomGuesser(AbstractGame):
#   def __init__(self, rounds):
#     self.rounds = rounds
#     self.round = 0

#   def reset(self):
#     self.round = 0
    
#   def play(self):
#     while self.round < self.rounds:
#       self.round += 1

#       print(f"Welcome to round {self.round}. Let's begin!")
    
  
#       random_number = random.randint(0, 10)
#       while True:
#         guess = input("Guess a number from 1-10: ")
#         if random_number == int(guess):
#           print("You got it!")
#           break
      

#     self.end()

  
# my_game = RandomGuesser(2)
# my_game.start()
    
    





# Abstract methods:

# class AbstractGame:

#   def start(self):
#     while True:
#       start = input("Would you like to play? ")
#       if start == "yes":
#         break
#     self.play()

#   def end(self):
#     print("The game has ended.")
#     self.reset()

#   # The abstract methods
#   def play(self):
#     raise NotImplementedError("You must provide an implementation for play()")

#   def reset(self):
#     raise NotImplementedError("You must provide an implementation for reset()")




    
# Creating Abstract classes:

# class AbstractGame:

#   def start(self):
#     while True:
#       start = input("Would you like to play? ")
#       if start == "yes":
#         break

#   def end(self):
#     print("The game has ended.")


