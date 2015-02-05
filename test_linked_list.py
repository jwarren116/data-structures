from linked_list import Node
from linked_list import LinkedList
import pytest


def test_node_data():
    newNode = Node("Bob")
    assert newNode.data == "Bob"


def test_node_add():
    bob = Node("Bob")
    newList = LinkedList()
    newList.insert(bob)
    assert newList.firstNode.data == "Bob"


def test_next_node_none():
    bob = Node("Bob")
    newList = LinkedList()
    newList.insert(bob)
    assert newList.firstNode.nextNode is None


def test_add_second_node():
    joe = Node("Joe")
    bob = Node("Bob")
    newList = LinkedList()
    newList.insert(bob)
    newList.insert(joe)
    assert newList.firstNode.nextNode.data == "Bob"


def test_pop():
    joe = Node("Joe")
    bob = Node("Bob")
    newList = LinkedList()
    newList.insert(bob)
    newList.insert(joe)
    assert newList.pop() == "Joe"


def test_pop_size():
    joe = Node("Joe")
    bob = Node("Bob")
    newList = LinkedList()
    newList.insert(bob)
    newList.insert(joe)
    newList.pop()
    assert newList.size() == 1


def test_size():
    joe = Node("Joe")
    bob = Node("Bob")
    newList = LinkedList()
    newList.insert(bob)
    newList.insert(joe)
    assert newList.size() == 2


def test_search_fail():
    joe = Node("Joe")
    bob = Node("Bob")
    newList = LinkedList()
    newList.insert(bob)
    newList.insert(joe)
    assert newList.search("Fred") is None


def test_search_success():
    joe = Node("Joe")
    bob = Node("Bob")
    newList = LinkedList()
    newList.insert(bob)
    newList.insert(joe)
    assert newList.search("Bob") == bob


def test_remove():
    joe = Node("Joe")
    bob = Node("Bob")
    newList = LinkedList()
    newList.insert(bob)
    newList.insert(joe)
    newList.remove(bob)
    assert newList.search("Bob") is None


def test_remove_empty():
    newList = LinkedList()
    assert newList.remove("Bob") == "THE LIST! IT'S EMPTY!!"


def test_pop_empty():
    newList = LinkedList()
    assert newList.pop() == "THE LIST! IT'S EMPTY!!"


def test_remove_fail():
    joe = Node("Joe")
    bob = Node("Bob")
    newList = LinkedList()
    newList.insert(bob)
    newList.insert(joe)
    with pytest.raises(ValueError):
        newList.remove("Fred")
