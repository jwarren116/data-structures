
from parenthetics import Parenthentic
import pytest


def test_isone():
    text = Parenthentic()
    assert text.isequal("(") == 1


def test_isneg():
    text = Parenthentic()
    assert text.isequal(")") == -1


def test_iszero():
    text = Parenthentic()
    assert text.isequal("( )") == 0


def test_withstring():
    text = Parenthentic()
    assert text.isequal("this is a (string) with open and close") == 0


def test_mismatched():
    text = Parenthentic()
    assert text.isequal("This is a string with )))))(((((( wrong order") == -1
