from graph import SimpleGraph
import pytest


def test_add_nodes():
    G = SimpleGraph()
    G.add_node([A, B])
    G.add_node([A, C])
    G.add_node([B, D])
    assert SimpleGraph() == ([A, B], [A, C], [B, D])
