#!/usr/bin/env python


class QueueItem(object):
    def __init__(self, data, prev_item=None, next_item=None):
        self.data = data
        self.next_item = next_item
        self.prev_item = prev_item

    def __str__(self):
        return str(self.data)


class Queue(object):
    def __init__(self, first_item=None, last_item=None):
        self.first_item = first_item
        self.last_item = last_item

    def enqueue(self, val):
        # adds val to beginning of queue
        new_item = QueueItem(val)
        if not self.first_item:
            self.first_item = self.last_item = new_item
        else:
            new_item.next_item = self.first_item
            self.first_item.prev_item = new_item
            self.first_item = new_item

    def dequeue(self):
        # pops last value from list and returns it
        obsolete_item = self.last_item
        if self.last_item is None:
            raise ValueError("No items in queue!")
        elif self.first_item is obsolete_item:
            self.last_item = self.first_item = None
        else:
            obsolete_item.prev_item.next_item = None
            self.last_item = self.last_item.prev_item
        return obsolete_item.data

    def size(self):
        # returns size of the queue, returns 0 if empty
        size = 0
        current_item = self.first_item
        while current_item is not None:
            size += 1
            current_item = current_item.next_item
        return size
