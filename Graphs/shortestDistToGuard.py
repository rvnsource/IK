from collections import deque
def find_shortest_distance_from_a_guard(grid):
    """
    Args:
     grid(list_list_char)
    Returns:
     list_list_int32
    """
    # Write your code here.

    rows = len(grid)
    cols = len(grid[0])

    # only coordinates not content values
    def getValidNeighbours(x, y):
        res = []
        # (1,0),(-1,0),(0,1),(0,-1)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r, c in directions:
            nx = x + r
            ny = y + c
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] !="W":
                res.append((nx, ny))
        return res

    def bfs(x, y):
        q = deque()
        visited = [[0] * cols for _ in range(rows)]
        distance = [[0] * cols for _ in range(rows)]

        q.append((x, y))
        visited[x][y] = 1
        level = 0
        res = []

        while q:
            qlen = len(q)
            level += 1
            for _ in range(qlen):
                front = q.popleft()
                r,c = front
                for nr, nc in getValidNeighbours(r, c):
                    if grid[nr][nc] == "G":
                        return level
                    if visited[nr][nc] == 0:
                        visited[nr][nc] = 1
                        q.append((nr,nc))


        return -1

    # overall function call bfs for each [row][col]


    table = [[0] * cols for _ in range(rows)]
    distval = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            #row = 0
            #col = 0

            if grid[row][col] == "O":
                distval = bfs(row, col)
                table[row][col] = distval
            elif grid[row][col] == "W":
                table[row][col] = -1
            elif grid[row][col] == "G":
                table[row][col] = 0

    print(table)


print("start...")
grid = [
    ["O", "O", "O", "O", "G"],
    ["O", "W", "W", "O", "O"],
    ["O", "O", "O", "W", "O"],
    ["G", "W", "W", "W", "O"],
    ["O", "O", "O", "O", "G"]
]
find_shortest_distance_from_a_guard(grid)

