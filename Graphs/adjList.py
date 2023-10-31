class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)  # For undirected graph

    def display(self):
        for vertex, edges in self.graph.items():
            print(vertex, ":", edges)

# Driver Code
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.display()