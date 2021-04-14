# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 16:41:15 2021.

@author: richa
"""

def linear_search(lst: list, target: int):

    for index, item in enumerate(lst):
        if lst[index] == target:
            return index

    return None

def verify(index):
    if index is not None:
        print('Target found at index: ', index)
    else:
        print('Target not found in list')
    
    
numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 6)
verify(result)
        