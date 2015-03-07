from bin_heap import BinaryHeap


class SimpleGraph(object):
    '''This is a simple graph program that will allow us
                to impliment a graph data structure'''
    def __init__(self):
        self.dict_graph = {}

    def nodes(self):
        '''return a list of all nodes in the graph'''
        return self.dict_graph.keys()

    def edges(self):
        '''return a list of all edges in the graph'''
        edges = []
        for key, value in self.dict_graph.iteritems():
            for item in value:
                edges.append((key, item))
        return edges

    def add_node(self, n):
        '''adds a new node 'n' to the graph'''
        self.dict_graph.setdefault(n, {})

    def add_edge(self, n1, n2, weight=0):
        '''adds a new edge to the graph connecting 'n1' and 'n2',
        if either n1 or n2 are not already present in the graph,
        they should be added.'''
        self.dict_graph.setdefault(n2, {})
        if n1 in self.dict_graph:
            self.dict_graph[n1][n2] = weight
        else:
            self.dict_graph[n1] = {n2: weight}

    def del_node(self, n):
        '''deletes the node 'n' from the graph,
        raises an error if no such node exists'''
        del self.dict_graph[n]
        for key, value in self.dict_graph.items():
            if n in value:
                del value[n]

    def del_edge(self, n1, n2):
        '''deletes the edge connecting 'n1' and 'n2' from the graph,
        raises an error if no such edge exists'''
        del self.dict_graph[n1][n2]

    def has_node(self, n):
        '''True if node 'n' is contained in the graph, False if not.'''
        return n in self.dict_graph

    def neighbors(self, n):
        '''returns the list of all nodes connected to 'n' by edges,
        raises an error if n is not in graph'''
        return self.dict_graph[n]

    def adjacent(self, n1, n2):
        '''returns True if there is an edge connecting n1 and n2, False if not,
        raises an error if either of the supplied nodes are not in g'''
        if n2 in self.dict_graph[n1]:
            return True
        else:
            return False

    def breadth_first_traversal(self, start):
        visited = set()
        queue = [start]
        return_value = []
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                return_value.append(node)
                queue.extend(self.dict_graph[node])
        return return_value

    def _depth_first_visitor(self, node, visited, return_value):
        if node in visited:
            return

        visited.add(node)
        return_value.append(node)
        for child_node in self.dict_graph[node]:
            self._depth_first_visitor(child_node, visited, return_value)

    def depth_first_traversal(self, start, visited=None):
        return_value = []
        self._depth_first_visitor(start, set(), return_value)
        return return_value


def dijkstra(graph, src, dest):
    pass
    


if __name__ == '__main__':
    nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    graph = {
        'B': {'A': 5, 'D': 1, 'G': 2},
        'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
        'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
        'G': {'B': 2, 'D': 1, 'C': 2},
        'C': {'G': 2, 'E': 1, 'F': 16},
        'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
        'F': {'A': 5, 'E': 2, 'C': 16}
    }
    print dijkstra(graph, 'A', 'G')
