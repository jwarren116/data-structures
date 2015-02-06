#!/usr/bin/env python
from __future__ import unicode_literals


class Node(object):
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)


class LinkedList(object):
    def __init__(self, firstNode=None):
        self.firstNode = firstNode

    def insert(self, val):
        # insert val at beginning of list
        self.newNode = Node(val)
        if not self.firstNode:
            self.firstNode = self.newNode
        else:
            self.newNode.nextNode = self.firstNode
            self.firstNode = self.newNode

    def pop(self):
        # pops first value from list and returns it
        if self.size() == 0:
            raise ValueError("The list is empty")
        else:
            obsoleteNode = self.firstNode
            self.firstNode = self.firstNode.nextNode
            return obsoleteNode.data.encode('utf-8')

    def size(self):
        # returns length of list
        currentNode = self.firstNode
        size = 0
        while currentNode is not None:
            size += 1
            currentNode = currentNode.nextNode
        return size

    def search(self, val):
        # return node containing 'val' in list, if present (else None)
        currentNode = self.firstNode
        if currentNode.data is None:
            raise ValueError()
        while currentNode.data != val:
            if currentNode.nextNode is None:
                return None
            else:
                currentNode = currentNode.nextNode
        return currentNode

    def remove(self, node):
        # remove node from list, wherever it might be
        if self.size() == 0:
            raise ValueError("The list is empty")
        else:
            prevNode = None
            currentNode = self.firstNode
            while currentNode is not node:
                if currentNode is None:
                    raise ValueError()
                else:
                    prevNode = currentNode
                    currentNode = currentNode.nextNode
            if prevNode is None:
                self.firstNode = currentNode.nextNode
            else:
                prevNode.nextNode = currentNode.nextNode

    def display(self):
        # print list as python tuple literal
        # (bonus points if you make it appear like "(12, 'sam', 32, 'fred')")
        display = "("
        currentNode = self.firstNode
        while currentNode is not None:
            display += currentNode.data.encode('utf-8') + ", "
            currentNode = currentNode.nextNode
        return display + ")"
