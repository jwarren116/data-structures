from bin_heap import BinaryHeap as heap


class SimpleGraph(object):
    '''This is a simple graph program that will allow us
                to impliment a graph data structure'''
    def __init__(self, edges=None):
        self.dict_graph = {}

    def nodes(self):
        '''return a list of all nodes in the graph'''
        return self.dict_graph.iterkeys()

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


def dijkstra(self, start):
    '''Using a binary heap to traverse the graph'''
    binheap = [(0, start)]

    '''using a dict comprehension to go through the nodes.
       assuming that an unvisited node is an infinitive
       value untill I can prove otherwise'''
    costs = {node: float('inf') for node in self.nodes()}
    costs[start] = 0

    while binheap:
        cost, node = heap.pop(binheap)

        for child in self.connected(node):
            new_cost = costs[node] + self.cost(node, child)
            if costs[child] > new_cost:
                costs[child] = new_cost
                heap.push(binheap, (new_cost, child))

    return costs


if __name__ == '__main__':
    graph = SimpleGraph([('a', 'b', 6), ('b', 'a', 5), ('a', 'g', 1), ('g', 'b', 1)])
    print dijkstra('a', 'g')
