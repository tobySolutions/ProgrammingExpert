"""
Notes:

- A generator is a special kind of "iterator" that uses the "yield" keyword to return the "next" value in the sequence.

- A "Generator" can achieve almost the exact same things as an "iterator".

- When you call a function that contains the "yield" keyword, it gives you a "generator object".

- Normal iterators created from the __iter__() are called legacy iterators

- A lot of times, you use a "Generator" when you want to generate an infinite sequence or a close-to-infinite sequence.

- You use a "Generator" when you do not care about the entire sequence, you just want to use one value at a time and you'll use a "list" when you want to access all the values.
"""

# Advanced Generator Example:

# ================================

# def fib(n):
#   last = 1
#   second_last = 1
#   current = 3

#   while current <= n:
#     number = last + second_last
#     yield number

#     second_last = last
#     last = number
#     current += 1

    
# for val in fib(10):
#   print(val);

# =================================

## Very inefficient approach

# def fib(n):
#   pass


# fib_numbers = [1, 1]

# for i in range(2, 100):
#   last = fib_numbers[i - 1];
#   second_last = fib_numbers[i - 2];
#   number = last + second_last;
#   fib_numbers.append(number)

# print(fib_numbers)

# =================================






# Using Generators:

# ===============================

# def gen():
#   yield 1;
#   yield 2;
#   yield 3;


# iterator = gen();

# for i in iterator:
#   print(i)
  

# ===============================

# def gen():
#   yield 1;
#   yield 2;
#   yield 3;


# iterator = gen();

# print(next(iterator))  # 1
# print(next(iterator))  # 2
# print(next(iterator))  # 3
# print(next(iterator))  # auto-exception (StopIteration)

# ==============================





# Creating a Generator:

# def gen():
#    yield 1;
#    yield 2;
#    yield 3;


# print(type(gen))  # <class 'function'>
# print(type(gen()))  # <class 'generator'>
# print(gen())  # <generator object gen at 0x7f986ab77e40>