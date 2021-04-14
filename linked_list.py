# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 14:42:02 2021

@author: richa
"""
class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list.
    """
    
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
        
    
    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList:
    """
    Singly list list
    """
    # only node that this list has reference to is head
    
    def __init__ (self):
        self.head = None
        
        
    def is_empty(self):
        return self.head == None
        
    def size(self):
        """
        Returns the number of nodes in the list.
        Takes O(n) time. Linear time.
        """

        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        
        return count
    
    def add(self, data):
        """
        Adds a new Node at the head of the list.
        This is a O(1) operation. Constant time.
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    
    def search(self, key):
        """
        Search for the first node containing data that matches the key.
        Return the Node or None if not found.
        
        Takes O(n) time. Linear time.
        """
        current = self.head
        
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
     
        
    def insert(self, data, index):
        """
        Inserts a new Node containing data at the index position.
        Insertion takes O(1) Constant time, but finding the node
        at the insertion point take O(n) Linear time.
        
        Overall takes O(n) Linear time.
        """         
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data) 
            
            position = index
            current = self.head
            
            while position > 1:
                current = node.next_node
                position -= 1
            
            prev_node = current
            next_node = current.next_node
            
            prev_node.next_node = new
            new.next_node = next_node
    
    def remove(self, key):
        """ 
        Removes node containiong data that matches the key.
        Returns the node or None if key doesnt exist.
        Takes O(n).
        """
        
        current = self.head
        previous = None
        found = False
        
        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.
        
        return current
            
    def __repr__(self):
        """
        Returns a string representation of the list.
        Takes O(n) time.
        """
        
        nodes = []
        current = self.head
        
        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            
            current = current.next_node
        return '-> '.join(nodes)
                
            