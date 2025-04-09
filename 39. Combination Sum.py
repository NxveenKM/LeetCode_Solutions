class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path)
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                backtrack(i, path + [candidates[i]], remaining - candidates[i])

        backtrack(0, [], target)
        return result
