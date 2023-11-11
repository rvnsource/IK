def climbStairs(n):


    if n == 0 or n == 1 or n == 2:
        return n

    # table = [0] * (n+1)
    table = [0] * (3)

    table[1] = 1
    table[2] = 2

    print('hello')

    for i in range(3, 6):
        # table[i] = table[i-1] + table[i-2]
        y = table[(i) % 3] = table[(i + 1) % 3] + table[(i + 2) % 3]
        print(y)
    print(f"i is {0}",i)
    return table[(i) % 3]





# Example usage:
N = 5
ways = climbStairs(N)
print(f"Number of ways to climb {N} stairs: {ways}")
