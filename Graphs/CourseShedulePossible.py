

def course_schedule(n, prerequisites):
    """
    Args:
     n(int32)
     a(list_int32)
     b(list_int32)
    Returns:
     bool
    """
    # Write your code here.

    visited = [0 for i in range(n)]
    adjList = [[] for _ in range(n)]

    for x,y in prerequisites:
        adjList[y].append(x)

    indegree = [0] * n
    for x,y in prerequisites:
        indegree[x] += 1

    def dfs(v,res):

        visited[v] = 1

        for neigh in adjList[v]:
            if visited[neigh] == 0:
                dfs(neigh,res)

        res.append(v)
        return res


    # overall
    res = []
    final = []
    for v in range(n):
        if indegree[v] == 0:
            dfs(v,res)



n = 4
prerequisites = [
[1, 0],
[2, 0],
[3, 1],
[3, 2]
]
print('hi')
result = course_schedule(n, prerequisites)
