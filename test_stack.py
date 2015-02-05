from stack import StackItem
from stack import StackFrame
import pytest


def test_item_data():
    # Tests that "Bacon" is returned when calling .data on item
    bacon = StackItem("Bacon")
    assert bacon.data == "Bacon"


def test_create_stack_frame():
    # Tests that an empty stack can be created
    new_stack = StackFrame()
    assert new_stack


def test_stack_push():
    # Tests that "Bacon" is first item when pushed to stack
    bacon = StackItem("Bacon")
    new_stack = StackFrame()
    new_stack.push(bacon)
    assert new_stack.first_item.data == "Bacon"


def test_stack_push_multi():
    # Tests that we can push multiple items to stack, then get expected results from pop
    bacon = StackItem("Bacon")
    steak = StackItem("Steak")
    grilled_cheese = StackItem("Grilled Cheese")
    new_stack = StackFrame()
    new_stack.push(bacon)
    new_stack.push(steak)
    new_stack.push(grilled_cheese)
    new_stack.pop()
    new_stack.pop()
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
