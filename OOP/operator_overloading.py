"""
Notes:

- Operator overloading is the ability to implement custom operations on our own classes.

- With operator overloading, you can make your own custom objects act like built-in objects in Python.

- "Dunder methods" are methods that are prefixed and suffixed by two underscores.

- "Dunder methods" are also known as "Magic methods".

- Dunder methods are built-in to Python and they affect built-in operators and operations.

- repr() returns the internal representation of objects in Python

- There are a lot "dunder methods" in Python; __init__() being one of them.

- __add__() method: This method is responsible for overloading the operator "+". It makes it such that you can perform the addition operation on every instance (object) of your class. 

- __sub__() method: This method is responsible for overloading the operator "-". It makes it such that you can perform the subtraction operation on every instance (object) of your class. 

- __mul__() method: This method is responsible for overloading the operator "*". It makes it such that you can perform the multiplication operation on every instance (object) of your class. 

- __truediv__() method: This method is responsible for overloading the operator "/". It makes it such that you can perform the float-division operation on every instance (object) of your class. 

- __floordiv__() method: This method is responsible for overloading the operator "//". It makes it such that you can perform the integer division operation on every instance (object) of your class. 


- __len__() method: This method is responsible for overloading the function len(). It makes it such that you can use the len() function on every instance (object) of your class. There are some issues with floats though when it comes to this; it has be an integer strictly.

- __eq__() method: This method is responsible for overloading the operator "==". It makes it such that you can perform the comparison operation on every instance (object) of your class. 

- __ne__() method: This method is responsible for overloading the operator "!=". It makes it such that you can perform the not equal-to operation on every instance (object) of your class. 


- __gt__() method: This method is responsible for overloading the operator ">". It makes it such that you can perform the greater-than operation on every instance (object) of your class. 

- __ge__() method: This method is responsible for overloading the operator ">=". It makes it such that you can perform the greater-than-or-equal-to operation on every instance (object) of your class. 

- __lt__() method: This method is responsible for overloading the operator "<". It makes it such that you can perform the less-than operation on every instance (object) of your class. 

- __le__() method: This method is responsible for overloading the operator "<=". It makes it such that you can perform the less-than-or-equal-to operation on every instance (object) of your class. 

- __str__() method: This method is responsible for overloading the operator the output of the instance when printed. It makes it such that you can change the output of every instance (object) of your class when it is printed to the console.

- __repr__() method: This overrides the internal representation of objects in Python. It makes it such that you change the internal representation of every instance (object) of your class when it is printed to the console. It is helpful in debugging.
"""

# __str__() and __repr__() methods: 

# class Page:
#   def __init__(self, text, page_number):
#     self.text = text
#     self.page_number = page_number

#   def __len__(self):
#     return len(self.text)

#   def __str__(self):
#     return f"Page({self.text}, {self.page_number})"

#   def __repr__(self):
#     return self.__str__()


# class Book:
#   def __init__(self, title, author, pages, id_number):
#      self.title = title
#      self.author = author
#      self.pages = pages
#      self.id_number = id_number
    
#   def __len__(self):
#     return len(self.pages)
    
#   def __str__(self):
#     output = f"Book({self.title}, {self.author}, {self.id_number})"
#     for page in self.pages:
#       output += "\n" + str(page)
#     return output

#   def __repr__(self):
#     return f"Book({self.id_number})"


    
# page1 = Page("This is Tobiloba", 1)
# page2 = Page("This is Solutions", 2)
# book = Book("Tobiloba: The Mystery", "Tobiloba", [page1, page2], 1)

# print(page1, page2)
# print(book) # Book(Tobiloba: The Mystery, Tobiloba, 1)
              # Page(This is Tobiloba, 1)
              # Page(This is Solutions, 2)

# print(repr(page1))  # Page("This is Tobiloba", 1)
# print(repr(book))  # Book(1)



  
# Operator Overloading Examples:

# class Page:
#   def __init__(self, text, page_number):
#     self.text = text
#     self.page_number = page_number

#   def __len__(self):
#     return len(self.text)


# class Book:
#   def __init__(self, title, author, pages, id_number):
#      self.title = title
#      self.author = author
#      self.pages = pages
#      self.id_number = id_number
    
#   def __len__(self):
#     return len(self.pages)
    
    


# page1 = Page("This is Tobiloba", 1)
# page2 = Page("This is Solutions", 2)
# book = Book("Tobiloba: The Mystery", "Tobiloba", [page1, page2], 1)


# print(len(page1))  # 16
# print(len(page2))  # 17
# print(len(book))  # 2
    


# Equality comparison methods (__eq__(), __ne__(), __gt__(), __ge__(), __lt__(),__le__()):

# import math

# class Line:
#   def __init__(self, point1, point2):
#     self.point1 = point1
#     self.point2 = point2


#   def __truediv__(self, factor):
#     new_point1 = (self.point1[0] / factor, self.point1[1] / factor)
#     new_point2 = (self.point2[0] / factor, self.point2[1] / factor)
#     return Line(new_point1, new_point2)

  
#   def __floordiv__(self, factor):
#     new_point1 = (self.point1[0] // factor, self.point1[1] // factor)
#     new_point2 = (self.point2[0] // factor, self.point2[1] // factor)
#     return Line(new_point1, new_point2)  

