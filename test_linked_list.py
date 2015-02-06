from linked_list import Node
from linked_list import LinkedList
import pytest


def test_node_add():
    newList = LinkedList()
    newList.insert("Bob")
    assert newList.firstNode.data == "Bob"


def test_next_node_none():
    newList = LinkedList()
    newList.insert("Bob")
    assert newList.firstNode.nextNode is None


def test_add_second_node():
    newList = LinkedList()
    newList.insert("Bob")
    newList.insert("Joe")
    assert newList.firstNode.nextNode.data == "Bob"


def test_pop():
    newList = LinkedList()
    newList.insert("Bob")
    newList.insert("Joe")
    assert newList.pop() == "Joe"


def test_pop_size():
    newList = LinkedList()
    newList.insert("Bob")
    newList.insert("Joe")
    newList.pop()
    assert newList.size() == 1


def test_size():
    newList = LinkedList()
    newList.insert("Bob")
    newList.insert("Joe")
    assert newList.size() == 2


def test_search_fail():
    newList = LinkedList()
    newList.insert("Bob")
    newList.insert("Joe")
    assert newList.search("Fred") is None


def test_search_success():
    newList = LinkedList()
    newList.insert("Bob")
    newList.insert("Joe")
    assert newList.search("Bob") is not None


def test_remove():
    newList = LinkedList()
    newList.insert("Bob")
    newList.insert("Joe")
    newList.remove(newList.search("Bob"))
    assert newList.search("Bob") is None


def test_remove_empty():
    newList = LinkedList()
    with pytest.raises(ValueError):
        newList.remove("Bob")


def test_pop_empty():
    newList = LinkedList()
    with pytest.raises(ValueError):
        newList.pop()


def test_remove_fail():
    newList = LinkedList()
    newList.insert("Bob")
    newList.insert("Joe")
    with pytest.raises(ValueError):
        newList.remove("Fred")
