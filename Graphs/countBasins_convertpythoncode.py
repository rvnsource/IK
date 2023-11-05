def get_sink(matrix, basins, row, column, basin_index):
    if basins[row][column] == -1:
        min_row, min_column = row, column

        # Check element which is at left.
        if column > 0 and matrix[row][column - 1] < matrix[min_row][min_column]:
            min_column = column - 1
            min_row = row

        # Check element which is at up.
        if row > 0 and matrix[row - 1][column] < matrix[min_row][min_column]:
            min_column = column
            min_row = row - 1

        # Check element which is at down.
        if row < len(matrix) - 1 and matrix[row + 1][column] < matrix[min_row][min_column]:
            min_column = column
            min_row = row + 1

        # Check element which is at right.
        if column < len(matrix[0]) - 1 and matrix[row][column + 1] < matrix[min_row][min_column]:
            min_column = column + 1
            min_row = row

        # If we found a sink.
        if min_row == row and min_column == column:
            basins[row][column] = basin_index
        else:
            # Recursively call to find a sink for element matrix[min_row][min_column].
            basins[row][column] = get_sink(matrix, basins, min_row, min_column, basin_index)

    return basins[row][column]

def find_basins(matrix):
    row_count = len(matrix)
    column_count = len(matrix[0])

    # To maintain ids of each element of matrix.
    basins = [[-1 for _ in range(column_count)] for _ in range(row_count)]

    basin_index = 0

    for i in range(row_count):
        for j in range(column_count):
            if get_sink(matrix, basins, i, j, basin_index) == basin_index:
                basin_index += 1

    # To store sink sizes.
    basin_sizes = [0] * basin_index

    for i in range(row_count):
        for j in range(column_count):
            basin_sizes[basins[i][j]] += 1

    # Sorting on sink sizes (you may need to implement count_sort separately).
    basin_sizes.sort()

    return basin_sizes




# Example terrain grid

matrix = [
[1, 5, 2],
[2, 4, 7],
[3, 6, 9]
]
num_basins = find_basins(matrix)
print("Number of basins:", num_basins)