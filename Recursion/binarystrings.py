
"""
def binarystrings(n):
    if n==1:
        return [str('p'),str('a'),str('l')]
    else:
        prev_result = binarystrings(n-1)
        result = [] #empty list or an array
        for s in prev_result:
            result.append(s+ "p")
            result.append(s + "a")
            result.append(s + "l")
        return result
"""
def binarystrings(n):
    if n==1:
        return [str('0'),str('1')]
    else:
        prev_result = binarystrings(n-1)
        result = [] #empty list or an array
        for s in prev_result:
            result.append(s+ "0")
            result.append(s + "1")
        return result



if __name__ == "__main__":
    print(binarystrings(3))
