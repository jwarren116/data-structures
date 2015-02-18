from graph import SimpleGraph
import pytest


test_dict = {"a": ["d"],
             "b": ["c"],
             "c": ["b", "c", "d", "e"],
             "d": ["a", "c"],
             "e": ["c"],
             "f": []}


def test_add_nodes():
    g = SimpleGraph(test_dict)
    assert 'a' in g.node()
    assert 'b' in g.node()
    assert 'c' in g.node()
    assert 'd' in g.node()
    assert 'e' in g.node()
    assert 'f' in g.node()


def test_del_nodes():
    g = SimpleGraph(test_dict)
    g.del_node('a')
    assert 'a' not in g.node()
    assert g.has_node('a') is False
    assert g.node() == ['c', 'b', 'e', 'd', 'f']
    g.add_node('a')


def test_del_edge():
    g = SimpleGraph(test_dict)
    g.del_edge('c', 'd')
    assert g.neighbors('c') == ['b', 'c', 'e']


def test_add_edge():
    g = SimpleGraph(test_dict)
    g.add_edge('q', 'a')
    assert g.has_node('q')
    assert g.neighbors('q') == ['a']


def test_has_node():
    g = SimpleGraph(test_dict)
    assert g.has_node('b')


def test_adjacent():
    g = SimpleGraph(test_dict)
    assert g.adjacent('a', 'd')
    assert not g.adjacent('a', 'f')


def test_edges():
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    assert g.has_node('a')
    assert  'c' in g.node()
    assert g.edges() == '''b->[]  c->[]  a->['c', 'b']  '''
