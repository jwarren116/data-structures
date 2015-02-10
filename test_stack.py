from stack import Stack
import pytest


def test_stack_push():
    # Tests that "Bacon" is first item when pushed to stack
    new_stack = Stack()
    new_stack.push("bacon")
    assert new_stack.first_item.data == "bacon"


def test_stack_push_multi():
    # Tests that we can push multiple items to stack
    # then get expected results from pop
    new_stack = Stack()
    new_stack.push("bacon")
    new_stack.push("steak")
    new_stack.push("grilled cheese")
    new_stack.pop()
    new_stack.pop()
    assert new_stack.pop() == "bacon"


def test_empty_stack_pop():
    # Tests that pop() on empty stack returns ValueError
    new_stack = Stack()
    with pytest.raises(ValueError):
        new_stack.pop()
