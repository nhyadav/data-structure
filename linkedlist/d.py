#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if self.head:
            self.tail.next = node
        else:
            self.head = node
        # if not self.head:
        #     self.head = node
        # else:
        #     self.tail.next = node


        self.tail = node
    def printLinkedList(self):
        if self.head:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next
        else:
            return None

if __name__ == '__main__':
    llist_count = int(input('count:'))

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input("data:"))
        llist.insert_node(llist_item)
    llist.printLinkedList()
    # printLinkedList(llist.head)
