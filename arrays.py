# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 14:06:00 2021

@author: richa
"""
new_list = [1,2,3]

result = new_list[0] 


# Accessing and reading values in array
if 1 in new_list: print(True)

for n in new_list:
    if n == 1:
        print(True)
        break
    
    
#inserting values to array

# true insert - has linear runtime - shifts all values resulting in linear runtime
new_list[2] = 'a'

print(new_list)

# appending -  constant time

