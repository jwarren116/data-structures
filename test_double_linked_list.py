from double_linked_list import DoubleLinked
import pytest


def test_insert_one():
    linked = DoubleLinked()
    linked.insert("Bob")
    assert linked.first_item.val == "Bob"


def test_insert_multi():
    linked = DoubleLinked()
    linked.insert("Fred")
    linked.insert("Bob")
    linked.insert("Joe")
    assert linked.first_item.val == "Joe"


def test_append_one():
    linked = DoubleLinked()
    linked.append("Bob")
    assert linked.last_item.val == "Bob"


def test_append_multi():
    linked = DoubleLinked()
    linked.append("Fred")
    linked.append("Bob")
    linked.append("Joe")
    assert linked.last_item.val == "Joe"


def test_pop_one():
    linked = DoubleLinked()
    linked.insert("Bob")
    assert linked.pop() == "Bob"


def test_pop_empty():
    linked = DoubleLinked()
    with pytest.raises(ValueError):
        linked.pop()


def test_shift_one():
    linked = DoubleLinked()
    linked.insert("Bob")
    assert linked.shift() == "Bob"


def test_shift_empty():
    linked = DoubleLinked()
    with pytest.raises(ValueError):
        linked.shift()
