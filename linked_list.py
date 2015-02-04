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
        pass

    def size(self):
        # returns length of list
        pass

    def search(self, val):
        # return node containing 'val' in list, if present (else None)
        pass

    def remove(self, node):
        # remove node from list, wherever it might be
        pass

    def display(self):
        # print list as python tuple literal
        # (bonus points if you make it appear like "(12, 'sam', 32, 'fred')")
        for node in self:
            print self.firstNode
