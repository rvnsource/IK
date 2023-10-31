from collections import deque


def is_it_a_tree(node_count, edge_start, edge_end):
    """
    Args:
     node_count(int32)
     edge_start(list_int32)
     edge_end(list_int32)
    Returns:
     bool
    """
    # Write your code here.

    # declarations
    adjList = [[] for _ in range(node_count)]
    parent = [-1] * node_count
    visited = [-1] * node_count

    # adjLkist build
    for i in range(len(edge_start)):
        adjList[edge_start[i]].append(edge_end[i])
        adjList[edge_end[i]].append(edge_start[i])

    # helperbfs
    def helperbfs(v):
        q = deque()
        visited[v] = 1
        q.append(v)

        while q:
            front = q.popleft()
            for neigh in adjList[front]:
                if visited[neigh] == -1:
                    visited[neigh] = 1
                    q.append(neigh)
                    parent[neigh] = front
                else:
                    if neigh != parent[front]:
                        return False
        return True

    # overall
    counter = 0
    flag = False
    for v in range(node_count):
        if visited[v] == -1:
            counter += 1
            if counter > 1:
                return False
            flag = helperbfs(v)
    if flag:
        return True
    else:
        return False


# Example usage:
node_count = 4
edge_start = [0, 0, 0]
edge_end = [1, 2, 3]


result = is_it_a_tree(node_count, edge_start, edge_end)
print(result)  # Output: True
