
def course_schedule(n, prerequisites):
    """
    Args:
     n(int32)
     prerequisites(list_list_int32)
    Returns:
     list_int32
    """
    # Write your code here.

    # a->b adjList
    alen = len(a)
    blen = len(b)
    visited = [0 for i in range(n)]
    arr = [0] * n
    dep = [0] * n

    adjList = [[] for _ in range(n)]
    for b,a in prerequisites:
        adjList[a[i]].append(b[i])

    def dfs(v):

        visited[v] = 1

        for neigh in adjList[v]:
            if visited[neigh] == 0:
                if not dfs(neigh):
                    return False
            else:
                if visited[neigh] == 1:
                    return False

        visited[v] = 2

        return True

    # overall
    for v in range(n):
        if visited[v] == 0:
            comp = dfs(v)
            if not comp:
                return False
    return True

