
from parenthetics import Parenthentic
# import pytest


def test_isone():
    text = Parenthentic()
    text.isequal("(")
    assert text.count == "1"


def test_isneg():
    text = Parenthentic()
    text.isequal(")")
    assert text.count == "-1"


def test_iszero():
    text = Parenthentic()
    text.isequal("()")
    assert text.count == "0"
