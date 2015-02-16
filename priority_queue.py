#!/usr/bin/env python


class QueueItem(object):
    def __init__(self, val, priority=None, prev_item=None, next_item=None):
        self.val = val
        self.next_item = next_item
        self.prev_item = prev_item
        self.priority = priority

    def __str__(self):
        return str(self.val)


class Queue(object):
    def __init__(self, first_item=None, last_item=None):
        self.first_item = first_item
        self.last_item = last_item

    def insert(self, val, priority):
        """adds new item to end of queue"""
        # adds val to last item of queue
        new_item = QueueItem(val, priority, prev_item=self.last_item)
        if not self.first_item:
            self.first_item = self.last_item = new_item
        else:
            self.last_item.next_item = new_item
            self.last_item = new_item

    def pop(self):
        """finds first highest priority item in queue, removes item and returns value"""
        if self.first_item is None:
            raise ValueError("No items in queue!")
        # if only one item in queue, reassign first and last items to none
        priority_item = self.first_item
        if self.first_item == self.last_item:
            self.first_item = self.last_item = None
            return priority_item.val
        # iterate through list to find highest priority item
        current_item = self.first_item.next_item
        while current_item is not None:
            if priority_item.priority > current_item.priority:
                priority_item = current_item
                current_item = current_item.next_item
            else:
                current_item = current_item.next_item
        # reassign neighbors of item with highest priority being popped
        if priority_item == self.first_item:
            priority_item.next_item.prev_item = None
            self.first_item = priority_item.next_item
        elif priority_item == self.last_item:
            priority_item.prev_item.next_item = None
            self.last_item = priority_item.prev_item
        else:
            priority_item.prev_item.next_item = priority_item.next_item
            priority_item.next_item.prev_item = priority_item.prev_item
        return priority_item.val

    def size(self):
        """returns size of the queue"""
        size = 0
        current_item = self.first_item
        while current_item is not None:
            size += 1
            current_item = current_item.next_item
        return size

    def peek(self):
        """returns highest first highest priority item in queue"""
        if self.first_item is None:
            raise ValueError("No items in queue!")
        if self.first_item == self.last_item:
            return self.first_item.val
        # iterate through list to find highest priority item
        priority_item = self.first_item
        current_item = self.first_item.next_item
        while current_item is not None:
            if priority_item.priority > current_item.priority:
                priority_item = current_item
                current_item = current_item.next_item
            else:
                current_item = current_item.next_item
        return priority_item.val
