


def getValidNeighbours(x,y,rows,cols):
    res = []

    #for knights
    directions = [(2,1),(2,-1),(1,2),(1,-2), (1,2),(-1,2),(2,1),(-2,1)]
    #directions = [(1,0),(-1,0),(0,1),(0,-1)]

    for j,k in directions:
        nx,ny = x+ j,y+k
        if 0 <= nx < rows and 0 <= ny < cols:
            res.append((nx,ny))
    return res



res = getValidNeighbours(2,2,8,8)
print(res)

