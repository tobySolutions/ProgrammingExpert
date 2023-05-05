"""
Notes:

- An iterator is a special kind of object that implements a single function: "next()".

- An iterator is a special object that allows us to loop through an iterable object.

- An iterable object is any object that has a method that allows it to get an iterator ("__iter__()")

- For you to do an iteration on an iterable object, you first have to convert the iterable object to an iterator.

- What makes something an iterator is that it has a "__next__()" method.


- For an iterable object, this is possible:
    my_list = [1, 2, 3]
    my_iterator = my_list.__iter__()


- For an iterator, this is possible:
      my_list = [1, 2, 3]
      my_iterator = my_list.__iter__()

      print(my_iterator.__next__())  1

- A for-loop underneath handles the conversion of an iterable object to an iterator.

- A self-contained-iterator is not a good idea as internal state will be shared across all the iterators of it.
"""





# Self-contained Iterator:

# class Numbers: 
#   def __init__(self, num1, num2, num3):
#     self.num1 = num1
#     self.num2 = num2
#     self.num3 = num3
#     self.current = 0

#   def __iter__(self):
#     self.current = 0
#     return self

#   def __next__(self):
#     self.current += 1
      
#     if self.current == 1:
#       return self.num1
#     elif self.current == 2:
#       return self.num2
#     elif self.current == 3:
#       return self.num3
#     else:
#       raise StopIteration
  


# nums = Numbers(1, 2, 3)
# num_iterator1 = iter(nums)
# print(next(num_iterator1)) # 1

# num_iterator2 = iter(nums)
# print(next(num_iterator1)) # 1
# print(next(num_iterator2)) # 2
# print(next(num_iterator1)) # 3


      
      
# Using Custom Iterators:

# class Numbers:
#   def __init__(self, num1, num2, num3):
#     self.num1 = num1
#     self.num2 = num2
#     self.num3 = num3

#   def __iter__(self):
#     return NumberIterator(self.num1, self.num2, self.num3)



# class NumberIterator:
#   def __init__(self, one, two, three):
#     self.one = one
#     self.two = two
#     self.three = three
#     self.current = 0

#   def __next__(self):
#     self.current += 1
#     if self.current == 1:
#       return self.one
#     elif self.current == 2:
#       return self.two
#     elif self.current == 3:
#       return self.three
#     else:
#       raise StopIteration


      

# numbers = Numbers(1, 2, 3)   

# for number in numbers:
#   print(number)


  

# Creating Iterators:

# class Numbers:
#   def __init__(self, num1, num2, num3):
#     self.num1 = num1
#     self.num2 = num2
#     self.num3 = num3

#   def __iter__(self):
#     return NumberIterator(self.num1, self.num2, self.num3)



# class NumberIterator:
#   def __init__(self, one, two, three):
#     self.one = one
#     self.two = two
#     self.three = three
#     self.current = 0

#   def __next__(self):
#     self.current += 1
#     if self.current == 1:
#       return self.one
#     elif self.current == 2:
#       return self.two
#     elif self.current == 3:
#       return self.three
#     else:
#       raise StopIteration


      

# numbers = Numbers(1, 2, 3)      
# my_iterator = iter(numbers)
# # print(my_iterator)  # Check to see if it works
# print(next(my_iterator))  # 1
# print(next(my_iterator))  # 2
# print(next(my_iterator))  # 3



      
# How for-loops work:

# my_list = [1, 2, 3]

# my_iterator = my_list.__iter__()

# while True:
#   try:
#     print(my_iterator.__next__())
#   except StopIteration:
#     break
    


# my_list = [1, 2, 3]

# my_iterator = iter(my_list)

# while True:
#   try:
#     print(next(my_iterator))
#   except StopIteration:
#     break
    



# next() and __next__():

# my_list = [1, 2, 3]

# my_iterator = iter(my_list)

# print(next(my_iterator))  # 1
# print(next(my_iterator))  # 2
# print(next(my_iterator))  # 3
# print(next(my_iterator))  # StopIteration exception


    


# iter() and __iter__():

# my_list = [1, 2, 3]

# my_iterator = iter(my_list)

# print(my_iterator)  # <list_iterator object at 0x7f87a0c194c0> (memory adress subject to change)