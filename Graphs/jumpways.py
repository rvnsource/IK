def can_reach_last_house(maximum_jump_lengths):
    """
    Args:
     maximum_jump_lengths(list_int32)
    Returns:
     bool
    """
    # Write your code here.

    n = len(maximum_jump_lengths)
    last = n - 1
    for i in range(n - 1, -1, -1):
        if i + maximum_jump_lengths[i] >= last:
            last = i
    print(last == 0)


# main
# maximum_jump_lengths = [2, 3, 1, 0, 4, 7]
maximum_jump_lengths = [3, 2, 1, 0, 1, 2, 3]
can_reach_last_house(maximum_jump_lengths)
"""
    # build adjList of vertex size is len of maximum_jump_lengths list
    # traverse dfs from verex 0. check if last vertex and return visited[len(maximum_jump_lengths)] - )
    size = len(maximum_jump_lengths)
    visited = [0] * (size)
    adjList = [[] for _ in range(size)]

    # building a adjList
    for idx, neighs in enumerate(maximum_jump_lengths):
        #friends = 0
        for localIdx in range(neighs):
            friends = idx + localIdx + 1
            if friends < size:
                adjList[idx].append(friends)

    def dfs(v):
        visited[v] = 1

        for neigh in adjList[v]:
            if visited[neigh] == 0:
                dfs(neigh)

    dfs(0)
    print(visited[size - 1])
    if visited[size - 1] != 1:
        return False

    return True
"""
