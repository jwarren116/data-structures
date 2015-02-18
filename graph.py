
class SimpleGraph(object):
    '''This is a simple graph program that will allow us
                to impliment a graph data structure'''
    def __init__(self, dict_graph={}):
        self.dict_graph = dict_graph

    def node(self):
        '''return a list of all nodes in the graph'''
        return self.dict_graph.keys()

    def edges(self):
        '''return a list of all edges in the graph'''
        edges = ''
        for key, value in self.dict_graph.items():
            edges = '{}->{}  {}'.format(key, value, edges)
        return edges

    def add_node(self, n):
        '''adds a new node 'n' to the graph'''
        if n not in self.dict_graph:
            self.dict_graph[n] = []

    def add_edge(self, n1, n2):
        '''adds a new edge to the graph connecting 'n1' and 'n2',
        if either n1 or n2 are not already present in the graph,
        they should be added.'''
        if n1 in self.dict_graph:
            self.dict_graph[n1].append(n2)
            if n2 not in self.dict_graph:
                self.add_node(n2)
        else:
            self.dict_graph[n1] = [n2]
            if n2 not in self.dict_graph:
                self.add_node(n2)

    def del_node(self, n):
        '''deletes the node 'n' from the graph,
        raises an error if no such node exists'''
        try:
            del self.dict_graph[n]
            for value in self.dict_graph.items():
                if n in value:
                    value.remove(n)
        except KeyError:
            raise KeyError('That node does not exist')

    def del_edge(self, n1, n2):
        '''deletes the edge connecting 'n1' and 'n2' from the graph,
        raises an error if no such edge exists'''
        try:
            self.dict_graph[n1].remove(n2)
        except ValueError:
            raise ValueError('That edge does not exist')

    def has_node(self, n):
        '''True if node 'n' is contained in the graph, False if not.'''
        return n in self.dict_graph

    def neighbors(self, n):
        '''returns the list of all nodes connected to 'n' by edges,
        raises an error if n is not in graph'''
        try:
            return self.dict_graph[n]
        except KeyError:
            raise KeyError('There are no neighbors here')

    def adjacent(self, n1, n2):
        '''returns True if there is an edge connecting n1 and n2, False if not,
        raises an error if either of the supplied nodes are not in g'''
        try:
            if n2 in self.dict_graph[n1] or n1 in self.dict_graph[n2]:
                return True
            else:
                return False
        except KeyError:
            raise KeyError('That node is not in the graph')
