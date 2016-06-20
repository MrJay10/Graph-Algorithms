def dfs(graph, vert, visited=dict()):
    visited[vert] = True
    print(vert, end=" ")

    for vertex in graph[vert]:
        if visited[vertex] == False:
            dfs(graph, vertex, visited)


if __name__ == '__main__':
    g = {'a': ['b', 's'],
     'b': ['a'],
     'c': ['d', 'e', 'f', 's'],
     'd': ['c'],
     'e': ['c', 'h'],
     'f': ['c', 'g'],
     'g': ['f', 'h', 's'],
     'h': ['e', 'g'],
     's': ['a', 'c', 'g']
     }

    v = {i: False for i in g.keys()}
    print("Depth First Traversal (starting from a): ", end=" ")
    dfs(g, 'a', v)
