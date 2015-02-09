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
        self.new_item = QueueItem(val)
        if not self.first_item:
            self.first_item = self.new_item
            self.last_item = self.new_item
        else:
            self.new_item.next_item = self.first_item
            self.first_item.prev_item = self.new_item
            self.first_item = self.new_item

    def dequeue(self):
        # poops last value from list and returns it
        if self.last_item is None:
            raise ValueError("No items in queue!")
        else:
            obsolete_item = self.last_item
            obsolete_item.prev_item.next_item = None
            self.last_item = self.last_item.prev_item
            return obsolete_item.data
