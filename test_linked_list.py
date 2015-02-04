from linked_list import Node
from linked_list import LinkedList


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
