class Graph:
    def __init__(self, graph_dict={}):
        self._graph = graph_dict

    def add_vertex(self, vertex):
        if vertex not in self._graph:
            self._graph[vertex] = []

    def add_edge(self, v1, v2):
        if v1 in self._graph:
            self._graph[v1].append(v2)
        else:
            self._graph[v1] = [v2]

    def vertices(self):
        return list(self._graph.keys())

    def edges(self):
        return self._generate_edges()

    def _generate_edges(self):
        edges = []
        for vertex in self._graph:
            for neighbour in self._graph[vertex]:
                if (vertex, neighbour) not in edges:
                    edges.append((vertex, neighbour))
        return edges

    def is_isolated(self, vertex):
        if vertex not in self._graph.keys():
            return False

        if not len(self._graph[vertex]):
            return True
        
        for i in self._graph.keys():
            if vertex in i:
                return False
        else: return True

    def degree(self, vertex):
        if vertex not in self._graph.keys():
            return -1
        return len(self._graph[vertex]) #+ self._graph[vertex].count(vertex)

    def __str__(self):
        res = "Vertices: "
        for vertex in self.vertices():
            res += str(vertex) + " "
        res += "\nEdges: "
        for edge in self._generate_edges():
            res += str(edge) + " "
        return res
