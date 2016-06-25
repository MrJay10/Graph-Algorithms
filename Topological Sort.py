class Graph:
    """
    Uses a set data structure to store edges.
    """
    def __init__(self, graph_dict=dict()):
        self._graph = graph_dict

    def add_vertex(self, vertex):
        if vertex not in self._graph.keys():
            self._graph[vertex] = set()     # make a new node and associate a set to store neighbors

    def add_edges(self, v1, v2):
        if v1 not in self._graph.keys():
            self._graph[v1] = {v2}
        else:
            self._graph[v1].add(v2)
        self.add_vertex(v2)     # add v2 as a node if it is not already present

    def vertices(self):
        return self._graph.keys()

    def top_sort_util(self, vertex, visited, stack):
        visited.add(vertex)
        for v in self._graph[vertex]:
            if v in visited:
                continue
            self.top_sort_util(v, visited, stack)
        stack.append(vertex)

    def top_sort(self):
        visited = set()   # set which stores visited vertices
        stack = list()    # stack to store topologically sorted vertices

        vertices = self.vertices()
        for vertex in vertices:
            if vertex in visited:
                continue
            self.top_sort_util(vertex, visited, stack)

        return stack


if __name__ == '__main__':
    graph = Graph()
    graph.add_edges('a', 'c')
    graph.add_edges('b', 'c')
    graph.add_edges('b', 'e')
    graph.add_edges('c', 'd')
    graph.add_edges('d', 'f')
    graph.add_edges('e', 'f')
    graph.add_edges('a', 'c')
    graph.add_edges('f', 'g')

    t_sort = graph.top_sort()
    while t_sort:
        print(t_sort.pop(), end='')
