from graph import SimpleGraph
import pytest


def test_add_nodes():
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    assert 'a' in g.nodes()
    assert 'b' in g.nodes()
    assert 'c' in g.nodes()


def test_del_nodes():
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    g.del_node('a')
    assert 'a' not in g.nodes()
    assert g.has_node('a') is False
    assert g.nodes() == ['c', 'b']


def test_del_error():
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    with pytest.raises(KeyError):
        g.del_node('p')


def test_del_edge():
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    g.del_edge('a', 'c')
    assert g.neighbors('a') == ['b']


def test_edge_error():
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    with pytest.raises(ValueError):
        g.del_edge('a', 'z')


def test_add_edge():
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    g.add_edge('q', 'a')
    assert g.has_node('q')
    assert g.neighbors('q') == ['a']


def test_has_node():
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    assert g.has_node('b')


def test_adjacent():
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'd')
    g.add_edge('a', 'f')
    assert 'f' in g.nodes()
    assert g.adjacent('a', 'd')
    assert not g.adjacent('a', 'b')


def test_adjacent_error():
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    with pytest.raises(KeyError):
        g.adjacent('l', 'm')


def test_edges():
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    assert ('a', 'c') in g.edges()
    assert ('a', 'b') in g.edges()
