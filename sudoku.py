# -*- coding: utf-8 -*-
"""
Created on Thu May  6 01:46:42 2021

@author: richa
"""

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               

def transpose(square):
    
    transposed = [] 
    for i, row in enumerate(square):
         transposed.append([square[n][i] for n in range(len(square))])
    
    return transposed
       
  
def check_valid_square(square):
    
    for val in square[0]:
        if not isinstance(val, int):
            return False
    return True
    

def check_soduku(square):
      
    if not check_valid_square(square):
        return False
           
    row_trigger = True
    row_count = 0

    length = [n+1 for n in range(len(square))]
    for row in square:
        for j in length:
            if j in row:
                row_count+=1
            else:
                row_trigger = False
          
    transposed = transpose(square)
    
    col_trigger = True
    col_count = 0    
    for row in transposed:
        for j in length:
            if j in row:
                col_count+=1
            else:
                col_trigger = False
    
    
    if row_trigger and col_trigger:
        return True
          
    else:
        return False
    
    

print(check_soduku(incorrect))
