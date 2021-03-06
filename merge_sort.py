# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 19:53:58 2021

@author: richa
"""

def merge_sort(lst):
    """
    Sorts a list in ascending order.
    Returns a new sorted list.
    
    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    """
    # stopping condition
    if len(lst) <= 1:
        return lst
    
    # divide using a helper function split()
    left_half, right_half = split(lst)
    
    # conquer step
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    # combine step
    return merge(left, right)


def split(lst):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right.
    """
    
    mid_index = len(lst)//2
    
    left_lst = lst[:mid_index]
    right_lst = lst[mid_index:]
    
    return left_lst, right_lst


def merge(left, right):
    """
    This function merges two lists (arrays) , sorting them in the process.
    Return a new merged list.
    """
    # merged list
    l = []
    # index in left list
    i = 0
    # index in right list
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1            
            
    
    while i < len(left):
        l.append(left[i])
        i += 1
        
    while j < len(right):
        l.append(right[j])
        j += 1

    return l
            

def verify_sorted(lst):
    n = len(lst)
    if n == 0 or n == 1:
        return True
    
    return lst[0] < lst[1] and verify_sorted(lst[1:])


my_list = [54, 78, 97, 5, 16, 43, 9, 12, 4]

l = merge_sort(my_list)

print(l)
print(verify_sorted(my_list))      
print(verify_sorted(l))      

            
            