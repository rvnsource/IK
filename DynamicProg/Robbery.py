def maximum_stolen_value(values):
    """
    Args:
     values(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    n = len(values)

    table = [-1] * (n + 1)
    table[0] = 0
    table[1] = values[0]
    table[2] = max(values[0], values[1])

    if n == 0 or n == 1 or n==2:
        return table[n]


    for i in range(3, n + 1):
        table[i] = max(table[i - 1], table[i - 2] + values[i - 1])
        print("")

    return table[n]


values = [6, 1, 2, 7]
print(maximum_stolen_value(values))