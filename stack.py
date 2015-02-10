class StackItem(object):
    def __init__(self, data, next_item=None):
        self.data = data
        self.next_item = next_item

    def __str__(self):
        return str(self.data)


class Stack(object):
    def __init__(self, first_item=None):
        self.first_item = first_item

    def push(self, val):
        # push val to beginning of list
        self.new_item = StackItem(val)
        if not self.first_item:
            self.first_item = self.new_item
        else:
            self.new_item.next_item = self.first_item
            self.first_item = self.new_item

    def pop(self):
        # poops first value from list and returns it
        if self.first_item is None:
            raise ValueError("No items in stack!")
        else:
            obsolete_item = self.first_item
            self.first_item = self.first_item.next_item
            return obsolete_item.data
