from linked_list import Node
from linked_list import LinkedList


def test_node_data():
    newNode = Node("Bob")
    assert newNode.data == "Bob"


def test_node_add():
    newNode = Node("Bob")
    newList = LinkedList()
    newList.insert(newNode)
    assert newList.firstNode.data == "Bob"
