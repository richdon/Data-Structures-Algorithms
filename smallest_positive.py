# -*- coding: utf-8 -*-
"""
Created on Wed May  5 22:06:06 2021

@author: richa
"""
def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    pos = []
    for n in in_list:
        if n > 0:
            pos.append(n)
    
    if pos:
        sp = pos[0]
        for n in pos:
            if n < sp:
                sp = n
    else:
        sp = None
            
    return sp
# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

print(smallest_positive([-6, -9, -7]))
# Correct output: None

print(smallest_positive([]))
# Correct output: None