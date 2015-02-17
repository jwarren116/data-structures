
class SimpleGraph(object):
    """This is a simple graph program that will allow us
    to impliment a graph data structure"""
    def __init__(self, n):
        self.n = n

    def node():
        '''return a list of all nodes in the graph'''
        pass

    def edges():
        '''return a list of all edges in the graph'''
        pass

    def add_node(self, n):
        '''adds a new node 'n' to the graph'''
        pass

    def add_edge(self, n1, n2):
        '''adds a new edge to the graph connecting 'n1' and 'n2',
        if either n1 or n2 are not already present in the graph,
        they should be added.'''
        pass

    def del_node(self, n):
        '''deletes the node 'n' from the graph,
        raises an error if no such node exists'''
        pass

    def del_edge(self, n1, n2):
        '''deletes the edge connecting 'n1' and 'n2' from the graph,
        raises an error if no such edge exists'''
        pass

    def has_node(self, n):
        '''True if node 'n' is contained in the graph, False if not.'''
        pass

    def neighbors(self, n):
        '''returns the list of all nodes connected to 'n' by edges,
        raises an error if n is not in g'''
        pass

    def adjacent(self, n1, n2):
        '''returns True if there is an edge connecting n1 and n2, False if not,
        raises an error if either of the supplied nodes are not in g'''
        pass
