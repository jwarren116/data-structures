from bin_heap import BinaryHeap
import pytest
import random


def test_is_empty():
    bin_list = BinaryHeap()
    assert bin_list.heaplist == [0]


def test_one_push_pop():
    bin_list = BinaryHeap()
    bin_list.push(10)
    assert bin_list.pop() == 10


def all_items(heap):
    items = []
    while True:
        try:
            items.append(heap.pop())
        except IndexError:
            return items
    return items


def test_reverse_range():
    heap = BinaryHeap()
    for i in range(5, 0, -1):
        heap.push(i)
    assert all_items(heap) == range(1, 6)


def test_load_up_the_list():
    heap = BinaryHeap()
    for i in range(10000, 0, -1):
        heap.push(i)
    assert all_items(heap) == range(1, 10001)


def test_random_input():
    h = BinaryHeap()
    for i in random.sample(range(100), 100):
        h.push(i)
    assert all_items(h) == range(0, 100)


def test_really_really_big_random_input():
    h = BinaryHeap()
    for i in random.sample(range(1000000), 1000000):
        h.push(i)
    assert all_items(h) == range(0, 1000000)
