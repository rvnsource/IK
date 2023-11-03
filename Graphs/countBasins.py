def findBasins(matrix):
    def findLowestNeighbor(x, y):
        min_altitude = matrix[x][y]
        min_neighbor = (x, y)

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] < min_altitude:
                min_altitude = matrix[nx][ny]
                min_neighbor = (nx, ny)

        return min_neighbor

    labels = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    label_counter = 1

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if labels[x][y] == 0:  # Cell is not labeled
                current_x, current_y = x, y
                while labels[current_x][current_y] == 0:
                    lowest_neighbor = findLowestNeighbor(current_x, current_y)
                    current_x, current_y = lowest_neighbor

                if labels[x][y] == 0:  # If still not labeled, it's a sink
                    labels[x][y] = label_counter
                    label_counter += 1
                else:  # Otherwise, assign the label of the lowest neighbor
                    labels[x][y] = labels[current_x][current_y]

    basin_sizes = [0] * label_counter
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            basin_sizes[labels[x][y]] += 1

    # Remove the size of the zero label (unused)
    basin_sizes = basin_sizes[1:]

    return sorted(basin_sizes)

# Example usage:
matrix = [
    [1, 5, 2],
    [2, 4, 7],
    [3, 6, 9]
]

basin_sizes = findBasins(matrix)
print(basin_sizes)  # Output: [2, 7]
