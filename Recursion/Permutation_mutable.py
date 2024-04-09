def Permutation(nums):
    solution = []
    result = []
    def backtrack():


        if len(nums) == len(solution):
            result.append(solution[:])


        for num in nums:
            if not num in solution:
                solution.append(num)
                backtrack()
                solution.pop()

    backtrack()
    return result


nums = [1,2,3]
print(Permutation(nums))