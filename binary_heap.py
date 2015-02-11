#!/usr/bin/env python


class BinaryHeap(object):
    def __init__(self):
        self.heap_list = []

    def push(self, val):
        """puts a new value at the top of the heap,
        maintaining the heap property"""
        self.heap_list.append(val)
        child_position = len(self.heap_list) - 1
        if len(self.heap_list) == 1:
            return
        while True:
            parent_position = (child_position - 1) / 2
            parent = self.heap_list[parent_position]
            if val <= parent:
                break
            else:
                self.heap_list[parent_position] = val
                self.heap_list[child_position] = parent
                child_position = parent_position
                if child_position == 0:
                    break

    def pop(self):
        """removes the 'top' value in the heap,
        maintaining the heap property"""
        end = len(self.heap_list) - 1
        if end <= 0:
            self.heap_list.pop()
        pop_item = self.heap_list[0]
        return_item = self.heap_list.pop()
        position = 0
        while True:
            child_two_position = (position + 1) * 2
            child_one_position = child_two_position - 1


    def swap(self, child, parent):
        pass
