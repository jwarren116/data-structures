from queue import Queue
import pytest


def test_enqueue_first_item():
    queue = Queue()
    queue.enqueue("Bacon")
    assert queue.last_item.data == "Bacon"


def test_enqueue_multi_last_item():
    queue = Queue()
    queue.enqueue("Bacon")
    queue.enqueue("Steak")
    queue.enqueue("Beer")
    assert queue.last_item.data == "Beer"


def test_dequeue_empty():
    queue = Queue()
    with pytest.raises(ValueError):
        queue.dequeue()


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
    assert queue.first_item.data == "Beer"
    assert queue.size() == 1


def test_size():
    queue = Queue()
    queue.enqueue("Bacon")
    queue.enqueue("Beer")
    assert queue.size() == 2


def test_size_with_remove():
    queue = Queue()
    queue.enqueue("Bacon")
    queue.enqueue("Beer")
    queue.enqueue("Cow")
    queue.enqueue("Whiskey")
    queue.dequeue()
    assert queue.size() == 3
