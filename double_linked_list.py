#!/usr/bin/env python


class ListItem(object):
    def __init__(self, val, prev_item=None, next_item=None):
        self.val = val
        self.next_item = next_item
        self.prev_item = prev_item

    def __str__(self):
        return str(self.data)


class DoubleLinked(object):
    def __init__(self, first_item=None, last_item=None):
        self.first_item = first_item
        self.last_item = last_item

    def insert(self, val):
        # adds val to beginning of list
        new_item = ListItem(val, next_item=self.first_item)
        if self.first_item is None:
            self.first_item = self.last_item = new_item
        else:
            self.first_item = self.first_item.prev_item = new_item

    def append(self, val):
        # adds val to end of list
        new_item = ListItem(val, prev_item=self.last_item)
        if not self.last_item:
            self.first_item = self.last_item = new_item
        else:
            self.last_item = self.last_item.next_item = new_item

    def pop(self):
        # pops first value from list and returns it
        obsolete_item = self.first_item
        if self.first_item is None:
            raise ValueError("No items in list!")
        elif self.last_item is obsolete_item:
            self.first_item = self.last_item = None
        else:
            obsolete_item.next_item.prev_item = None
            self.first_item = self.first_item.next_item
        return obsolete_item.val

    def shift(self):
        # pops last value from list and returns it
        obsolete_item = self.last_item
        if self.last_item is None:
            raise ValueError("No items in list!")
        elif self.first_item is obsolete_item:
            self.first_item = self.last_item = None
        else:
            obsolete_item.prev_item.next_item = None
            self.last_item = self.last_item.prev_item
        return obsolete_item.val

    def remove(self, value):
        # remove value from list, wherever it might be
        if self.first_item is None:
            raise ValueError("The list is empty")
        else:
            current_item = self.first_item
            while current_item.val != value:
                if current_item.next_item is None:
                    raise ValueError("Value not found in list")
                else:
                    current_item = current_item.next_item
            if current_item.prev_item is None:
                self.first_item = self.first_item.next_item
            else:
                current_item.prev_item.next_item = current_item.next_item
                current_item.next_item.prev_item = current_item.prev_item
