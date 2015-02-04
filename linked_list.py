#!/usr/bin/env python


class Node(object):
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode


class LinkedList(object):
    def __init__(self, firstNode=None):
        self.firstNode = firstNode

    def insert(self, newNode):
        # insert newNode at beginning of list
        if not self.firstNode:
            self.firstNode = newNode
        else:
            newNode.nextNode = self.firstNode
            self.firstNode = newNode

    def pop(self):
        # pops first value from list and returns it
        obsoleteNode = self.firstNode
        self.firstNode = self.firstNode.nextNode
        return obsoleteNode

    def size(self):
        # returns length of list
        currentNode = self.firstNode
        size = 0
        while currentNode is not None:
            size += 1
            currentNode = self.nextNode
        return size

    def search(self, val):
        # return node containing 'val' in list, if present (else None)
        pass

    def remove(self, node):
        # remove node from list, wherever it might be
        if size == 0:
            return "List is empty"
        else: 
            pass


    def display(self):
        # print list as python tuple literal
        # (bonus points if you make it appear like "(12, 'sam', 32, 'fred')")
        for node in self:
            print self.firstNode
