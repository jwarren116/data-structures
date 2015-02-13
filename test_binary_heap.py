from bin_heap import BinaryHeap
import pytest


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


# def test_with_range():
#     bh = BinaryHeap()
#     bh.push(range_func)
#     assert all_items(5) == range(0, 5)


def test_0():
    bin_list = BinaryHeap()
    assert bin_list.heaplist == [0]


def test_1():
    bin_list = BinaryHeap()
    bin_list.push(10)
    bin_list.push(9)
    bin_list.push(4)
    bin_list.push(72)
    assert len(bin_list.heaplist) == 5


def test_2():
    bin_list = BinaryHeap()
    bin_list.push(10)
    bin_list.push(9)
    bin_list.push(5)
    bin_list.push(7)
    bin_list.pop()
    bin_list.pop()
    assert bin_list.pop() == 9


def test_3():
    bin_list = BinaryHeap()
    bin_list.push(10)
    assert bin_list.pop() == 10


def test_4():
    bin_list = BinaryHeap()
    bin_list.push(10)
    bin_list.push(9)
    bin_list.push(5)
    bin_list.push(17)
    bin_list.push(28)
    bin_list.push(6)
    assert bin_list.pop() == 5


def test_5():
    bin_list = BinaryHeap()
    with pytest.raises(IndexError):
        bin_list.pop()


# def test_6():
#     bin_list = BinaryHeap()
#     assert [bin_list.pop() for i in range(3)] == [1, 2, 3, 4]
