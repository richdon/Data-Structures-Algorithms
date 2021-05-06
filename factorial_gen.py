# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Thu May  6 00:31:29 2021
# 
# @author: richa
# """
# # Definition of the generator to produce even numbers.
# def all_even():
#     n = 0
#     while True:
#         yield n
#         n += 2
# 
# my_gen = all_even()
# 
# # Generate the first 5 even numbers.
# for i in range(5):
#     print(next(my_gen))
# 
# # Now go and do some other processing.
# do_something = 4
# do_something += 3
# print('doing something',do_something)
# 
# # Now go back to generating more even numbers.
# for i in range(100):
#     print(next(my_gen))
# =============================================================================


def prod(a,b):
    # TODO change output to the product of a and b
    output = a * b
    return output

def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        # TODO: update i and n
        n = output
        i += 1 
        # Hint: i is a successive integer and n is the previous product


# Test block
my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120


