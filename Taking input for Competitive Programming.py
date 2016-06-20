from Graph import Graph

graph = dict()

# Remove the message in input(); change str -> int for integer input
vertices = list(map(str, input("Enter vertices :: ").split()))

for vertex in vertices:
    # Remove the message in input(); change str -> int for integer input
    graph[vertex] = list(map(str, input("Enter neighbors of "+vertex+" -> ").split()))

g = Graph(graph)
print("Your Graph is ::\n\n"+str(g)+"\n")
