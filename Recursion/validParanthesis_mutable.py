def generate_parenthesis(n):
    def backtrack(s=[], left=0,right=0):
        if len(s) == 2 * n:
            result.append(''.join(s))

        if left < n:
            s.append('(')
            backtrack(s,left+1,right)
            s.pop()


        if right < left:
            s.append(')')
            backtrack(s, left, right+1)
            s.pop()

    result = []
    backtrack()
    return result


if __name__ == "__main__":
    # Example usage
    n = 2
    print(generate_parenthesis(n))
	#main()