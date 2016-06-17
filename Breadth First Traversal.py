def bfs(graph, start):
    """
    Graph and source vertex are given as arguments.
    Uses a dicitionary visited to save time in checking
    whether a node is visited or not.
    """
    visited = {v: False for v in graph.keys()}  # dictionary to mark if a node is visited or not
    visited[start] = True # marks source vertex as visited
    queue = [start]     # enqueue source vertex

    bfs_path = [start]  # stores the bfs traversal
    
    while len(queue):
        curr = queue.pop(0)     # gets currently active node
        for vertex in graph[curr]:  # traverses through neighbors
            if visited[vertex] == False:    # and if they are not already visited
                visited[vertex] = True      # mark them as visited
                bfs_path.append(vertex)     # and add it to the path
                queue.append(vertex)        # as well as queue
    return bfs_path         # return the traversal

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

    print("BFS :: ", end=" ")
    for i in bfs(g, 'a'):
        print(i, end=' ')
