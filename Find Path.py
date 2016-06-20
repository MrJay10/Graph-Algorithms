def find_path(graph, start, end, path = []):    # Not the shortest path
    path += [start]

    if start == end:
        return path
    
    if start not in graph:
        return None

    for vertex in graph[start]:
        if vertex not in path:
            extended_path = find_path(graph, vertex, end, path)
            if extended_path: return extended_path

    return None


if __name__ == '__main__':
    g = {'a': ['s', 'b'],
     'b': ['a'],
     'c': ['d', 'e', 'f', 's'],
     'd': ['c'],
     'e': ['c', 'h'],
     'f': ['c', 'g'],
     'g': ['h', 'f', 's'],
     'h': ['e', 'g'],
     's': ['g', 'c', 'a']
     }

    path = find_path(g, 'a', 'c')
    if path:
        print("Path: ", end=" ")
        for i in path:
            print(i, end=" ")
