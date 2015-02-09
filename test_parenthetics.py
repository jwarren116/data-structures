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


def test_text():
    assert parenthetics("This is a silly test!") == 0


def test_text_parens():
    assert parenthetics("This is a silly test (but not really that silly)!") == 0
