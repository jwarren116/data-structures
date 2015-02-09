import pytest
from parenthetics import parenthetics


def test_single_open():
    assert parenthetics("(") == 1


def test_single_close():
    assert parenthetics(")") == -1


def test_single_balanced():
    assert parenthetics("()") == 0


def test_multi_open_close_1():
    assert parenthetics("(()") == 1


def test_multi_open_close_2():
    assert parenthetics("())") == -1


def test_broken():
    assert parenthetics("))((") == -1