#   # Returns the length of the line
#   def __len__(self):
#     distance_x = (self.point1[0] - self.point2[0]) ** 2
#     distance_y = (self.point1[1] - self.point2[1]) ** 2
    
#     distance = math.sqrt(distance_x + distance_y)
#     return round(distance)

#   def __eq__(self, other):
#     if not isinstance(other, Line):
#       return False
#     return self.point1 == other.point1 and self.point2 == other.point2  

#   def __ne__(self, other):
#     return not self.__eq__(other)

#   def __gt__(self, other):
#     return len(self) > len(other)

#   def __ge__(self, other):
#     return len(self) >= len(other)

#   def __lt__(self, other):
#     return len(self) < len(other)

#   def __le__(self, other):
#     return len(self) <= len(other)
    

# line1 = Line((20, 5), (30, 10))    
# line2 = Line((20, 5), (30, 10))   
# line3 = Line((20, 10), (30, 20))


# print(line1 == line2)  # True
# print(line1 != line3)  # True
# print(line1 > line3)  # False
# print(line3 >=  line1)  # True
# print(line1 < line3)  # True
# print(line3 <= line1)  # False





# __len__() method:
    
# import math

# class Line:
#   def __init__(self, point1, point2):
#     self.point1 = point1
#     self.point2 = point2


#   def __truediv__(self, factor):
#     new_point1 = (self.point1[0] / factor, self.point1[1] / factor)
#     new_point2 = (self.point2[0] / factor, self.point2[1] / factor)
#     return Line(new_point1, new_point2)

  
#   def __floordiv__(self, factor):
#     new_point1 = (self.point1[0] // factor, self.point1[1] // factor)
#     new_point2 = (self.point2[0] // factor, self.point2[1] // factor)
#     return Line(new_point1, new_point2)  

#   # Returns the length of the line
#   def __len__(self):
#     distance_x = (self.point1[0] - self.point2[0]) ** 2
#     distance_y = (self.point1[1] - self.point2[1]) ** 2
    
#     distance = math.sqrt(distance_x + distance_y)
#     return round(distance)



# line1 = Line((20, 5), (30, 10))    
# print(len(line1))

    
    

    
# __truediv__() and __floordiv__ methods:

# class Line:
#   def __init__(self, point1, point2):
#     self.point1 = point1
#     self.point2 = point2


#   def __truediv__(self, factor):
#     new_point1 = (self.point1[0] / factor, self.point1[1] / factor)
#     new_point2 = (self.point2[0] / factor, self.point2[1] / factor)
#     return Line(new_point1, new_point2)

  
#   def __floordiv__(self, factor):
#     new_point1 = (self.point1[0] // factor, self.point1[1] // factor)
#     new_point2 = (self.point2[0] // factor, self.point2[1] // factor)
#     return Line(new_point1, new_point2)  


# line1 = Line((20, 5), (30, 10))
# line2 = line1 / 2
# line3 = line1 // 2

# print(line2.point1, line2.point2)  # (10.0, 2.5) (15.0, 5.0)
# print(line3.point1, line3.point2)  # (10, 2) (15, 5)


    

  


# __mul__() method:

# class StoreItem:
#   TAX = 0.13
  
#   def __init__(self, name, price):
#     self.name = name
#     self.price = price
#     self.after_tax_price = 0
#     self.set_after_tax_price()
    

#   def set_after_tax_price(self):
#     self.after_tax_price = round(self.price * (1 + self.TAX), 2)

#   # Apply the discount to the item and return a new store item
#   def __sub__(self,  discount):
#     return StoreItem(self.name, self.price - discount)


#   def __mul__(self, value):
#     return StoreItem(self.name, self.price * value)




# bread = StoreItem("Bread", 21)
# discounted_bread = bread * 0.8  # 20% off
# print(discounted_bread.after_tax_price)  # 18.98





# __sub__() method: 

# class StoreItem:
#   TAX = 0.13
  
#   def __init__(self, name, price):
#     self.name = name
#     self.price = price
#     self.after_tax_price = 0
#     self.set_after_tax_price()
    

#   def set_after_tax_price(self):
#     self.after_tax_price = round(self.price * (1 + self.TAX), 2)

#   # Apply the discount to the item and return a new store item
#   def __sub__(self,  discount):
#     return StoreItem(self.name, self.price - discount)



# bread = StoreItem("Bread", 21)
# print(bread.after_tax_price)  # 23.73

# discounted_bread = bread - 2
# print(discounted_bread.after_tax_price)  # 21.47






    
# __add__() method:

# class Page:
#   def __init__(self, words, page_number):
#     self.words = words
#     self.page_number = page_number


#   # adds the words from both pages and returns a new Page with the new string and nextpage
#   def __add__(self, other):
#     new_words = self.words + " " + other.words
#     new_page = max(self.page_number, other.page_number) + 1
    
#     return Page(new_words, new_page)


# page1 = Page("This is for Tobiloba", 1)
# page2 = Page("This is for Solutions", 2)

# page3 = page1 + page2

# print(page3.words, page3.page_number)  # "This for Tobiloba This is for Solutions" 3


