
from parenthetics import is_balanced
import pytest


def test_isone():
    assert is_balanced("(") == 1


def test_isneg():
    assert is_balanced(")") == -1


def test_iszero():
    assert is_balanced("( )") == 0


def test_withstring():
    assert is_balanced("this is a (string) with open and close") == 0


def test_mismatched():
    assert is_balanced("This is a string with )))))(((((( wrong order") == -1


def test_bug():
    assert is_balanced("()(") == 1


def test_greater_than_one():
    assert is_balanced("(((") == 1


def test_three():
    assert is_balanced("(((this is some text)))some more text") == 0


def test_three_unballanced():
    assert is_balanced("(((text))))(") == -1


def test_empty():
    assert is_balanced("") == 0


def test_no_paren():
    assert is_balanced("this is text no parenthesis") == 0


def test_jumbled_up():
    assert is_balanced("(()()))()") == -1


def test_will_it_break():
    assert is_balanced("()())(())(())(((") == -1
