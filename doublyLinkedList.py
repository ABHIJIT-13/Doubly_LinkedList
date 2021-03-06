
#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    temp = head
    node = DoublyLinkedListNode(data)
    nex = DoublyLinkedListNode(None)
    while temp != None:
    	nex = temp.next
    	if node.data <= head.data :
    		node.next = head
    		node.prev = None
    		head.prev = node
    		head = node
    		return head
    	if nex == None :
    		node.pev = temp
    		node.next = None
    		temp.next = node
    		return head	
    	if node.data > temp.data and node.data <= nex.data :
    		node.prev = temp
    		nex.prev = node
    		node.next = nex
    		temp.next = node
    		return head
    	temp = temp.next	




if __name__ == '__main__':
    

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ')
        print('\n')

    
            