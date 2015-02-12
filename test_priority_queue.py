from priority_queue import Queue
import pytest


def test_enqueue_first_item():
    queue = Queue()
    queue.insert("Bacon", 1)
    assert queue.last_item.val == "Bacon"


def test_enqueue_multi_last_item():
    queue = Queue()
    queue.insert("Bacon", 1)
    queue.insert("Steak", 2)
    queue.insert("Beer", 1)
    assert queue.last_item.val == "Beer"


def test_insert_with_spaces():
    queue = Queue()
    queue.insert("Breakfast Foods", 32)
    queue.insert("Water Bottles", 3)
    queue.insert("Non awkward backrubs", 1)
    assert queue.size() == 3


def test_dequeue_empty():
    queue = Queue()
    with pytest.raises(ValueError):
        queue.pop()


def test_dequeue():
    queue = Queue()
    queue.insert("Bacon", 1)
    assert queue.pop() == "Bacon"
    assert queue.size() == 0


def test_dequeue_multi():
    queue = Queue()
    queue.insert("Bacon", 1)
    queue.insert("Beer", 5)
    assert queue.pop() == "Bacon"
    assert queue.first_item.val == "Beer"
    assert queue.size() == 1


def test_size():
    queue = Queue()
    queue.insert("Bacon", 65)
    queue.insert("Beer", 2)
    assert queue.size() == 2


def test_size_with_remove():
    queue = Queue()
    queue.insert("Bacon", 1)
    queue.insert("Beer", 7)
    queue.insert("Cow", 5)
    queue.insert("Whiskey", 2)
    queue.pop()
    assert queue.size() == 3


def test_pop_multi():
    queue = Queue()
    queue.insert("Pickles", 3)
    queue.insert("Apples", 10)
    queue.insert("lemons", 14)
    queue.insert("human", 1)
    queue.insert("pineapple", 7)
    assert queue.pop() == "human"
    assert queue.pop() == "Pickles"
    assert queue.pop() == "pineapple"
    assert queue.size() == 2


def test_peek():
    queue = Queue()
    queue.insert("Bacon", 25)
    queue.insert("Eggs", 63)
    queue.insert("Fajitas", 67)
    queue.insert("Chicken", 5)
    assert queue.peek() == "Chicken"
