import bin_heap as bh


class Priority(object):
    """docstring for priority"""
    def __init__(self):
        self.bin_heap = bh()

    def insert(self, item, rank):
        bh.push(item, rank)

    def pop(self):
        item = self.bin_heap.pop()
        return item

    def peek(self, item):
        return item
