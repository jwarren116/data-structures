from queue import QueueItem
from queue import Queue
import pytest


def test_enqueue():
    queue = Queue()
    queue.enqueue("Bacon")
    assert queue.size() == 1


def test_enqueue_multi():
    queue = Queue()
    queue.enqueue("Bacon")
    queue.enqueue("Steak")
    queue.enqueue("Beer")
    assert queue.size() == 3


def test_dequeue():
    queue = Queue()
    queue.enqueue("Bacon")
    assert queue.dequeue() == "Bacon"
    assert queue.size() == 0


def test_dequeue_multi():
    queue = Queue()
    queue.enqueue("Bacon")
    queue.enqueue("Beer")
    assert queue.dequeue() == "Bacon"
    assert queue.last_item.data == "Beer"


def test_size():
    pass
