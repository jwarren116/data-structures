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
        # adds val to last item of queue
        new_item = QueueItem(val, self.priority, next_item=self.last_item)
        if not self.first_item:
            self.first_item = self.last_item = new_item
        else:
            self.last_item.prev_item = new_item
            self.last_item = new_item

    def pop(self):
        # pops first value of highest priority from the queue and returns it
        priority_item = self.first_item
        current_item = self.first_item
        if self.first_item is None:
            raise ValueError("No items in queue!")
        # elif self.last_item is obsolete_item:
        #     self.first_item = self.last_item = None

        while current_item is not None:
            if priority_item.priority > current_item.next_item.priority:
                priority_item = current_item.next_item
                current_item = current_item.next_item
            else:
                current_item = current_item.next_item

        #     obsolete_item.prev_item.next_item = None
        #     self.first_item = self.first_item.prev_item
        # return obsolete_item.val

    def size(self):
        # returns size of the queue, returns 0 if empty
        size = 0
        current_item = self.last_item
        while current_item is not None:
            size += 1
            current_item = current_item.next_item
        return size
