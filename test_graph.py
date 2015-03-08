from graph import SimpleGraph
import pytest


def test_add_nodes():
    """nodes are added"""
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
    """nodes are deleted"""
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    g.del_node('a')
    assert 'a' not in g.nodes()
    assert g.has_node('a') is False


def test_del_error():
    """error raised when non-existant value deleted"""
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    with pytest.raises(KeyError):
        g.del_node('p')


def test_del_edge():
    """other edges preserved when one deleted"""
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    g.del_edge('a', 'c')
    assert g.neighbors('a') == {'b': 0}


def test_edge_error():
    """delete non-existant edge"""
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    with pytest.raises(KeyError):
        g.del_edge('a', 'z')


def test_add_edge():
    """edge added, new node added"""
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    g.add_edge('q', 'a')
    assert g.has_node('q')
    assert g.neighbors('q') == {'a': 0}


def test_has_node():
    """edge added, new node added"""
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    assert g.has_node('b')


def test_adjacent():
    """adjacent correctly identify edges, new edge add node"""
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
    """error raised when nodes non-existant"""
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    with pytest.raises(KeyError):
        g.adjacent('l', 'm')


def test_edges():
    """edges prints correct edges as tuples"""
    g = SimpleGraph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a', 'c')
    g.add_edge('a', 'b')
    assert ('a', 'c') in g.edges()
    assert ('a', 'b') in g.edges()


def test_breadth():
    g = SimpleGraph()
    g.add_edge('a', 'b')
    g.add_edge('a', 'c')
    g.add_edge('b', 'd')
    g.add_edge('b', 'e')
    g.add_edge('e', 'f')
    g.add_edge('f', 'g')
    assert g.breadth_first_traversal('a') == ['a', 'c', 'b', 'e', 'd', 'f', 'g']


def test_depth():
    g = SimpleGraph()
    g.add_edge('a', 'b')
    g.add_edge('a', 'c')
    g.add_edge('b', 'd')
    g.add_edge('b', 'e')
    g.add_edge('e', 'f')
    g.add_edge('f', 'g')
    assert g.depth_first_traversal('a') == ['a', 'c', 'b', 'e', 'f', 'g', 'd']


def test_one_breadth():
    g = SimpleGraph()
    g.add_node('a')
    assert g.breadth_first_traversal('a') == ['a']


def test_one_depth():
    g = SimpleGraph()
    g.add_node('a')
    assert g.depth_first_traversal('a') == ['a']


def test_one_loop_breadth():
    g = SimpleGraph()
    g.add_edge('a', 'a')
    assert g.breadth_first_traversal('a') == ['a']


def test_one_loop_depth():
    g = SimpleGraph()
    g.add_edge('a', 'a')
    assert g.depth_first_traversal('a') == ['a']


def fully_connected_graph(nodes):
    g = SimpleGraph()
    for node in nodes:
        g.add_node(node)
        for other_node in nodes:
            if other_node is not node:
                g.add_edge(node, other_node)
    return g


def test_fully_connected():
    g = fully_connected_graph(['a', 'b', 'c', 'd'])
    assert g.breadth_first_traversal('a') == ['a', 'c', 'b', 'd']


def test_fully_connected_again():
    g = fully_connected_graph(['a', 'b', 'c', 'd'])
    assert g.depth_first_traversal('a') == ['a', 'c', 'b', 'd']


def test_weighted_edges():
    g = SimpleGraph()
    g.add_edge('a', 'b', 5)
    g.add_edge('a', 'c', 2)
    g.add_edge('b', 'c', 1)
    assert g.dict_graph['a'] == {'b': 5, 'c': 2}


def test_weighted_edges_with_edge_delete():
    g = SimpleGraph()
    g.add_edge('a', 'b', 5)
    g.add_edge('a', 'c', 2)
    g.del_edge('a', 'c')
    assert g.dict_graph['a'] == {'b': 5}


def test_weighted_edges_with_node_delete():
    g = SimpleGraph()
    g.add_edge('a', 'b', 5)
    g.add_edge('a', 'c', 2)
    g.del_node('c')
    assert g.dict_graph['a'] == {'b': 5}


def test_dijkstra():
    graph = SimpleGraph([('a', 'b', 6), ('b', 'a', 5),
                         ('a', 'g', 1), ('g', 'b', 1)])
    assert graph.dijkstra('a') == {'a': 0, 'b': 2, 'g': 1}


def test_bellman_ford():
    """basic Bellman Ford algorithm test"""
    graph = SimpleGraph([('a', 'b', 6), ('b', 'a', 5),
                         ('a', 'g', 1), ('g', 'b', 1)])
    assert graph.bellmanford('a') == {'a': 0, 'b': 2, 'g': 1}


def test_bellman_ford_negative():
    """Bellman Ford algorithm test with negative cycle"""
    graph = SimpleGraph([('a', 'b', -1), ('b', 'a', -3),
                         ('a', 'g', 1), ('g', 'b', 1)])
    assert graph.bellmanford('a') == 'Graph contains a negative-weight cycle'
