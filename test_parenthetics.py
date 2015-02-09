
from parenthetics import isequal
import pytest


def test_isequal():
    text.isequal("(")
    assert count == "1"

    text.isequal(")")
    assert count == "-1"

    text.isequal("()")
    assert count == "0"
