def generate_parenthesis(n):
    def backtrack(s='', left=0,right=0):
        if len(s) == 2 * n:
            result.append(s)

        if left < n:
            backtrack(s+'(',left+1,right)


        if right < left:
            backtrack(s + ')', left, right+1)

    result = []
    backtrack()
    return result


if __name__ == "__main__":
    # Example usage
    n = 2
    print(generate_parenthesis(n))
	#main()