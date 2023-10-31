from collections import deque


def count_islands(matrix):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    # initializations
    numrow = len(matrix)
    numcol = len(matrix[0])

    # getneighbours(x,y)->list_list_int32:
    def validgetneighbours(x, y):
        res = []
        if x + 1 < numrow and matrix[x+1][y] == 1:
            res.append((x + 1, y))

        if y + 1 < numcol and matrix[x][y+1] == 1:
                res.append((x, y + 1))
        if x - 1 >= 0 and matrix[x-1][y] == 1:
                res.append((x - 1, y))
        if y - 1 >= 0 and matrix[x][y-1] == 1:
                res.append((x, y - 1))
        """
        #  [x+1][y+1]  [x+1][y-1]  [x-1][y+1]  [x-1][y-1] diagnals
        if x+1 < len(matrix) and if matrix[x+1][y+1] == 1:
            res.append(x+1,y+1)
        """
        return res


# helperbfs
def helperbfs(x, y):
    q = deque()
    q.append((x, y))
    matrix[x][y] = 'A'

    while q:
        (fr, fc) = q.popleft()
        for nr, nc in validgetneighbours(fr, fc):
            q.append((nr, nc))
            matrix[nr][nc] = 'A'


    # overall bfs

    for row in range(numrow):
        for col in range(numcol):
            if matrix[row][col] == 1:
                helperbfs(row, col)
                counter += 1

    return counter

# overall bfs
counter = 0


for row in range(len()):
    for col in range(numcol):
        if matrix[row][col] == 1:
            helperbfs(row, col)
            counter += 1


print(f"islands {0}",counter)



