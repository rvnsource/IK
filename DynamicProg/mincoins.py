def minimum_coins(coins, value):
    """
    Args:
     coins(list_int32)
     value(int32)
    Returns:
     int32
    """
    # Write your code here.
    # declare array of size value+1
    # initialize them to -1

    table = [[0] for _ in range(value + 1)]

    # nothing of this demonmination
    table[0] = 0
    for i in range(1, value + 1):
        minvalue = float('inf')
        for c in coins:
            if i - c >= 0:
                minvalue = min(table[i - c], minvalue)
        table[i] = minvalue + 1
        res = table[value]
    print(f"{table[value]}")
    print('a')
    return table[value]


coins = [1,5,7]
value = 9
minimum_coins(coins, value)