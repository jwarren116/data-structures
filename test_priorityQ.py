import _priorityQ as pq
# import sys
import pytest


class StackTest():

    def test_init(self):
        queue = pq.Priority()
        assert type(queue) == pq.Priority

    def test_insert(self):
        self.assertEqual(self.append.data)

    def test_pop(self):
        self.asserEqual(self.pop.data)
        self.assertEqual(self.length == 0)

    def test_peek(self):
        self.asserEqual(self.append.data)
        self.assertEqual(self.peek == 0)
