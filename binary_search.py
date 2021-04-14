# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 19:31:22 2021

@author: richa
"""

def binary_search(lst, target):
    first = 0
    
    # constant time operation
    last = len(lst) - 1
    
    # keep executing until value of first is <= value of last
    while first <= last:
        midpoint = (first + last) // 2
        
        # constant time operations
        if lst[midpoint] == target:
            return midpoint
        elif lst[midpoint] < target:
            first = midpoint + 1
        elif lst[midpoint] > target:
            last = midpoint - 1
    
    return None

def verify(index):
    if index is not None:
        print('Target found at index: ', index)
    else:
        print('Target not found in list')
    
    
numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 6)
verify(result)