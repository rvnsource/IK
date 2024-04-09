def Permutation(nums):

    result = []

    def backtrack(solution):


        if len(nums) == len(solution):
            result.append(solution)


        for num in nums:
            if not num in solution:
                backtrack(solution + [num])


    backtrack([])
    return result


nums = [1,2,3]
print(Permutation(nums))