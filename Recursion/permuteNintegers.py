def helper(arr,n):
    if n == 1:
        tmp = []
        arr_size = len(arr)
        for i in range(1, arr_size + 1, 1):
            tmp.append(i)
        return tmp

    else:
        prev = helper(arr, n-1)
        result = []

        for s in prev:
             for i in range(1, len(arr)+1, 1):
                result.append(i)
        return result


def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.

    res = helper(arr, len(arr))

    return res


"""
def main():
    arr = [1, 2, 3]
    get_permutations(arr)

"""

if __name__ == "__main__":
    arr = [1, 2, 3]
    get_permutations(arr)
	#main()
