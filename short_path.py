import heapq
import sys
# from graph import add_edges


def dijkstra(self, start, finish):
    distances = {}
    previous = {}
    nodes = []

    for edge in self.vertices:
        if edge == start:
            distances[edge] = 0
            heapq.heappush(nodes, [0, edge])
        else:
            distances[edge] = sys.maxint
            heapq.heappush(nodes, [sys.maxint, edge])
        previous[edge] = None

    while nodes:
        smallest = heapq.heappop(nodes)[1]
        if smallest == finish:
            path = []
            while previous[smallest]:
                path.append(smallest)
                smallest = previous[smallest]
            return path
        if distances[smallest] == sys.maxint:
            break

        for neighbor in self.vertices[smallest]:
            alt = distances[smallest] + self.vertices[smallest][neighbor]
            if alt < distances[neighbor]:
                distances[neighbor] = alt
                previous[neighbor] = smallest
                for n in nodes:
                    if n[1] == neighbor:
                        n[0] = alt
                        break
                heapq.heapify(nodes)
    print distances

# g = Dijkstra()
# g.add_edge('A', {'B': 7, 'C': 8})
# g.add_edge('B', {'A': 7, 'F': 2})
# g.add_edge('C', {'A': 8, 'F': 6, 'G': 4})
# g.add_edge('D', {'F': 8})
# g.add_edge('E', {'H': 1})
# g.add_edge('F', {'B': 2, 'C': 6, 'D': 8, 'G': 9, 'H': 3})
# g.add_edge('G', {'C': 4, 'F': 9})
# g.add_edge('H', {'E': 1, 'F': 3})
# print g.shortest_path('A', 'H')
