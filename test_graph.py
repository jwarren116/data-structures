from graph import SimpleGraph
import pytest


def test_add_nodes():
    g = SimpleGraph()
    {"a": ["d"],
        "b": ["c"],
        "c": ["b", "c", "d", "e"],
        "d": ["a", "c"],
        "e": ["c"],
        "f": []}
    assert g.node() == ['a', 'c', 'b', 'e', 'd', 'f']
