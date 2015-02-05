from stack import StackItem
from stack import StackFrame
import pytest


def test_item_data():
    # Tests that "Bacon" is returned when calling .data on item
    bacon = StackItem("Bacon")
    assert bacon.data == "Bacon"


def test_stack_push():
    # Tests that "Bacon" is first item when pushed to stack
    bacon = StackItem("Bacon")
    new_stack = StackFrame()
    new_stack.push(bacon)
    assert new_stack.first_item.data == "Bacon"


def test_stack_pop():
    # Tests that "Bacon" is returned when it is popped from stack
    bacon = StackItem("Bacon")
    new_stack = StackFrame()
    new_stack.push(bacon)
    assert new_stack.pop() == "Bacon"


def test_empty_stack_pop():
    # Tests that pop() on empty stack returns ValueError
    new_stack = StackFrame()
    with pytest.raises(ValueError):
        new_stack.pop()
