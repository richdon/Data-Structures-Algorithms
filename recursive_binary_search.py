# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 23:42:20 2021

@author: richa
"""

def recursive_binary_search(lst, target):
    if len(lst) == 0:
        return False
    else:
        midpoint = (len(lst)) // 2
        
        if lst[midpoint] == target:
            return True
        else:
             if lst[midpoint] < target:
               return recursive_binary_search(lst[midpoint+1:], target)
             else:
                 return recursive_binary_search(lst[:midpoint], target)
    

def verify(result):
    print('Target found:', result)
    
numbers = [1,2,3,4,5,6,7,8,9,10]    
result = recursive_binary_search(numbers, 6)
verify(result)

result = recursive_binary_search(numbers, 12)
verify(result)