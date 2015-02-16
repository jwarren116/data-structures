import _priorityQ as pq
import sys
import pytest


class StackTest():

    def test_init(self):
        queue = pq.Priority()
        assert type(queue) == pq.Priority

    def test_insert(self):
        self.assertEqual(self.append.item)

    def test_pop(self):
        self.asserEqual(self.pop.item)
        self.assertEqual(self.length == 0)

    def test_peek(self):
        self.asserEqual(self.append.item)
        self.assertEqual(self.peek == 0)
