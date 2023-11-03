


def zombie_cluster():
    """
    Args:
     zombies(list_str)
    Returns:
     int32
    """
    # Write your code here.
    zombies = ["10000", "01000", "00100", "00010", "00001"]

    # 1. CONVERT STR MATRIX TO INTEGER MATRIX
    numrows = len(zombies)
    integer_list = [int(char) for char in zombies[0]]
    numcols = len(integer_list)

    table = []

    print(table)

    for row in range(numrows):
        integer_list = [int(char) for char in zombies[row]]
        table.append(integer_list)

    print(table)

zombie_cluster()