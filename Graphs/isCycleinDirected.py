def has_cycle(number_of_vertices, number_of_edges, edges):
    # Form an adjList
    adjList = [[] for _ in range(number_of_vertices)]
    arrtime = [0] * number_of_vertices
    deptime = [0] * number_of_vertices
    visited = [0] * number_of_vertices

    for src, dst in edges:
        adjList[src].append(dst)

    # For finding a cycle in a Directed graph, run DFS and see if there is a back edge to an ancestor
    def dfshelper(node):
        arrtime[node] += 1
        visited[node] = 1
        for neigh in adjList[node]:
            if visited[neigh] == 0:
                if dfshelper(neigh):
                    return True
            else:
                if deptime[neigh] == 0:
                    return True
        deptime[node] += 1
        return False

    res = False  # Initialize res to False
    for v in range(number_of_vertices):
        if visited[v] == 0:
            res = dfshelper(v)  # Use a bitwise OR operation to combine results
            if res:
                return True

    return False  # Return the final result after the loop

# Example usage:
number_of_vertices = 10
number_of_edges = 9
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4,5), (5,6),(6,7),(7,8),(8,9)]

result = has_cycle(number_of_vertices, number_of_edges, edges)
print("Does the graph have a cycle?", result)
