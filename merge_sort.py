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