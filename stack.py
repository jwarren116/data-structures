class StackItem(object):
    def __init__(self, data, next_item=None):
        self.data = data
        self.next_item = next_item

    def __str__(self):
        return self.data


class StackFrame(object):
    def __init__(self, first_item=None):
        self.first_item = first_item

    def push(self, new_item):
        # push new_item to beginning of list
        if not self.first_item:
            self.first_item = new_item
        else:
            new_item.next_item = self.first_item
            self.first_item = new_item

    def pop(self):
        # poops first value from list and returns it
        obsolete_item = self.first_item
        self.first_item = self.first_item.next_item
        return obsolete_item.data
